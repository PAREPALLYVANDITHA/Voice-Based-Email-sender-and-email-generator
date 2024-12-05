'''
string = "vanditha08102004 hyphen gmail.com"
if "at the rate" in string:
    substring = "at the rate"
elif "hyphen" in string:
    substring = "hyphen"
else:
    substing = "abc"
print(substring)
print(string.replace(substring,"@"))
'''
#attachments for mail

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(sender_email, receiver_email, password, subject, body, file_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return
    try:
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
            msg.attach(part)
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
if __name__ == "__main__":
    sender_email = "vanditha08102004@gmail.com"
    receiver_email = "22951a66g5@iare.ac.in"
    password = "qruvbqpylbhnzwke"
    subject = "Subject of the Email"
    body = "This is the body of the email, which might contain special characters: ñ, é, ü."
    file_path = r"C:\Users\parep\Downloads\IMG_20240926_162808.jpg"

    send_email_with_attachment(sender_email, receiver_email, password, subject, body, file_path)


