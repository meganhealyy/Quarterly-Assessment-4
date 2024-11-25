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

def fetch_articles_for_topics():
    # Step 1: Get user input for multiple topics
    topics = input("Enter topics you're interested in, separated by commas (e.g., technology, sports, health): ").strip()
    topics = [topic.strip() for topic in topics.split(",") if topic.strip()]  # Remove empty strings and whitespace

    if not topics:
        print("You must enter at least one topic. Please try again.")
        return

    # Step 2: Define the API endpoint
    BASE_URL = 'https://newsapi.org/v2/top-headlines'

    all_articles = {}  # Dictionary to store articles for each topic

    for topic in topics:
        params = {
            'q': topic,  # User-specified topic
            'apiKey': API_KEY,
            'language': 'en',
            'pageSize': 5  # Limit to 5 articles per topic
        }

        try:
            # Step 3: Make the API request for the current topic
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for HTTP issues

            # Step 4: Parse the JSON response
            articles = response.json().get('articles', [])
            if not articles:
                print(f"No articles found for the topic '{topic}'.")
                continue

            # Store articles in the dictionary
            all_articles[topic] = articles

            # Print and log the headlines, descriptions, and links for the current topic
            print(f"\nArticles for '{topic}':")
            for i, article in enumerate(articles, start=1):
                print(f"{i}. {article['title']}")
                print(f"   Description: {article['description']}")
                print(f"   Link: {article['url']}\n")
                logging.info(f"Topic '{topic}' - Article: {article['title']} - {article['url']}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching news for topic '{topic}': {e}")
            print(f"Error fetching news for topic '{topic}': {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print(f"An unexpected error occurred: {e}")

    # Step 5: Save all results to a JSON file
    if all_articles:
        filename = f"articles_summary_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(filename, 'w') as file:
            json.dump(all_articles, file, indent=4)
        print(f"\nAll articles saved to '{filename}'.")

if __name__ == "__main__":
    fetch_articles_for_topics()
