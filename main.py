import os
from dotenv import load_dotenv
from fetch_data import fetch_articles
from summarize_data import summarize_article
from send_email import send_email

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get API keys from environment variables
    news_api_key = os.getenv("key")
    openai_api_key = os.getenv("open_ai_key")

    if not news_api_key or not openai_api_key:
        print("API keys are missing. Please check your .env file.")
        return

    # Prompt user for email details
    recipient_email = input("Enter your email address to receive the summary: ").strip()
    sender_email = input("Enter your Gmail address: ").strip()
    password = input("Enter your Gmail password or app-specific password: ").strip()

    # Validate the topic input
    topic = input("Enter a topic you're interested in (e.g., technology, sports, health): ").strip()

    # Fetch articles
    articles = fetch_articles(topic, news_api_key)
    if not articles:
        print(f"No articles found for the topic: {topic}")
        return

    # Summarize articles
    summaries = []
    for article in articles:
        title = article.get("title", "No Title")
        url = article.get("url", "No URL")
        content = article.get("content", "No Content Available")
        summary = summarize_article(content, openai_api_key)
        summaries.append(f"**{title}**\n{summary}\nRead more: {url}\n")

    # Format the email body
    email_body = "\n\n".join(summaries)

    # Use Gmail's SMTP details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Send the email
    try:
        send_email(smtp_server, smtp_port, sender_email, password, recipient_email, "Your News Summary", email_body)
        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    main()
