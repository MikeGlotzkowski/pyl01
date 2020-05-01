from functools import reduce
import json
import riot_api
import database as db

connection = db.get_connection()
collection = db.get_connection_to_collection(connection, riot_api.Available_tiers.master.name)
number_of_matches_per_player = 200

all_summoner_names = riot_api.get_all_summoner_names_in_league(
    riot_api.Available_tiers.master.name)
for summoner_index, summoner_name in enumerate(all_summoner_names):
    matches_for_summoner = riot_api.get_matches_by_summoner_name(
        summoner_name, number_of_matches_per_player)
    for match_index, match in enumerate(matches_for_summoner):
        try:
            match_details = riot_api.get_match_details(match)
        except Exception as e:
            print("error getting data from API:", str(e))
            pass
        try:
            db.insert_to_collection_if_not_exists(
                collection, match_details, True)
        except Exception as e:
            print("error writing data to db:", str(e))
            pass
        print("match {0}/{1} matches of summoner {2}/{3} summoners.".format(
            (match_index+1), len(matches_for_summoner), (summoner_index+1), len(all_summoner_names)))