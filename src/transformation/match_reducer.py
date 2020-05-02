
import json
import pathlib

import_data_file = "./import/one_example_match.json"
export_data_file = "./export/result.json"

with open(import_data_file) as json_file:
    data = json.load(json_file)
    transformed_data = {
        "match_id": data["metadata"]["match_id"],
        "game_datetime": data["info"]["game_datetime"],
        "game_length": data["info"]["game_length"],
        "participants": []
    }
    for participant in data["info"]["participants"]:
        transformed_data["participants"].append(
            {
                "puuid": participant["puuid"],
            }
        )
    with open(export_data_file, 'w') as outfile:
        json.dump(transformed_data, outfile)
