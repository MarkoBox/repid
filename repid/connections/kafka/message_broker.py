import aiokafka

from repid import ParametersT, RoutingKeyT
from repid.connections.abc import EncodedPayloadT, MessageBrokerT

from .consumer import _KafkaConsumer


class KafkaMessageBroker(MessageBrokerT):
    CONSUMER_CLASS = _KafkaConsumer

    def __init__(self, dsn: str, *, some_arg):
        self.dsn = dsn
        self.__producer: aiokafka.AIOKafkaProducer | None = None

    async def connect(self) -> None:
        if self.__producer is None:
            self.__producer = aiokafka.AIOKafkaProducer(bootstrap_servers=self.dsn)

    async def disconnect(self) -> None:
        await self.__producer.stop()

    async def enqueue(
        self, key: RoutingKeyT, payload: EncodedPayloadT = "", params: ParametersT | None = None,
    ) -> None:
        await self.__producer.send(key=key, value=payload.encode("utf-8"), topic="test")

    async def reject(self, key: RoutingKeyT) -> None:
        pass

    async def ack(self, key: RoutingKeyT) -> None:
        pass

    async def nack(self, key: RoutingKeyT) -> None:
        pass

    async def requeue(
        self, key: RoutingKeyT, payload: EncodedPayloadT = "", params: ParametersT | None = None,
    ) -> None:
        pass

    async def queue_declare(self, queue_name: str) -> None:
        pass

    async def queue_flush(self, queue_name: str) -> None:
        pass

    async def queue_delete(self, queue_name: str) -> None:
        pass
