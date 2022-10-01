from typing import List
from typing import Any
from dataclasses import dataclass   

@dataclass
class Companion:
    content_ID: str
    item_ID: int
    skin_ID: int
    species: str

    @staticmethod
    def from_dict(obj: Any) -> 'Companion':
        _content_ID = str(obj.get("content_ID"))
        _item_ID = int(obj.get("item_ID"))
        _skin_ID = int(obj.get("skin_ID"))
        _species = str(obj.get("species"))
        return Companion(_content_ID, _item_ID, _skin_ID, _species)
