import json
import requests
import pandas
import matplotlib.pyplot as plt
#from bs4 import BeautifulSoup
import matplotlib
import Dota_data

matplotlib.style.use('ggplot')

player_id = input("Enter player ID: ")

def get_heroes_data(playerId):
    url = "https://api.opendota.com/api/players/"+ playerId+ "/heroes"
    header = {'x-requested with': "XMLHttpRequest"}
    data = requests.get(url, header)
    df = pandas.read_json(url)
    for key in Dota_data.heroes_dict:
        df = df.replace(to_replace={"hero_id":{key:Dota_data.heroes_dict[key]}})
    return df

heroes_meme = get_heroes_data(player_id)
print(heroes_meme)


def graph_heroes_wins(data):
    data.plot.bar(x="hero_id", y=["win","games"], color=["cyan", "magenta"])
    plt.show()

graph_heroes_wins(heroes_meme)

