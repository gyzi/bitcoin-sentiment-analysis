from requests_oauthlib import OAuth1Session
import os
import json
import boto3  # AWS SDK for Python

# Part 1: Fetch Bitcoin-related tweets (unchanged)
def fetch_bitcoin_tweets():
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")

    query = "#Bitcoin OR #BTC OR Bitcoin"
    tweet_count = 30

    params = {
        "query": query,
        "max_results": tweet_count,
        "tweet.fields": "created_at,author_id,text"
    }

    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print("Error: Check CONSUMER_KEY or CONSUMER_SECRET.")
        return None

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")

    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    print(f"Authorize here: {authorization_url}")
    verifier = input("Paste the PIN: ")

    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    response = oauth.get("https://api.twitter.com/2/tweets/search/recent", params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None

    json_response = response.json()
    with open("bitcoin_trends_tweets.json", 'w', encoding='utf-8') as f:
        json.dump(json_response, f, ensure_ascii=False, indent=4)

    print("Tweets saved to bitcoin_trends_tweets.json")
    return json_response

# Part 2: Perform sentiment analysis using AWS Comprehend
def analyze_sentiment(tweets):
    # Initialize AWS Comprehend client
    comprehend = boto3.client('comprehend', region_name='us-east-2')  # Update region as needed

    tweet_texts = [tweet['text'] for tweet in tweets['data']]
    
    # AWS allows up to 25 texts per batch request
    batch_size = 25
    sentiments = {"POSITIVE": 0, "NEUTRAL": 0, "NEGATIVE": 0, "MIXED": 0}

    for i in range(0, len(tweet_texts), batch_size):
        batch = tweet_texts[i:i+batch_size]
        
        # Call AWS Comprehend API
        response = comprehend.batch_detect_sentiment(
            TextList=batch,
            LanguageCode='en'
        )
        
        # Count sentiments
        for result in response['ResultList']:
            sentiment = result['Sentiment']
            sentiments[sentiment] += 1

    total_tweets = len(tweet_texts)
    sentiment_percentages = {
        sentiment.lower(): (count / total_tweets) * 100 
        for sentiment, count in sentiments.items()
    }
    
    return sentiment_percentages

# Main execution
if __name__ == "__main__":
    tweets = fetch_bitcoin_tweets()
    if tweets:
        sentiment_analysis = analyze_sentiment(tweets)
        print("Bitcoin Sentiment Analysis Results:")
        for sentiment, percentage in sentiment_analysis.items():
            print(f"{sentiment.capitalize()}: {percentage:.2f}%")
    else:
        print("Failed to fetch tweets.")