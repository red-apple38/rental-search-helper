from getuseragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import undetected_chromedriver as uc
import time



##Fake useragent wird in aktueller Version nicht benötigt

useragent = UserAgent()
theuseragent = useragent.Random()
hdr = {'User-Agent': theuseragent,
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'
}
class WebBot:
    def __init__(self):
        self.URL = "https://www.immobilienscout24.de/"
        self.driver = uc.Chrome()
        self.element = None
        self.html_content = None

    def start(self):
        self.driver.get(self.URL)

    def set_element(self, dom_suchkriterium, element_locator, timeout=10.):
        self.element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((dom_suchkriterium, element_locator))
        )

    def set_element_in_shadow_root(self,sdom_suchkriterium, sdom_element_locator, dom_suchkriterium, element_locator, timeout=10):
        s_element = self.driver.find_element(sdom_suchkriterium, sdom_element_locator).shadow_root
        wait = WebDriverWait(s_element, timeout)
        self.element = wait.until(EC.element_to_be_clickable((dom_suchkriterium, element_locator)))

    def clear_and_send_keys(self, text):
        self.element.clear()
        self.element.send_keys(text)
        time.sleep(1)

    def select_field_by_value(self, value):
        Select(self.element).select_by_value(value)
        time.sleep(1)

    def click(self):
        self.element.click()
        time.sleep(1)

    def set_and_get_html_content(self):
        self.html_content = self.driver.page_source
        return self.html_content
bot = WebBot()
bot.start()
time.sleep(3)
try:
    bot.set_element_in_shadow_root(sdom_suchkriterium="css selector", sdom_element_locator='[id="usercentrics-root"]',
                                   dom_suchkriterium="css selector", element_locator='button[data-testid="uc-customize-button"]')
    bot.click()
    bot.set_element_in_shadow_root(sdom_suchkriterium="css selector", sdom_element_locator='[id="usercentrics-root"]',
                                   dom_suchkriterium="css selector", element_locator='button[data-testid="uc-deny-all-button"]')
    bot.click()

except TimeoutError as t:
    raise t

finally:
    bot.set_element(dom_suchkriterium="id", element_locator="oss-location", )
    bot.clear_and_send_keys(text="Gießen")
    bot.set_element(dom_suchkriterium="id", element_locator="oss-price")
    bot.clear_and_send_keys("800")
    bot.set_element(dom_suchkriterium="id", element_locator="oss-radius")
    bot.select_field_by_value("Km5")
    bot.set_element(dom_suchkriterium="id", element_locator="oss-rooms")
    bot.select_field_by_value("2")
    bot.set_element(dom_suchkriterium="css selector", element_locator="button.oss-main-criterion.oss-button")
    bot.click()
    time.sleep(4)
    print(bot.set_and_get_html_content())
    time.sleep(1000)