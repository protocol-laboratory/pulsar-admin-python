from dataclasses import dataclass

from pulsar_admin.retention_policy import RetentionPolicy


@dataclass
class BacklogQuota:
    limit_size: int
    limit_time: int
    policy: RetentionPolicy
