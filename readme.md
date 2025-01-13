# Bitcoin Sentiment Analysis from Twitter

## Description

This Python script fetches Bitcoin-related tweets and analyzes their sentiment using Twitter API and Azure AI Language services. It's designed for testing purposes using free-tier API limits.

## Prerequisites

- Python 3.7+
- Twitter Developer Account with API access
- Azure account with AI Language service (Free tier)

## Installation

1. Clone the repository:
```
git clone https://github.com/gyzi/bitcoin-sentiment-analysis.git
cd bitcoin-sentiment-analysis
```
2. Install required packages:
```
pip install -r requirements.txt
```
## Configuration
Set the following environment variables:

- `CONSUMER_KEY`: Your Twitter API consumer key
- `CONSUMER_SECRET`: Your Twitter API consumer secret
- `AZURE_KEY`: Your Azure AI Language key
- `AZURE_ENDPOINT`: Your Azure AI Language endpoint

You can set these in your shell or use a `.env` file with a package like `python-dotenv`.
## Usage

Run the script:
```
python bitcoin_tweets.py
```
Follow the prompts to authorize the Twitter API access. The script will then fetch tweets, perform sentiment analysis, and display the results.

## Features

- Fetches recent Bitcoin-related tweets "by default is set 30"
- Saves tweets to a JSON file
- Performs sentiment analysis in batches of 10 tweets
- Displays sentiment analysis results as percentages

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)