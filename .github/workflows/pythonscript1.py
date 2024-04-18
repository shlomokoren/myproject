import requests
import re

def get_versions(api_url):
    versions = []
    page = 1
    per_page = 100  # Adjust this value based on your needs

    try:
        while True:
            params = {"page": page, "page_size": per_page}
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()  # Parse response as JSON
            results = data["results"]
            if not results:  # Stop if no more results are returned
                break
            versions.extend(tag["name"] for tag in results)
            if page < 2:
                page += 1
            else:
                break
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

    return versions

def getlastJiarVarsion(versions):

    # Define your regex pattern
    pattern = r'\b\d{1,3}\.\d{1,3}(?:\.\d{1,3})?\b$'

    # Example list


    # Check each element in the list against the pattern
    matches = [element for element in versions if re.match(pattern, element)]
#    print(matches)
    lastversion = matches[0]
#    matches = [element for element in versions if re.match(pattern, element)]
#    print(matches)

    return lastversion
def getProductLastVersionrule1(product):
    lastProductVersion = ""
    api_url = "https://hub.docker.com/v2/repositories/"+product+"/tags/"
    versions = get_versions(api_url)
    if not versions:
        print("Failed to fetch versions.")
        return lastProductVersion
    lastProductVersion = getlastJiarVarsion(versions)
    print( product +" last version is " + getlastJiarVarsion(versions))
    return lastProductVersion
# Example usage
if __name__ == "__main__":
    product = "atlassian/jira-software"
    getProductLastVersionrule1(product)

    product = "jenkins/jenkins"
    getProductLastVersionrule1(product)