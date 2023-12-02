import requests


# auth = "8yvmVcvZ0VsRWJkS75XS7EMN"
# headers = {
#     "Authorization": "Bearer 8yvmVcvZ0VsRWJkS75XS7EMN"
# }
#
# response = requests.get("https://api.sheety.co/9cd5c9e95a701eec3555d448104261d8/wohungssuche/tabellenblatt1", headers=headers).json()
#
# print(response)


# res = {'tabellenblatt1': [{'ort': 'Gießen', 'preis': 700, 'zimmer': 2, 'id': 2},
#                           {'ort': 'Marburg', 'preis': 650, 'zimmer': 2, 'id': 3},
#                           {'ort': 'Biedenkopf', 'preis': 800, 'zimmer': 4, 'id': 4}]}
#
# for key, value in res.items():
#     res = value
#
# print(res)


class Daten:

    def __init__(self):
        self.headers = {
            "Authorization": "Bearer 8yvmVcvZ0VsRWJkS75XS7EMN"}
        self.response = requests.get(
            "https://api.sheety.co/9cd5c9e95a701eec3555d448104261d8/wohungssuche/tabellenblatt1",
            headers=self.headers).json()

    def miet_daten(self):
        for key, value in self.response.items():
            self.response = value
        return self.response
