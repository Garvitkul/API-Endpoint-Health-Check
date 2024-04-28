import requests
import smtplib

"""
You can add your API key if your API endpoint requires the key for authentication.
Technically API key is not required to just check the health of the API endpoint.
Api key variable can be left blank as this will send the blank header which will not affect the health monitoring.
"""
api_endpoint_url = "https://catfact.ninja/fact"
timeout = 2
api_key = ""

#You need to replace values of four below variables.
sender_email = "your_sender_email@example.com"
receiver_email = "your_receiver_email@example.com"
smtp_username = "your_smtp_username"
smtp_password = "your_smtp_password"

smtp_server = "smtp.example.com"
smtp_port = 587

def check_health():
    try:
        headers = {"x-api-key": api_key}
        response = requests.get(api_endpoint_url, headers=headers, timeout=timeout)
        if response.status_code == 200:
            print("Endpoint is healthy.")
        else:
            send_email("API Health Check Failed", f"Endpoint returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        send_email("API Health Check Failed", f"Failed to connect to endpoint {api_endpoint_url}. Error: {str(e)}")

def send_email(subject, body):
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message)

check_health()
