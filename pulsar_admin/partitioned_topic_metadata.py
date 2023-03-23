from typing import Dict
from dataclasses import dataclass


@dataclass
class PartitionedTopicMetadata:
    partitions: int
    deleted: bool
    properties: Dict[str, str] = None
