import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def clean_body(body):
    """
    Cleans up the email body to avoid encoding errors.
    Replaces non-breaking spaces and other problematic characters with standard ones.
    """
    # Replace non-breaking spaces (0xA0) with regular spaces
    body = body.replace("\xa0", " ")
    
    # You can add more replacements or clean up as needed, for example:
    # body = body.replace("some_other_char", "replacement")

    return body

def send_email(smtp_server, smtp_port, from_email, password, to_email, subject, body):
    """
    Sends an email with the specified parameters.

    Parameters:
    smtp_server (str): The SMTP server address (e.g., 'smtp.gmail.com').
    smtp_port (int): The SMTP port (e.g., 587 for TLS).
    from_email (str): The sender's email address.
    password (str): The sender's email password or app-specific password.
    to_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body of the email.
    """
    try:
        # Clean the email body to ensure no problematic characters remain
        clean_email_body = clean_body(body)
        
        # Create the email content
        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject
        
        # Attach the cleaned email body (with UTF-8 encoding to handle special characters)
        message.attach(MIMEText(clean_email_body, "plain", "utf-8"))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message.as_string())
        print(f"Email successfully sent to {to_email}")
    
    except Exception as e:
        print(f"Failed to send email: {e}")
