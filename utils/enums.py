from enum import Enum, auto

class BookStatus(Enum):
    AVAILABLE = auto()
    BORROWED = auto()
    RESERVED = auto()
    LOST = auto()
    RETURNED = auto()