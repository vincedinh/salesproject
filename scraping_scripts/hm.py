import requests
#from bs4 import BeautifulSoup
#from selenium import webdriver

"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://duckgo.com"
driver.get(start_url)
print(driver.page_source.encode("utf-8"))
driver.quit()
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--lang=en_US')
#driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options) --ying's pc
driver = webdriver.Chrome(executable_path=r'C:\Users\Vince\Documents\GitHub\salesproject\chromedriver.exe')
#url = "https://www.gap.com/browse/category.do?cid=65289&nav=meganav%3ASale%3AShop%20Sale%3AMen&ak_t=80597F6050F6CEB9FFBDDFFB91DBA2B517C532EEEA61000020804560A4BB1155"
#url = "https://www.nike.com/w/sale-3yaep"
url = 'https://www2.hm.com/en_us/sale/men/view-all.html'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

#print(soup.prettify())
#open('output.txt', soup.prettify(), encoding='utf-8') 

#menu = soup.find_all("div", {"class" : "page-content"})
#print(allItems)
#parsys = menu.find_all("div", {"class" : "main parsys"})
#section = parsys.find_all("div", {"class" : "section"})
#product_listing = section.find_all("ul", {"class" : "products-listing small"})
#items = soup.find_all("li", {"class" : "product-item"})
#tag = soup.find_all('a')[3]
#print(tag.string)

#print(items)

body = soup.body
content = body.find('ul', class_="products-listing small")

def retrieve_product_info(soup_object):
    name = product.find('a', class_='link').string
    link = "hm.com" + product.find('a', class_='link')['href']
    current_price = product.find('span', class_='price sale').string
    past_price = product.find('span', class_='price regular').string
    return [name, link, current_price, past_price]

for product in content:
    try:
        info_list = retrieve_product_info(product)
        print("Name: " + info_list[0])
        print("Link: " + info_list[1])
        print("Current Price: " + info_list[2])
        print("Past Price: " + info_list[3])
        print()
    except Exception as e:
        pass