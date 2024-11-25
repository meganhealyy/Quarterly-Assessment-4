# main.py

import os
from dotenv import load_dotenv
from fetch_data import fetch_articles
from summarize_data import summarize_articles
from send_email import send_email_smtp, send_sendgrid_email

# Load the .env file for API key and email credentials
load_dotenv()

def main():
    # Get the API key for OpenAI
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    # Fetch articles for a given topic
    topic = input("Enter a topic you're interested in (e.g., technology, sports, health): ")
    articles = fetch_articles(topic)
    
    # Summarize the articles
    summaries = summarize_articles(articles, openai_api_key)
    
    # Format the email body with summaries
    body = "Here are your daily news summaries:\n\n" + "\n".join([f"- {summary}" for summary in summaries])
    
    # Email details
    subject = f"Latest News Summary for {topic.capitalize()}"
    to_email = "recipient@example.com"  # Replace with the recipient's email
    from_email = "your_email@example.com"  # Replace with your email

    # Option 1: Send email using smtplib
    # Use your SMTP details (replace with your own details)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = "your_email@example.com"  # Your email login
    password = "your_email_password"  # Your email password or app-specific password
    send_email_smtp(subject, body, to_email, from_email, smtp_server, smtp_port, login, password)

    # Option 2: Send email using SendGrid (uncomment the below line if you prefer SendGrid)
    # api_key = "your_sendgrid_api_key"  # Replace with your SendGrid API key
    # send_sendgrid_email(subject, body, to_email, from_email, api_key)

if __name__ == "__main__":
    main()
