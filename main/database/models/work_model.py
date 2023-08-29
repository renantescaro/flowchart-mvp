import json
from typing import Optional
from sqlmodel import Field, SQLModel


class Work(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    data: str = Field(max_length=9999)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "data": json.loads(self.data),
        }
