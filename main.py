import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time


def get_response(api_url):
    response = requests.get(api_url)
    return response.text


def perform_action(response, api_name):
    if response:
        json_data = json.loads(response)
        if 'response' in json_data and json_data['response']:
            response_value = float(json_data['response'])
            if response_value < 100:
                send_email(api_name, response_value)
        else:
            print(f"Response from {api_name} is empty or does not contain 'response' key.")
    else:
        print(f"No response received from {api_name}.")


def send_email(api_name, response_value):
    sender_email = ''
    receiver_email = ''
    smtp_server = ''
    smtp_port = 465
    smtp_username = ''
    smtp_password = ''

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f'Alert 🔴 : {api_name} balance Less Than 100'

    body = (f"Hello Saki\n"
            f"\n"
            f"Your {api_name} operator current balance is: {response_value} TK \n"
            f"Please arrange a payment asap.\n"
            f"\n"
            f"Thank you!")
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def main():
    apis = {
        'api_name': "https://api....",
    
    }

    for api_name, api_url in apis.items():
        response = get_response(api_url)
        perform_action(response, api_name)


if __name__ == "__main__":
    schedule.every(1).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
