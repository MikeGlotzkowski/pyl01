from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Trait:
    name: str
    num_units: int
    style: int
    tier_current: int
    tier_total: int

    @staticmethod
    def from_dict(obj: Any) -> 'Trait':
        _name = str(obj.get("name"))
        _num_units = int(obj.get("num_units"))
        _style = int(obj.get("style"))
        _tier_current = int(obj.get("tier_current"))
        _tier_total = int(obj.get("tier_total"))
        return Trait(_name, _num_units, _style, _tier_current, _tier_total)