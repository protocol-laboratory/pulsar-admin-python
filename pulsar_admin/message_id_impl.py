from dataclasses import dataclass


@dataclass
class MessageIdImpl:
    ledger_id: int
    entry_id: int
    partition_index: int
    batch_index: int = None

    def __str__(self):
        if self.batch_index is not None:
            return f"{self.ledger_id}:{self.entry_id}:{self.partition_index}:{self.batch_index}"
        return f"{self.ledger_id}:{self.entry_id}:{self.partition_index}"
