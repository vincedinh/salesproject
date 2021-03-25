import requests
from bs4 import BeautifulSoup

# Using the requests module, we use the "get" function
# provided to access the webpage provided as an
# argument to this function:
result = requests.get("https://www.nordstrom.com/")

# Check for 200 OK response
print(result.status_code)

print(result.headers)
src = result.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
print(links)
print("\n")

# Checks for text with " off"
for link in links:
    if "off" in link.text:
        print(link)
        print(link.attrs['href'])
