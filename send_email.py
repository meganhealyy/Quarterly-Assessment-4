# send_email.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

# Function to send email using smtplib
def send_email_smtp(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    """
    Sends an email with the given subject and body to the provided recipient email using smtplib.
    
    Parameters:
    subject (str): The subject of the email.
    body (str): The body content of the email.
    to_email (str): The recipient's email address.
    from_email (str): The sender's email address.
    smtp_server (str): The SMTP server (e.g., smtp.gmail.com).
    smtp_port (int): The port number for the SMTP server (usually 587 for TLS).
    login (str): The email login.
    password (str): The email password or app-specific password.
    """
    # Set up the MIME (Multipurpose Internet Mail Extensions) message structure
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body as plain text
    msg.attach(MIMEText(body, 'plain'))

    # Establish an SMTP connection and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(login, password)  # Login to the SMTP server using provided credentials
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)  # Send the email
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Function to send email using SendGrid
def send_sendgrid_email(subject, body, to_email, from_email, api_key):
    """
    Sends an email using SendGrid API with the provided subject and body.
    
    Parameters:
    subject (str): The subject of the email.
    body (str): The body content of the email.
    to_email (str): The recipient's email address.
    from_email (str): The sender's email address.
    api_key (str): SendGrid API key for authentication.
    """
    sg = sendgrid.SendGridAPIClient(api_key)
    from_email = Email(from_email)
    to_email = To(to_email)
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, subject, content)

    try:
        response = sg.send(mail)
        print(f"Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")
