import requests

def get_data(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()  # Parse response as JSON and return
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    api_url = "https://hub.docker.com/v2/repositories/library/mariadb/tags"  # Example API endpoint
    data = get_data(api_url)
    if data:
        print("Data received:")
        print(data)
    else:
        print("Failed to fetch data.")

