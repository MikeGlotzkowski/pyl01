import requests
import os
import json
from enum import Enum
from time import sleep

# api
api_key = os.environ.get("RIOT_API_KEY")
headers = {"X-Riot-Token": api_key, "User-Agent": "sebis-api-wrapper"}
seconds_to_wait_if_throttled = 120

Available_tiers = Enum(
    "Available_tiers", "challenger grandmaster master diamond platin gold silver bronze iron")


def get_puuid_by_summoner_name(name):
    url = "https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{0}".format(
        name)
    r = requests.get(url, headers=headers)
    ok = check_response(r)
    if not ok:
        return get_puuid_by_summoner_name(name)
    return r.json()["puuid"]


def get_matches_by_puuid(puuid, number_of_matches=100):
    url = "https://europe.api.riotgames.com/tft/match/v1/matches/by-puuid/{0}/ids?count={1}".format(
        puuid, number_of_matches)
    r = requests.get(url, headers=headers)
    ok = check_response(r)
    if not ok:
        return get_matches_by_puuid(puuid, number_of_matches)
    return r.json()


def get_matches_by_summoner_name(name, number_of_matches=100):
    puuid = get_puuid_by_summoner_name(name)
    return get_matches_by_puuid(puuid, number_of_matches)


def get_match_details(game_id):
    url = "https://europe.api.riotgames.com/tft/match/v1/matches/{0}".format(
        game_id)
    r = requests.get(url, headers=headers)
    ok = check_response(r)
    print(r)
    if not ok:
        return get_match_details(game_id)
    return r.json()


def get_all_summoners_in_league(tier, division="empty"):
    # challanger, grandmaster and master have no divisions
    if division != "empty":
        raise NotImplementedError("division not implemented yet")
    url = "https://euw1.api.riotgames.com/tft/league/v1/{0}".format(tier)
    r = requests.get(url, headers=headers)
    ok = check_response(r)
    if not ok:
        return get_all_summoners_in_league(tier, division)
    return r.json()["entries"]


def get_all_summoner_names_in_league(tier, division="empty"):
    challangers = (get_all_summoners_in_league(tier, division))
    return list(map(lambda x: x["summonerName"], challangers))


def check_response(resp):
    if resp.ok:
        return True
    elif resp.status_code == 429:
        wait(seconds_to_wait_if_throttled)
        return False
    else:
        resp.raise_for_status()


def wait(seconds_to_wait_if_throttled):
    print("throttled....now waiting for {0} seconds".format(
        seconds_to_wait_if_throttled))
    for x in range(0, seconds_to_wait_if_throttled):
        sleep(1)
        if x % 10 == 0:
            print("only {0} more seconds!".format(
                seconds_to_wait_if_throttled - x))
    print("ok let's go again!")
