from typing import List
from typing import Any
from dataclasses import dataclass
import uuid
from .Participant import Participant
from .Metadata import Metadata

@dataclass
class Info:
    _id: str # key
    game_datetime: float
    game_length: float
    game_version: str
    participants: List[Participant]
    queue_id: int
    tft_game_type: str
    tft_set_core_name: str
    tft_set_number: int

    @staticmethod
    def from_dict(obj: Any, _metadata: Metadata) -> 'Info':
        _id = str(uuid.uuid4()) 
        _game_datetime = float(obj.get("game_datetime"))
        _game_length = float(obj.get("game_length"))
        _game_version = str(obj.get("game_version"))
        _raw_participants = obj.get("participants")
        _participants = []
        for i, participant_id in enumerate(_metadata.participants):
            _participant = Participant.from_dict(_raw_participants[i], participant_id)
            _participants.append(_participant)

        _queue_id = int(obj.get("queue_id"))
        _tft_game_type = str(obj.get("tft_game_type"))
        _tft_set_core_name = str(obj.get("tft_set_core_name"))
        _tft_set_number = int(obj.get("tft_set_number"))
        return Info(_id, _game_datetime, _game_length, _game_version, _participants, _queue_id, _tft_game_type, _tft_set_core_name, _tft_set_number)
