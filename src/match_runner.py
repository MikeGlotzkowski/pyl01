import database as db
import riot_api
import json
from functools import reduce
import logging
from datetime import datetime
import pathlib


class MatchRunner:

    def __init__(self, database_collection, tft_tier_name, number_of_matches_per_player):
        self.database_collection = database_collection
        self.tft_tier_name = tft_tier_name
        self.number_of_matches_per_player = number_of_matches_per_player
        self.init_logger()

    def init_logger(self):
        self.logger_name = "MatchRunner_logger"
        logger_level = logging.INFO
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        date_time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

        pathlib.Path('./logs/').mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        fh = logging.FileHandler(
            "./logs/{0}_{1}".format(date_time, self.logger_name))
        ch.setLevel(logger_level)
        fh.setLevel(logger_level)
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)
        
        logger.info('Logger started...')

    def run(self):
        logger = logging.getLogger(self.logger_name)

        logger.info('getting all summoner names in {0}.'.format(
            self.tft_tier_name))
        all_summoner_names = riot_api.get_all_summoner_names_in_league(
            self.tft_tier_name)
        for summoner_index, summoner_name in enumerate(all_summoner_names):
            matches_for_summoner = riot_api.get_matches_by_summoner_name(
                summoner_name, self.number_of_matches_per_player)
            for match_index, match in enumerate(matches_for_summoner):
                is_in_db_already = db.found_in_collection(
                    match, self.database_collection)
                if is_in_db_already:
                    logger.info(
                        "match {0} in db collection already.".format(match))
                    continue
                try:
                    match_details = riot_api.get_match_details(match)
                except Exception as e:
                    logger.critical(
                        "unhandled error getting data from API: {0}".format(str(e)))
                    pass
                try:
                    db.insert_to_collection_if_not_exists(
                        self.database_collection, match_details, True)
                except Exception as e:
                    logger.critical(
                        "error writing data to db: {0}".format(str(e)))
                    pass
                logger.info("match {0}/{1} matches of summoner {2}/{3} summoners.".format(
                    (match_index+1), len(matches_for_summoner), (summoner_index+1), len(all_summoner_names)))
