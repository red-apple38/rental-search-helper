import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc
from getuseragent import UserAgent

GOOGLE_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLSc5Hqs5nTL4s1pGYfGyiLNwOb_nQlyR5Gcd-cJETEXRLCCSww/viewform"
URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A37.78329010579611%2C%22east%22%3A-122.40174094892636%2C%22south%22%3A37.704423943193675%2C%22west%22%3A-122.55709449506894%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A567889%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%7D"
# #chrome_driver_path = "D:\Programme (x86)\chrome_driver.exe"
# if __name__ == "__main__":
#     driver = uc.Chrome()
#     driver.get(URL)
#     time.sleep(5)
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(5)
#     immobilien = driver.find_elements(By.CSS_SELECTOR, 'span[data-test="property-card-price"]' )
#     print(len(immobilien))
#
#
#     driver.quit()


useragent = UserAgent()

theuseragent = useragent.Random()
print(theuseragent)

hdr = {'User-Agent': theuseragent,
      # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      # 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      # 'Accept-Encoding': 'none',
      # 'Accept-Language': 'en-US,en;q=0.8',
      # 'Connection': 'keep-alive'
       }






response = requests.get(URL, headers=hdr)
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

css_klasse = "ListItem-c11n-8-84-3__sc-10e22w8-0"
all_link_elements = soup.select(f".{css_klasse} a")
print(css_klasse)

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

prices = soup.select(".ListItem-c11n-8-73-8__sc-10e22w8-0 .hRqIYX span")
all_price =[]
for price in prices:
      all_price.append(price.text)
print(all_price)
print(len(all_price))

adresses = soup.select(".ListItem-c11n-8-73-8__sc-10e22w8-0 a address")
all_address = []

for address in adresses:
      all_address.append(address.text)
print(len(all_address))
print(all_address)

min_len = min(len(all_address), len(all_price), len(all_links))



for i in range(min_len):

      if __name__ == "__main__":
            driver = uc.Chrome()
            driver.get(GOOGLE_FORMS)
            time.sleep(7)
            input_tags = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')

            print(len(input_tags))
            time.sleep(1)
            input_tags[0].send_keys(all_address[i])
            time.sleep(2)
            input_tags[1].send_keys(all_price[i])
            time.sleep(2)
            input_tags[2].send_keys(all_links[i])
            time.sleep(2)
            send_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            send_form.click()
            time.sleep(5)
            driver.quit()
            time.sleep(1)
      else:
            print('name not main')