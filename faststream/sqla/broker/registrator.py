from typing import Any
from faststream._internal.broker.registrator import Registrator
from faststream.sqla.subscriber.factory import create_subscriber
from faststream.sqla.retry import RetryStrategy


class SqlaRegistrator(Registrator[Any, Any]):
    def subscriber(
        self,
        queue: str,
        max_workers: int,
        retry_strategy: RetryStrategy,
        fetch_interval: float,
        fetch_batch_size: int,
        overfetch_factor: float,
        flush_interval: float,
        release_stuck_interval: float,
    ) -> Any:
        workers = max_workers or 1

        subscriber = create_subscriber(
            queue=queue,
            max_workers=max_workers,
            retry_strategy=retry_strategy,
            fetch_interval=fetch_interval,
            fetch_batch_size=fetch_batch_size,
            overfetch_factor=overfetch_factor,
            flush_interval=flush_interval,
            release_stuck_interval=release_stuck_interval,
        )

        super().subscriber(subscriber)

        # subscriber.add_call(
        #     parser_=parser,
        #     decoder_=decoder,
        #     dependencies_=dependencies,
        #     middlewares_=middlewares,
        # )

        return subscriber