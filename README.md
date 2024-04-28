# API-Endpoint-Health-Check

This repository contains a Python script for **checking the health of an API endpoint** and sending **email notifications** if the health check fails.

## Functionality

The script uses the **Requests library** to send HTTP GET requests to the specified API endpoint. It sets a **timeout** for the request to ensure timely responses. If the endpoint returns a **non-successful status code** or if there's a **connection error**, the script sends an **email notification** using the **SMTP protocol**.

- **Requests Library**: Simplifies sending HTTP requests in Python. Allows the script to easily interact with the API endpoint, handle responses, and set timeouts for requests.

- **SMTP (Simple Mail Transfer Protocol)**: Used for sending email notifications. The script connects to an SMTP server using the provided credentials and sends an email with details about the health check status if an issue is detected with the API endpoint.

## Additional Information

- **Third-Party Login**: Make sure to enable third-party app login in your Google account, which you are using to send emails.
- You can refer to [this article](https://www.geeksforgeeks.org/enabling-third-party-app-login-using-google-account/) written by me on GeeksforGeeks.
