from fetch_data import fetch_articles
from summarize_data import summarize_article
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("key")
OPENAI_API_KEY = os.getenv("open_ai_key")

if not NEWS_API_KEY or not OPENAI_API_KEY:
    raise ValueError("API keys are missing. Ensure they're stored in the .env file.")

def main():
    # Get topics from the user
    topics = input("Enter topics you're interested in, separated by commas: ").strip().split(',')
    topics = [topic.strip() for topic in topics if topic.strip()]

    if not topics:
        print("Please provide at least one topic.")
        return

    # Fetch and summarize articles for each topic
    for topic in topics:
        articles = fetch_articles(topic, NEWS_API_KEY)
        print(f"\nArticles for '{topic}':")
        
        for idx, article in enumerate(articles[:5], start=1):  # Limit to 5 articles per topic
            headline = article.get('title', 'No title available')
            content = article.get('content', 'No content available')
            link = article.get('url', 'No URL available')

            print(f"\nArticle {idx}:")
            print(f"Headline: {headline}")
            print(f"Link: {link}")

            # Generate and print summary
            summary = summarize_article(content, OPENAI_API_KEY)
            print(f"Summary: {summary}")

if __name__ == "__main__":
    main()
