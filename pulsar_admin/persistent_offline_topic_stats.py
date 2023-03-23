from typing import Dict, List
from dataclasses import dataclass


@dataclass
class PersistentOfflineTopicStats:
    storage_size: int
    total_messages: int
    message_backlog: int
    broker_name: str
    topic_name: str
    data_ledger_details: List["LedgerDetails"]
    cursor_details: Dict[str, "CursorDetails"]
    stat_generated_at: str

    @dataclass
    class CursorDetails:
        cursor_backlog: int
        cursor_ledger_id: int

    @dataclass
    class LedgerDetails:
        entries: int
        timestamp: int
        size: int
        ledger_id: int
