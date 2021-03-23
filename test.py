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
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--lang=en_US')
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
#url = "https://www.gap.com/browse/category.do?cid=65289&nav=meganav%3ASale%3AShop%20Sale%3AMen&ak_t=80597F6050F6CEB9FFBDDFFB91DBA2B517C532EEEA61000020804560A4BB1155"
url = "https://www.nike.com/w/sale-3yaep"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
print(soup.prettify())
