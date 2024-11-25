import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    # User inputs for SMTP server details
    smtp_server = input("Enter your SMTP server (e.g., smtp.gmail.com): ")
    smtp_port = int(input("Enter your SMTP port (e.g., 587 for TLS, 465 for SSL): "))
    from_email = input("Enter your email address: ")
    password = input("Enter your email password (or app-specific password if 2FA is enabled): ")

    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        if smtp_port == 465:  # For SSL
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:  # For TLS
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

        # Login to the server
        server.login(from_email, password)

        # Send email
        server.sendmail(from_email, to_email, message.as_string())
        print(f"Email successfully sent to {to_email}")

        # Close the connection
        server.quit()

    except Exception as e:
        print(f"Failed to send email: {e}")
