from typing import Optional
from flask import Blueprint, render_template, request

from main.database.models.database import Database
from main.database.models.work_model import Work
from main.database.repository.work_repository import WorkRepository

bp = Blueprint(
    "work",
    __name__,
    template_folder="templates",
    url_prefix="/work",
)


class WorkCtrl:
    @bp.route("/delete", methods=["POST"])
    def delete_work():
        try:
            id_work = request.json.get("id")
            work = WorkRepository.get_by_id(id_work)
            Database().delete(work)
            return {}, 200
        except Exception as e:
            print(e)
            return {}, 400

    @staticmethod
    @bp.route("/save/<id>", methods=["POST"])
    @bp.route("/save", methods=["POST"])
    def save_work(id: Optional[int] = None):
        try:
            name = request.json.get("name")
            description = request.json.get("description")
            data = request.json.get("data")
            if not name or not description:
                return {}, 400

            if id:
                work = WorkRepository.get_by_id(id)
                work.name = name
                work.description = description
                work.data = data

                Database().save(work)
                return {}, 200

            work = Work(
                name=name,
                description=description,
                data=data,
            )
            Database().save(work)
            return {}, 200

        except Exception as e:
            print(e)
            return str(e), 400

    @bp.route("/list", methods=["GET"])
    def list_work():
        return WorkRepository.get_all(), 200

    @bp.route("/load/<id>", methods=["GET"])
    def load_work(id):
        data = WorkRepository.get_by_id(id).to_dict()
        return data, 200
