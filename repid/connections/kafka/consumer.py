from typing import Iterable

import aiokafka

from repid import ConsumerT, MessageBrokerT, ParametersT, RoutingKeyT
from repid.connections.abc import EncodedPayloadT


class _KafkaConsumer(ConsumerT):
    def __init__(
        self,
        broker: MessageBrokerT,
        queue_name: str,
        topics: Iterable[str] | None = None,
        max_unacked_messages: int | None = None,
    ) -> None:
        self.__consumer: aiokafka.AIOKafkaProducer | None = None

    async def start(self) -> None:
        pass

    async def pause(self) -> None:
        pass

    async def unpause(self) -> None:
        pass

    async def finish(self) -> None:
        pass

    async def consume(self) -> tuple[RoutingKeyT, EncodedPayloadT, ParametersT]:
        pass
