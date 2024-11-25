import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, smtp_port, from_email, password, to_email, subject, body):
    """
    Sends an email using the provided SMTP server.

    Parameters:
    smtp_server (str): The SMTP server to connect to.
    smtp_port (int): The SMTP port to use.
    from_email (str): The sender's email address.
    password (str): The sender's email password.
    to_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body of the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add the body content to the email (ensure UTF-8 encoding)
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS for security
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())

        print(f"Email successfully sent to {to_email}")
    
    except Exception as e:
        print(f"Failed to send email: {e}")
