from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

start_time = time.time()

###CODE FOR SCRAPING USING SELENIUM###
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--lang=en_US')
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
url = "https://www.nike.com/w/sale-3yaep"
driver.get(url)

inner_height = driver.execute_script("return window.innerHeight")
scroll_height = driver.execute_script("return window.scrollY")
offsetHeight = driver.execute_script("return document.body.offsetHeight")

while not inner_height + scroll_height >= offsetHeight:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    inner_height = driver.execute_script("return window.innerHeight")
    scroll_height = driver.execute_script("return window.scrollY")
    offsetHeight = driver.execute_script("return document.body.offsetHeight")


#element.scrollHeight - element.scrollTop === element.clientHeight
#window.innerHeight + window.scrollY) >= document.body.offsetHeight

"""
print(driver.execute_script("return window.innerHeight"))
print(driver.execute_script("return window.scrollY"))
print(driver.execute_script("return document.body.offsetHeight"))

print()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

print(driver.execute_script("return window.innerHeight"))
print(driver.execute_script("return window.scrollY"))
print(driver.execute_script("return document.body.offsetHeight"))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

print(driver.execute_script("return window.innerHeight"))
print(driver.execute_script("return window.scrollY"))
print(driver.execute_script("return document.body.scrollHeight"))

print()

time.sleep(10)

print(driver.execute_script("return window.innerHeight"))
print(driver.execute_script("return window.scrollY"))
print(driver.execute_script("return document.body.offsetHeight"))
"""


"""
for i in range(100):
    height = driver.execute_script("return window.scrollY")
    driver.execute_script("window.scrollTo(0,document.body.offsetHeight)")

    #if driver.execute_script("if((window.innerHeight+window.scrollY)>=document.body.offsetHeight){return true;}"):
        #print("hello")
    print(i)
"""


soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
