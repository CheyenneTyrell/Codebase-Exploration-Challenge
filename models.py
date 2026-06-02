from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    ABANDONED = "ABANDONED"


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: Status
    priority: Priority
    due_date: str  # ISO format string
    created_at: str

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=Status(data["status"]),
            priority=Priority(data["priority"]),
            due_date=data["due_date"],
            created_at=data["created_at"],
        )