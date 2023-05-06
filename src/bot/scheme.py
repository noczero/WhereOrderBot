from dataclasses import dataclass, asdict
from json import dumps


@dataclass
class Tracking:
    name: str
    status: str
    estimate_process_time: str


@dataclass
class OrderedProduct:
    order_id: str
    name: str
    tracking: Tracking


@dataclass
class User:
    full_name: str


@dataclass
class InputMessage:
    intent: str
    product: OrderedProduct
    user: User

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)


@dataclass
class OutputMessage:
    request: InputMessage
    response: str

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)


