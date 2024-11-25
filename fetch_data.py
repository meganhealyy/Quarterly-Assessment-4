import requests
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from .env
API_KEY = os.getenv("key")
if not API_KEY:
    raise ValueError("API key not found in .env file. Please set 'NEWS_API_KEY'.")

# Setup logging
logging.basicConfig(
    filename="news_fetch.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_articles():
    # Step 1: Get user input for the topic
    topic = input("Enter a topic you're interested in (e.g., technology, sports, health): ").strip()
    if not topic:
        print("Topic cannot be empty. Please try again.")
        return

    # Step 2: Define the API endpoint and parameters
    BASE_URL = 'https://newsapi.org/v2/top-headlines'

    params = {
        'q': topic,  # User-specified topic
        'apiKey': API_KEY,
        'language': 'en',
        'pageSize': 5  # Limit to 5 articles for testing
    }

    try:
        # Step 3: Make the API request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Step 4: Parse the JSON response
        articles = response.json().get('articles', [])
        if not articles:
            print(f"No articles found for the topic '{topic}'.")
            return

        # Step 5: Print and log the headlines and links
        print(f"\nLatest Articles on '{topic}':")
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['title']}")
            print(f"   Link: {article['url']}\n")
            logging.info(f"Fetched article: {article['title']} - {article['url']}")

        # Step 6: Save the results to a JSON file
        filename = f"articles_{topic}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(filename, 'w') as file:
            json.dump(articles, file, indent=4)
        print(f"Articles saved to '{filename}'.")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching news: {e}")
        print(f"Error fetching news: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_articles()
