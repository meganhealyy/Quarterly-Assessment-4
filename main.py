from fetch_data import fetch_articles
from summarize_data import summarize_article
from send_email import send_email
import os
from dotenv import load_dotenv

def main():
    # Get user inputs for email details and topic
    load_dotenv()
    recipient_email = input("Enter your email address to receive the summary: ").strip()
    password = input("Enter your Gmail password or app-specific password: ").strip()
    topic = input("Enter a topic you're interested in (e.g., technology, sports, health): ").strip()

    # Define SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Fetch articles
    api_key = os.getenv("key")  # Ensure your News API key is set in the .env file
    articles = fetch_articles(topic, api_key)

    if not articles:
        print(f"No articles found for the topic: {topic}")
        return

    # Summarize articles
    open_ai_key = os.getenv("open_ai_key")  # Ensure your OpenAI API key is set in the .env file
    summaries = summarize_article(articles, open_ai_key)

    # Format email content
    email_body = f"Topic: {topic}\n\n"
    email_body += "Here are the latest articles and their summaries:\n\n"
    for i, article in enumerate(articles):
        title = article.get("title", "No title")
        url = article.get("url", "No URL available")
        summary = summaries[i] if i < len(summaries) else "No summary available"
        email_body += f"{i+1}. {title}\nLink: {url}\nSummary: {summary}\n\n"

    # Clean up the email body (remove non-ASCII characters)
    email_body = clean_text(email_body)

    # Send the email
    try:
        send_email(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            from_email=recipient_email,  # Use the recipient's email as sender
            password=password,
            to_email=recipient_email,  # Send the email to the same address
            subject="Your News Summary",
            body=email_body
        )
        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def clean_text(text):
    """
    Cleans up the text to remove any unwanted non-ASCII characters, 
    including non-breaking spaces and other special characters.
    """
    # Replace non-breaking spaces and other special characters
    cleaned_text = text.replace('\xa0', ' ')  # Replace non-breaking space with a regular space
    # You can further add other characters to replace or remove if needed
    return cleaned_text

if __name__ == "__main__":
    main()
