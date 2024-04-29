# API Endpoint Health Check

This repository contains a Python script for **checking the health of an API endpoint** and sending **email notifications** if the health check fails. This is deployed on **AWS Lambda** and uses **AWS SNS client** of **Boto3 SDK**.

1. AWS Lambda Function **api-health-check** is created in ap-south-1 region. It is using python runtime.
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/399aedff-5d3b-47c4-9183-db6d868279c8)
2. AWS Lambda Layer **api-health-check** is created for the requests library of python.
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/4a8e241b-92a9-44ab-90df-a68854670058)
3. Code from check_health.py is copied to Lambda function.
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/2680185b-1d2b-4960-b62d-be4a4b814f21)
4. Create SNS topic named **api-health-check** and create a subscription of email address and verify it.
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/d740e67f-b531-494c-b83e-722ec09ced09)
5. Now, deploy the lambda function and **Test** it.
You can see the output based on the URL health and will get email as well.
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/8cd9ea99-63c1-4cf7-8f9f-95d83935b875)
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/94b553a7-1342-4c0e-becb-83811c22dc4a)
6. Here is the one with healthy API -
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/6fb28a7c-9f89-4b41-ae44-0793af2af040)
![image](https://github.com/Garvitkul/API-Endpoint-Health-Check/assets/83578615/2f73f748-37ec-4cb0-bc86-b2a70d270213)

## Functionality

The script uses the **Requests library** to send HTTP GET requests to the specified API endpoint. It sets a **timeout** for the request to ensure timely responses. 
- **Requests Library**: Simplifies sending HTTP requests in Python. Allows the script to easily interact with the API endpoint, handle responses, and set timeouts for requests.
