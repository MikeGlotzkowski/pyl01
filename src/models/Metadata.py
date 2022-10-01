from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Metadata:
    data_version: str
    match_id: str
    participants: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        _data_version = str(obj.get("data_version"))
        _match_id = str(obj.get("match_id"))
        _participants = obj.get("participants")
        return Metadata(_data_version, _match_id, _participants)
