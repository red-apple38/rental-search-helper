import time
from webbot import WebBot
from soup import Soup
from g_sheets import Daten


class Controller:
    def __init__(self):
        self.bot = WebBot()
        self.soup = Soup()


    def launch(self):
        self.bot.start_webbot()
        #None check URL check
        self.soup.get_seitenanzahl()
        #param check

    def get_listings(self): #Inserate in Datenbank

        for i in range(2, self.soup.seitenanzahl):
            if self.bot.html_content is not None:
                self.soup.get_inserate(text=self.bot.html_content)
                self.bot.params["pagenumber"] = i
                self.bot.get_response()
                time.sleep(5.5-10) # server sollen nicht gespamt werden

            else:
                # POC no rotation
                # soft Maßnahmen
                break















            















