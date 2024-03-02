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

    def get_listings(self):

        for i in range(1, self.soup.seitenanzahl):
            self.soup.get_inserate(text=self.bot.html_content)












            















