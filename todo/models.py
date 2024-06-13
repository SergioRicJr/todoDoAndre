from typing import Any
from datetime import datetime

class TaskEntity:
    def __init__(self, name: str, description: str, due_date: datetime, completed: bool = False) -> None:
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self) -> str:
        return f"Task <{self.name}>"

    def __getattribute__(self, __name: str) -> Any:
        if __name == 'due_date':
            return object.__getattribute__(self, __name).strftime("%d/%m/%Y %H:%M:%S")
        else:
            return object.__getattribute__(self, __name)