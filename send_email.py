import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(smtp_server, smtp_port, from_email, password, to_email, subject, body):
    """
    Sends an email with the specified subject and body.

    Parameters:
    smtp_server (str): The SMTP server address.
    smtp_port (int): The SMTP server port.
    from_email (str): The sender's email address.
    password (str): The sender's email password.
    to_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body of the email.
    """
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS encryption
        server.login(from_email, password)  # Log in to the server
        server.send_message(msg)  # Send the email
