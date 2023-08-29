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
    @bp.route("/save", methods=["POST"])
    def save_work():
        try:
            user_group_access = Work(
                name=request.json.get("name"),
                description=request.json.get("description"),
                data=request.json.get("data"),
            )
            Database().save(user_group_access)
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
