import os
import smtplib 
from email.message import EmailMessage

EMAIL_CLIENT = os.environ.get('EMAIL_CLIENT')
EMAIL_CLIENT_APP_PASSWORD = os.environ.get('EMAIL_CLIENT_APP_PASSWORD')

def email_alert(subject, to, body):
    message = EmailMessage()
    message['subject'] = subject
    message['to'] = to
    message['from'] = EMAIL_CLIENT
    message.set_content(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_CLIENT, EMAIL_CLIENT_APP_PASSWORD)
    server.send_message(message)
    server.quit()

if __name__ == '__main__':
    email_alert("this is my subject", "recipient@email.com", "this is my body")
