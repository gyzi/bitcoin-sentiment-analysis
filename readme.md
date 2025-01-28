# Bitcoin Sentiment Analysis from Twitter

## Description

This Python script fetches Bitcoin-related tweets and analyzes their sentiment using either **Azure AI Language** or **AWS Comprehend**. Designed for testing purposes with free-tier API limits.

## Prerequisites

- Python 3.7+
- Twitter Developer Account with API access
- **For Azure**:
  - Azure account with Language Service enabled
  - Free-tier keys (200K text records/month)
- **For AWS**:
  - AWS account with Comprehend access
  - IAM user with Comprehend permissions
  - AWS CLI configured (optional)

## Installation
```bash
#1. Clone the repository:
git clone https://github.com/gyzi/bitcoin-sentiment-analysis.git
cd bitcoin-sentiment-analysis
#2.Install required packages:
pip install -r requirements.txt
```

## Configuration
Set environment variables in your shell or .env file:
Twitter API: generate from here https://developer.twitter.com/en/portal/projects
- CONSUMER_KEY: Twitter API consumer key
- CONSUMER_SECRET: Twitter API consumer secret
Azure AI Language:
- AZURE_KEY: Language service key
- AZURE_ENDPOINT: Language service endpoint
AWS Comprehend:
- AWS_ACCESS_KEY_ID: IAM user access key
- AWS_SECRET_ACCESS_KEY: IAM user secret key
- AWS_REGION (optional): Defaults to 'us-east-1'

## Usage
Run with default settings (30 tweets):
```bash
#For Azure 
python bitcoin_tweets.py 
#For AWS 
python bitcoin_tweet_aws.py
```
The script will:
1. Authenticate with Twitter API
2. Fetch recent Bitcoin-related tweets
3. Perform sentiment analysis using your configured cloud service
4. Save tweets to bitcoin_trends_tweets.json
5. Display sentiment percentages

| Feature                | Azure AI Language                     | AWS Comprehend                      |
|------------------------|---------------------------------------|-------------------------------------|
| **Max Batch Size**     | 10 documents/request                  | 25 documents/request                |
| **Sentiment Labels**   | Positive, Neutral, Negative, Mixed    | Positive, Neutral, Negative, Mixed  |
| **Free Tier**          | 5,000 text records/month              | 50,000 text units/month             |
| **Pricing**            | $1 per 1,000 text records             | $0.0001 per text unit               |
| **Language Support**   | 125+ languages                        | 100+ languages                      |
| **API Type**           | Dedicated resource endpoint           | Regional service endpoint           |
| **Setup Complexity**   | Moderate (resource creation required) | Simple (IAM keys only)              |

### Choose Azure if:
You need opinion mining (aspect-based sentiment)
You're already using Azure ecosystem
Require strict compliance certifications

### Choose AWS if:
You want higher batch sizes
Prefer pay-per-use pricing model
Need seamless integration with other AWS services

