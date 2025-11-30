from typing import Any
from faststream._internal.endpoint.subscriber.call_item import CallsCollection
from faststream._internal.endpoint.subscriber.specification import SubscriberSpecification
from faststream._internal.endpoint.subscriber.usecase import SubscriberUsecase
from faststream._internal.types import MsgType
from faststream.sqla.configs.subscriber import SqlaSubscriberConfig
from faststream.sqla.parser import SqlaParser


class SqlaSubscriber(SubscriberUsecase[Any]):
    def __init__(
        self,
        config: "SqlaSubscriberConfig",
        specification: "SubscriberSpecification[Any, Any]",
        calls: "CallsCollection[MsgType]",
    ) -> None:
        self.parser = SqlaParser()
        config.parser = self.parser.parse_message
        config.decoder = self.parser.decode_message
        super().__init__(config, specification, calls)