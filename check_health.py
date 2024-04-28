import requests

api_endpoint_url = "https://catfact.ninja/fact" #Change it to your API endpoint.
timeout = 5

#You can add your API key if your API endpoint requires the key for authentication.
#Technically API key is not required to just check the health of the API endpoint.
#Api key variable can be left blank as this will send the blank header which will not affect the health monitoring.
api_key = "" 

def check_health():
    try:
        headers = {"x-api-key": api_key}
        response = requests.get(api_endpoint_url, headers=headers, timeout=timeout)
        if response.status_code == 200:
            print("Endpoint is healthy.")
        else:
            print(f"Endpoint returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to endpoint {api_endpoint_url}. Error: {str(e)}")

check_health()
