from webbot import WebBot
from soup import Soup
from g_sheets import Daten


class Controller:
    def __init__(self):
        self.bot = WebBot()
        self.soup = Soup()

    def launch(self):
        self.bot.start_webbot()


controller = Controller()
