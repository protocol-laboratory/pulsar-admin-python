from dataclasses import dataclass, field
from typing import Set


@dataclass
class TenantInfo:
    admin_roles: Set[str] = field(default_factory=set)
    allowed_clusters: Set[str] = field(default_factory=set)

    def to_json(self):
        return {
            "adminRoles": list(self.admin_roles),
            "allowedClusters": list(self.allowed_clusters),
        }
