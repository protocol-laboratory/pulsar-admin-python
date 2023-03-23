from enum import Enum


class RetentionPolicy(Enum):
    producer_request_hold = "producer_request_hold"
    producer_exception = "producer_exception"
    consumer_backlog_eviction = "consumer_backlog_eviction"
