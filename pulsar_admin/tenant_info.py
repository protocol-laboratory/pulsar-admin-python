import json
from dataclasses import dataclass, field
from typing import Set


@dataclass
class TenantInfo:
    admin_roles: Set[str] = field(default_factory=set)
    allowed_clusters: Set[str] = field(default_factory=set)

    def to_json(self):
        return json.dumps(self.__dict__)
