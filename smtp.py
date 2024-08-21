import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file for secuirty concerns
load_dotenv()

from_addr = os.getenv("EMAIL_ADDRESS")
to_addrs = os.getenv("EMAIL_RECIPIENT")
email_password = os.getenv("EMAIL_PASSWORD")

def email_logic(mail):
    # Prepare the message
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = to_addrs
    msg["Subject"] = "News of Today"

    # Auto-generate the message content
    message_lines = mail
    msg.set_content("\n".join(message_lines))

    print("Message length is", len(msg.as_string()))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Start TLS encryption
        # Use environment variables or another secure way to store your credentials
        server.login(from_addr, email_password)  # Gmail authentication
        server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")
    finally:
        server.quit()