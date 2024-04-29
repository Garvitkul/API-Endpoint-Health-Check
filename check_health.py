import requests
import boto3

api_endpoint_url = "https://catfact.ninja/facts" #Replace your API endpoint
timeout = 2


def lambda_handler(event, context):
    sns_client = boto3.client('sns', region_name="ap-south-1")
    try:
        response = requests.get(api_endpoint_url, timeout=timeout)
        if response.status_code == 200:
            message = "Endpoint is healthy."
            print(message)
            sns_client.publish(TopicArn="arn:aws:sns:ap-south-1:146366115606:api-health-check", Subject="API Health Check", Message=message)
        else:
            message = f"Endpoint returned status code {response.status_code}"
            print(message)
            sns_client.publish(TopicArn="arn:aws:sns:ap-south-1:146366115606:api-health-check", Subject="API Health Check", Message=message)            
    except requests.exceptions.RequestException as e:
        message = f"Failed to connect to endpoint {api_endpoint_url}. Error: {str(e)}"
        print(message)
        sns_client.publish(TopicArn="arn:aws:sns:ap-south-1:146366115606:api-health-check", Subject="API Health Check", Message=message)
        
        
    
