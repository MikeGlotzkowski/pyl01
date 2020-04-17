import requests
import os
import json

# api
api_key = os.environ.get("RIOT_API_KEY")
headers = {"X-Riot-Token": api_key, "User-Agent": "sebis-api-wrapper"}

# general settings
number_of_matches = 100


def get_puuid_by_summoner_name(name):
    url = "https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{0}".format(
        name)
    r = requests.get(url, headers=headers)
    return r.json()["puuid"]


def get_matches_by_puuid(puuid, number_of_matches):
    url = "https://europe.api.riotgames.com/tft/match/v1/matches/by-puuid/{0}/ids?count={1}".format(
        puuid, number_of_matches)
    r = requests.get(url, headers=headers)
    return r.json()


def get_matches_by_summoner_name(name):
    puuid = get_puuid_by_summoner_name(name)
    return get_matches_by_puuid(puuid, number_of_matches)


def get_match_details(game_id):
    url = "https://europe.api.riotgames.com/tft/match/v1/matches/{0}".format(
        game_id)
    r = requests.get(url, headers=headers)
    return r.json()


matches = get_matches_by_summoner_name("KackZwerg")

match_numero_uno = get_match_details(matches[0])
testy = json.dumps(match_numero_uno)
print(match_numero_uno)
