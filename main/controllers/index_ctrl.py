from flask import Blueprint, render_template, request
from main.services.flowchart.flowchart_run_sv import FlowchartRunSv

bp = Blueprint(
    "index",
    __name__,
    template_folder="templates",
)


class IndexCtrl:
    @bp.route("/", methods=["GET"])
    def index():
        return render_template("flowchart/index.html")

    @bp.route("/run", methods=["POST"])
    def run():
        result = FlowchartRunSv().execute(request.json)
        return result, 200
