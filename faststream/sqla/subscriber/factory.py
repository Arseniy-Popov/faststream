from typing import Any

from faststream._internal.endpoint.subscriber.call_item import CallsCollection
from faststream._internal.endpoint.subscriber.specification import SubscriberSpecification
from faststream.sqla.configs.broker import SqlaBrokerConfig
from faststream.sqla.configs.subscriber import SqlaSubscriberConfig
from faststream.sqla.retry import RetryStrategy
from faststream.sqla.subscriber.specification import SqlaSubscriberSpecification
from faststream.sqla.subscriber.usecase import SqlaSubscriber


def create_subscriber(
    queue: str,
    max_workers: int,
    retry_strategy: RetryStrategy,
    fetch_interval: float,
    fetch_batch_size: int,
    overfetch_factor: float,
    flush_interval: float,
    release_stuck_interval: float,
) -> Any:
    subscriber_config = SqlaSubscriberConfig(
        queue=queue,
        max_workers=max_workers,
        retry_strategy=retry_strategy,
        fetch_interval=fetch_interval,
        fetch_batch_size=fetch_batch_size,
        overfetch_factor=overfetch_factor,
        flush_interval=flush_interval,
        release_stuck_interval=release_stuck_interval,
    )

    calls = CallsCollection[Any]()

    specification = SqlaSubscriberSpecification()

    return SqlaSubscriber(subscriber_config, specification, calls)