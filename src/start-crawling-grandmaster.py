from match_runner import MatchRunner
import riot_api
import database as db

connection = db.get_connection()
collection = db.get_connection_to_collection(
    connection, riot_api.Available_tiers.grandmaster.name)
number_of_matches_per_player = 200

riot_api.init_logger()
mr = MatchRunner(collection, riot_api.Available_tiers.grandmaster.name,
                 number_of_matches_per_player)
mr.init_logger()
mr.run()
