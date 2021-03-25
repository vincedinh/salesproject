from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

###CODE FOR SCRAPING USING SELENIUM###
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080000')
chrome_options.add_argument('--lang=en_US')
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
url = "https://www.nike.com/w/sale-3yaep"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()


###FINDING PRODUCTS ON THE WEBPAGE###
body = soup.body
content = body.find('div', class_="product-grid__items")

def retrieve_product_info(soup_object):
    product_dict = {}
    product_dict["name"] = product.find('div', class_='product-card__title').string
    product_dict["link"] = product.find('a', class_='product-card__img-link-overlay')['href']
    product_dict["current_price"] = product.find('div', class_='is--current-price').string
    product_dict["past_price"] = product.find('div', class_='is--striked-out').string
    return product_dict

for product in content:
    try:
        product_dict = retrieve_product_info(product)
        print("Name: " + product_dict["name"])
        print("Link: " + product_dict["link"])
        print("Current Price: " + product_dict["current_price"])
        print("Past Price: " + product_dict["past_price"])
        print()
    except Exception as e:
        pass


print(len(content.contents))
