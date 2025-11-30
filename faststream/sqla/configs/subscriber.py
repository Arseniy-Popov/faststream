from dataclasses import dataclass, field
from faststream._internal.configs.endpoint import SubscriberUsecaseConfig
from faststream.middlewares.acknowledgement.config import AckPolicy
from faststream.sqla.configs.broker import SqlaBrokerConfig
from faststream.sqla.retry import RetryStrategy


@dataclass(kw_only=True)
class SqlaSubscriberConfig(SubscriberUsecaseConfig):
    _outer_config: "SqlaBrokerConfig" = field(default_factory=SqlaBrokerConfig)

    queue: str
    max_workers: int
    retry_strategy: RetryStrategy
    fetch_interval: float
    fetch_batch_size: int
    overfetch_factor: float
    flush_interval: float
    release_stuck_interval: float

    @property
    def ack_policy(self) -> AckPolicy:
        return AckPolicy.NACK_ON_ERROR