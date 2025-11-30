from typing import Any, Iterable, Optional, Union

from sqlalchemy.ext.asyncio import AsyncEngine

from faststream._internal.broker import BrokerUsecase
from faststream.security import BaseSecurity
from faststream.specification.schema.broker import BrokerSpec
from faststream.specification.schema.extra.tag import Tag, TagDict
from faststream.sqla.broker.registrator import SqlaRegistrator
from faststream.sqla.configs.broker import SqlaBrokerConfig


class SqlaBroker(
    SqlaRegistrator,
    BrokerUsecase[
        Any,
        Any,
    ],
):
    url: list[str]

    def __init__(
        self,
        *,
        engine: AsyncEngine,
        # broker base args
        routers: Iterable[SqlaRegistrator] = (),
        # AsyncAPI args
        security: Optional["BaseSecurity"] = None,
        specification_url: str | Iterable[str] | None = None,
        protocol: str | None = None,
        protocol_version: str | None = "auto",
        description: str | None = None,
        tags: Iterable[Union["Tag", "TagDict"]] = (),
    ) -> None:

        super().__init__(
            routers=routers,
            config=SqlaBrokerConfig(),
            specification=BrokerSpec(
                description=description,
                url=specification_url,
                protocol=protocol,
                protocol_version=protocol_version,
                security=security,
                tags=tags,
            ),
        )
    
    async def _connect(self) -> Any:
        return True

    async def start(self) -> None:
        await self.connect()
        await super().start()