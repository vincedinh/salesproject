import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# Using the requests module, we use the "get" function
# provided to access the webpage provided as an
# argument to this function:
#result = requests.get("https://www.gap.com/browse/category.do?cid=65289&nav=meganav%3ASale%3AShop%20Sale%3AMen")

# using selenium to get correct dump
driver = webdriver.Chrome(executable_path=r'C:\Users\Vince\Documents\GitHub\salesproject\chromedriver.exe')
url = "https://www.gap.com/browse/category.do?cid=65289&nav=meganav%3ASale%3AShop%20Sale%3AMen"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
#print(soup.prettify())


# Check for 200 OK response
#print(result.status_code)
#print(result.text)

#print(result.headers)
#soup = BeautifulSoup(result, 'lxml')
#print(soup.prettify())

allItems = soup.find_all("div", {"class" : "faceted-grid"})
print(allItems)
#innerItems = allItems.find_all("div", {"class" : "product-card"})
#cards = soup.find_all("img")
#print(innerItems)
#print("\n")

# Checks for text with "img alt="
#tag = soup.find_all('')
#for item in allItems:
    #if "$" in item.text:
        #print(tag)
        #print(link.attrs['href'])
