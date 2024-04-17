import requests

def get_versions(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse response as JSON
        return [tag["name"] for tag in data["results"]]  # Extract version names
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    api_url = "https://hub.docker.com/v2/repositories/atlassian/jira-software/tags/"
    versions = get_versions(api_url)
    if versions:
        print("Versions:")
        for version in versions:
            print(version)
    else:
        print("Failed to fetch versions.")
