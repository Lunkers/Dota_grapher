import json
import requests
import pandas
import matplotlib.pyplot as plt
#from bs4 import BeautifulSoup
import matplotlib
import Dota_data

matplotlib.style.use('ggplot')

class Player:

    def __init__(self, playerID, playerName =""):
        self.playerID = playerID
        self.heroData = self.get_heroes_data()
        self.playerName = playerName
        self.playerData = self.get_player_match_data()

    def get_heroes_data(self):
        url = "https://api.opendota.com/api/players/"+ self.playerID + "/heroes"
        header = {'x-requested with': "XMLHttpRequest"}
        df = pandas.read_json(url)
        for key in Dota_data.heroes_dict:
            df = df.replace(to_replace={"hero_id":{key:Dota_data.heroes_dict[key]}})

        return df

    def calculate_wr(self):
        self.heroData["Winrate"] = self.heroData.win / self.heroData.games


    def graph_heroes_wins(self):
        self.heroData.plot.bar(x="hero_id", y=["win","games"], color=["cyan", "magenta"], title=self.playerName + "'s awful hero stats")
        plt.show()

    def graph_winrate(self):
        self.calculate_wr()
        self.heroData.plot.bar(x="hero_id", y="Winrate", color=["Yellow"])
        plt.show()

    def get_player_match_data(self):
        url = "https://api.opendota.com/api/players/" + self.playerID + "/matches"
        header = {'x-requested with': "XMLHttpRequest"}
        df = pandas.read_json(url)
        for key in Dota_data.heroes_dict:
            df = df.replace(to_replace={"hero_id": {key: Dota_data.heroes_dict[key]}})

        return df

lunkers = Player("83675587")
print(lunkers.playerData)