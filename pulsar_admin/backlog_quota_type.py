from enum import Enum


class BacklogQuotaType(Enum):
    destination_storage = "destination_storage"
    message_age = "message_age"
