import requests
import os
import json
from enum import Enum

# api
api_key = os.environ.get("RIOT_API_KEY")
headers = {"X-Riot-Token": api_key, "User-Agent": "sebis-api-wrapper"}

Available_tiers = Enum(
    "Available_tiers", "challenger grandmaster master diamond platin gold silver bronze iron")


def get_puuid_by_summoner_name(name):
    url = "https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{0}".format(
        name)
    r = requests.get(url, headers=headers)
    return r.json()["puuid"]


def get_matches_by_puuid(puuid, number_of_matches=100):
    url = "https://europe.api.riotgames.com/tft/match/v1/matches/by-puuid/{0}/ids?count={1}".format(
        puuid, number_of_matches)
    r = requests.get(url, headers=headers)
    return r.json()


def get_matches_by_summoner_name(name, number_of_matches=100):
    puuid = get_puuid_by_summoner_name(name)
    return get_matches_by_puuid(puuid, number_of_matches)


def get_match_details(game_id):
    url = "https://europe.api.riotgames.com/tft/match/v1/matches/{0}".format(
        game_id)
    r = requests.get(url, headers=headers)
    return r.json()


def get_all_summoners_in_league(tier, division="empty"):
    # challanger, grandmaster and master have no divisions
    if division != "empty":
        raise NotImplementedError("division not implemented yet")
    url = "https://euw1.api.riotgames.com/tft/league/v1/{0}".format(tier)
    r = requests.get(url, headers=headers)
    return r.json()["entries"]


def get_all_summoner_names_in_league(tier, division="empty"):
    challangers = (get_all_summoners_in_league(tier, division))
    return list(map(lambda x: x["summonerName"], challangers))
