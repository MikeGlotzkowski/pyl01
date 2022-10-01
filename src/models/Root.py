from typing import Any
from dataclasses import dataclass
from .Metadata import Metadata
from .Info import Info

@dataclass
class Root:
    _id: str # key
    metadata: Metadata
    info: Info

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        __id = str(obj.get("_id"))
        _metadata = Metadata.from_dict(obj.get("metadata"))
        _info = Info.from_dict(obj.get("info"), _metadata)
        return Root(__id, _metadata, _info)
