from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
import requests
from fake_useragent import UserAgent
from logs import writelogs


class WebBot:
    ua = UserAgent(browsers=['edge', 'chrome'])

    def __init__(self):
        self.URL = "https://www.immobilienscout24.de/"
        self.driver = uc.Chrome()  # headless Fehler
        self.element = None
        self.html_content = None
        self.user_agent = self.ua.random

    def start(self):
        self.driver.get(self.URL)

    def set_element(self, dom_suchkriterium, element_locator, timeout=10.):
        self.element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((dom_suchkriterium, element_locator))
        )

    def set_element_in_shadow_root(self, sdom_suchkriterium, sdom_element_locator, dom_suchkriterium, element_locator,
                                   timeout=10):
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

    def selenium_html_content(self) -> str:  # decrapped: Höherer Speicherbedarf, alternative vllt. in Zukunft?
        self.html_content = self.driver.page_source
        return self.html_content

    def get_response(self, url) -> str:
        selenium_cookies = self.driver.get_cookies()
        requests_cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
        hdr = {'User-Agent': self.user_agent,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
               'Accept-Charset': 'utf-8',
               'Accept-Encoding': 'none',
               'Cookie': '; '.join([f'{key}={value}' for key, value in requests_cookies.items()]),
               'Connection': 'keep-alive'
               }

        try:
            response = requests.get(url, headers=hdr)  # self.driver.current_url
            response.raise_for_status()
            self.html_content = response.text
            return self.html_content

        except requests.exceptions.RequestException as e:
            writelogs(e)
            self.html_content = None # etwas ist schiefgelaufen


# Implementierung als statische methode? später vllt...
    def start_webbot(self): # driver Error falls Chrome updated abfangen Log message --- Funktion zerschlagen!
        self.start()
        try: # Zeitaufwändig bei wiederholung ? control behavior

            self.set_element_in_shadow_root(sdom_suchkriterium="css selector",
                                               sdom_element_locator='[id="usercentrics-root"]',
                                               dom_suchkriterium="css selector",
                                               element_locator='button[data-testid="uc-customize-button"]')
            self.click()
            self.set_element_in_shadow_root(sdom_suchkriterium="css selector",
                                               sdom_element_locator='[id="usercentrics-root"]',
                                               dom_suchkriterium="css selector",
                                               element_locator='button[data-testid="uc-deny-all-button"]')
            self.click()

        except TimeoutError as t:
            raise t

        finally:
            self.set_element(dom_suchkriterium="id", element_locator="oss-location", )
            self.clear_and_send_keys(text="Gießen")
            time.sleep(0.5)
            self.element.send_keys(Keys.ENTER)
            time.sleep(0.5)
            self.element.send_keys(Keys.ENTER)
            # nicht sleep url muss stimmen -> später Abfrage nach Integration von sheets
            time.sleep(3)

            # Todo Feature will be delayed
            # Design update Immo:
            # bot.set_element(dom_suchkriterium="id", element_locator="oss-price")
            # bot.clear_and_send_keys("800")
            # bot.set_element(dom_suchkriterium="id", element_locator="oss-radius"
            # bot.select_field_by_value("Km5")
            # bot.set_element(dom_suchkriterium="id", element_locator="oss-rooms")
            # bot.select_field_by_value("2")

            self.get_response(url=self.driver.current_url)
            self.driver.quit()




