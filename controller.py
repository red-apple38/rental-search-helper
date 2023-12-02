from webbot import WebBot
from soup import Soup
from google_tabelle import Daten

class Controller:
    def __init__(self):
        self.web_bot = WebBot()
        self.soup = Soup()
        self.sheet_as_list = Daten().set_miet_daten()








controller = Controller()
