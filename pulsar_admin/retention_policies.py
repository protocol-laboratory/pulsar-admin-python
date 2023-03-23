from dataclasses import dataclass


@dataclass
class RetentionPolicies:
    retention_time_in_minutes: int
    retention_size_in_mb: int
