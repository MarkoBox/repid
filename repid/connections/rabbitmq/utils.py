from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from datetime import datetime

    from repid.data.protocols import ParametersT, RoutingKeyT


def durable_message_decider(key: RoutingKeyT) -> bool:  # noqa: ARG001
    """Decides if queue is set as durable in RabbitMQ."""
    return True


def qnc(queue_name: str, *, delayed: bool = False, dead: bool = False) -> str:
    """Queue name constructor for RabbitMQ."""
    if dead:  # pragma: no cover
        return f"{queue_name}:dead"
    if delayed:
        return f"{queue_name}:delayed"
    return queue_name


def wait_until(params: ParametersT | None = None) -> datetime | None:
    if params is None or params.delay is None:
        return None
    return params.delay.next_execution_time or params.compute_next_execution_time


class MessageContent(TypedDict):
    payload: str
    parameters: str


@dataclass(frozen=True)
class ExchangeOverrideMapping:
    """
    Override exchange name for jobs which share job_name and queue_name combination.
    """

    exchange_name: str
    job_name: str  # routing on app level
    queue_name: str | None = None  # routing on broker level
