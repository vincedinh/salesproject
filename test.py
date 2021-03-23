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
#print(soup.prettify())


body = soup.body
content = body.find('div', class_="product-grid__items")

def retrieve_product_info(soup_object):
    name = product.find('div', class_='product-card__title').string
    link = product.find('a', class_='product-card__img-link-overlay')['href']
    current_price = product.find('div', class_='is--current-price').string
    past_price = product.find('div', class_='is--striked-out').string
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


#print(len(content.contents))
