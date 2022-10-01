from typing import List
from typing import Any
from dataclasses import dataclass
from .Companion import Companion
from .Trait import Trait
from .Unit import Unit

@dataclass
class Participant:
    participant_id: str
    augments: List[str]
    companion: Companion
    gold_left: int
    last_round: int
    level: int
    partner_group_id: int
    placement: int
    players_eliminated: int
    puuid: str
    time_eliminated: float
    total_damage_to_players: int
    traits: List[Trait]
    units: List[Unit]

    @staticmethod
    def from_dict(obj: Any, participant_id: str) -> 'Participant':
        _participant_id = str(participant_id)
        _augments = obj.get("augments")
        _companion = Companion.from_dict(obj.get("companion"))
        _gold_left = int(obj.get("gold_left"))
        _last_round = int(obj.get("last_round"))
        _level = int(obj.get("level"))
        _partner_group_id = int(obj.get("partner_group_id"))
        _placement = int(obj.get("placement"))
        _players_eliminated = int(obj.get("players_eliminated"))
        _puuid = str(obj.get("puuid"))
        _time_eliminated = float(obj.get("time_eliminated"))
        _total_damage_to_players = int(obj.get("total_damage_to_players"))
        _traits = [Trait.from_dict(y) for y in obj.get("traits")]
        _units = [Unit.from_dict(y) for y in obj.get("units")]
        return Participant(_participant_id, _augments, _companion, _gold_left, _last_round, _level, _partner_group_id, _placement, _players_eliminated, _puuid, _time_eliminated, _total_damage_to_players, _traits, _units)

