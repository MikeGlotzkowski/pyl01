from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Unit:
    character_id: str
    itemNames: List[str]
    items: List[int]
    name: str
    rarity: int
    tier: int

    @staticmethod
    def from_dict(obj: Any) -> 'Unit':
        _character_id = str(obj.get("character_id"))
        _itemNames = obj.get("itemNames")
        _items = obj.get("items")
        _name = str(obj.get("name"))
        _rarity = int(obj.get("rarity"))
        _tier = int(obj.get("tier"))
        return Unit(_character_id, _itemNames, _items, _name, _rarity, _tier)