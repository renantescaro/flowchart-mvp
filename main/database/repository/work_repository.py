from typing import Dict, List
from main.database.models.database import Database, select
from main.database.models.work_model import Work


class WorkRepository:
    @staticmethod
    def get_all():
        statement = select(Work)
        items: List[Work] = Database().get_all(statement)
        return [item.to_dict() for item in items]

    @staticmethod
    def get_by_id(id: int) -> Work:
        statement = select(Work).where(Work.id == id)
        work: Work = Database().get_one(statement)
        return work
