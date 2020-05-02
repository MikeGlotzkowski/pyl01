import database as db
import riot_api
import json
from functools import reduce
import logging
from datetime import datetime


class MatchRunner:

    def __init__(self, database_collection, tft_tier_name, number_of_matches_per_player):
        self.database_collection = database_collection
        self.tft_tier_name = tft_tier_name
        self.number_of_matches_per_player = number_of_matches_per_player

    def init_logger(*self):
        # create logger
        logger = logging.getLogger('MatchRunner_logger')
        logger.setLevel(logging.INFO)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        # 'application' code
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

        logging.info('Logger started...')

    def run(self):
        all_summoner_names = riot_api.get_all_summoner_names_in_league(
            self.tft_tier_name)
        for summoner_index, summoner_name in enumerate(all_summoner_names):
            matches_for_summoner = riot_api.get_matches_by_summoner_name(
                summoner_name, self.number_of_matches_per_player)
            for match_index, match in enumerate(matches_for_summoner):
                is_in_db_already = db.found_in_collection(
                    match, self.database_collection)
                if is_in_db_already:
                    print("match is in db already")
                    continue
                try:
                    match_details = riot_api.get_match_details(match)
                except Exception as e:
                    print("error getting data from API:", str(e))
                    pass
                try:
                    db.insert_to_collection_if_not_exists(
                        self.database_collection, match_details, True)
                except Exception as e:
                    print("error writing data to db:", str(e))
                    pass
                print("match {0}/{1} matches of summoner {2}/{3} summoners.".format(
                    (match_index+1), len(matches_for_summoner), (summoner_index+1), len(all_summoner_names)))
