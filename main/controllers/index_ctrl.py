from flask import Blueprint, render_template

bp = Blueprint(
    "index",
    __name__,
    template_folder="templates",
)


class IndexCtrl:
    @bp.route("/", methods=["GET"])
    def inicial_json():
        return render_template("index.html")
