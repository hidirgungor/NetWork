import requests
from bs4 import BeautifulSoup

# Define the domain to scan
domain = "example.com"

# Make a request to the domain
r = requests.get("http://" + domain)

# Parse the HTML of the page
soup = BeautifulSoup(r.content, "html.parser")

# Find all links on the page
links = soup.find_all("a")

# Iterate through the links
for link in links:
    # Check if the link is a subdomain
    if domain in link["href"]:
        # Print the subdomain
        print(link["href"])
