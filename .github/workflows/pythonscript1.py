import requests
import re
import json

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
    lastversion = ""
    pattern = r'\b\d{1,3}\.\d{1,3}(?:\.\d{1,3})?\b$'
    # Check each element in the list against the pattern
    matches = [element for element in versions if re.match(pattern, element)]
#    print(matches)
    if len(matches)> 0:
        lastversion = matches[0]
    return lastversion

def getProductLastVersionrule1(product):
    lastProductVersion = None
    data={"name":product,"lastversion":""}
    api_url = "https://hub.docker.com/v2/repositories/"+product+"/tags/"
    versions = None
    try:
        versions = get_versions(api_url)
        if not versions:
            print("Failed to fetch versions.")
            return None
    except:
        print("Failed to fetch versions.")
        return None

    lastProductVersion = getlastJiarVarsion(versions)
    data = {"product":product,"lastVersion": lastProductVersion}
    print( product +" last version is " + getlastJiarVarsion(versions))
    return data
# Example usage
if __name__ == "__main__":
    json_array = []
    json_array.append(getProductLastVersionrule1("atlassian/jira-software"))
    json_array.append(getProductLastVersionrule1("atlassian/bitbucket"))
    json_array.append(getProductLastVersionrule1("atlassian/confluence"))
    json_array.append(getProductLastVersionrule1("jenkins/jenkins"))
    json_array.append(getProductLastVersionrule1("library/nginx"))
    #    json_array.append(getProductLastVersionrule1("library/sonarqube"))

    # Convert the list to a JSON array
    json_string = json.dumps(json_array)

    # Write the JSON array to a file
    with open("output.json", "w") as json_file:
        json_file.write(json_string)


