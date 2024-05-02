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

def getlastVersion(versions):
    lastversion = ""
    pattern = r'\b\d{1,3}\.\d{1,3}(?:\.\d{1,3})?\b$'
    # Check each element in the list against the pattern
    matches = [element for element in versions if re.match(pattern, element)]
#    print(matches)
    if len(matches)> 0:
        sorted_versions = sorted(matches, key=lambda x: tuple(map(int, x.split('.'))))
        lastversion = sorted_versions[-1]
 #       lastversion = matches[0]
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

    lastProductVersion = getlastVersion(versions)
    data = {"product":product,"lastVersion": lastProductVersion}
    print(product +" last version is " + lastProductVersion)
    return data

def json_to_html_table(json_str):
    try:
        data = json.loads(json_str)
        if not isinstance(data, list):
            raise ValueError("Input JSON must be a list")

        html = "<table border='1' style='text-align:left; border-collapse: collapse;'>\n"  # Added border-collapse for better borders
        html += "<tr style='background-color:#f2f2f2;'><th style='background-color:#ddd;'>Product Name</th><th style='background-color:#ddd;'>Product Last Version</th></tr>\n"  # Header row with background color

        # Alternate row colors for better readability
        for i, entry in enumerate(data):
            product = entry.get("product", "")
            last_version = entry.get("lastVersion", "")
            bgcolor = "#ffffff" if i % 2 == 0 else "#f2f2f2"
            html += f"<tr style='background-color:{bgcolor};'><td>{product}</td><td>{last_version}</td></tr>\n"

        html += "</table>"
        return html
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except Exception as e:
        print("An error occurred:", e)


# start
if __name__ == "__main__":
    json_array = []
    json_array.append(getProductLastVersionrule1("atlassian/jira-software"))
    json_array.append(getProductLastVersionrule1("atlassian/jira-servicemanagement"))
    json_array.append(getProductLastVersionrule1("atlassian/bitbucket"))
    json_array.append(getProductLastVersionrule1("atlassian/confluence"))
    json_array.append(getProductLastVersionrule1("jenkins/jenkins"))
    json_array.append(getProductLastVersionrule1("library/nginx"))
    #    json_array.append(getProductLastVersionrule1("library/sonarqube"))

    # Convert the list to a JSON array
    json_string = json.dumps(json_array)

    # Write the JSON array to a file
    with open("products_versions.json", "w") as json_file:
         result = json_file.write(json_string)

    # Convert JSON to HTML table
    html_table = json_to_html_table(json_string)

    # Write HTML table to a file
    with open("products_versions.html", "w") as f:
        f.write(html_table)
        print("HTML table has been written to output.html")



