import requests
from rq import Queue
from typing import Dict
from flask import Blueprint, request
from main.helpers.worker import enqueue


bp = Blueprint(
    "worker_ping",
    __name__,
    template_folder="templates",
    url_prefix="/api/worker-ping",
)


@bp.route("/", methods=["POST"])
def ping():
    message = request.json.get("message")
    authorization = request.json.get("authorization")

    url = request.json.get("url")
    headers = {"Authorization": authorization}
    body = {
        "content": message,
        "tts": False,
    }

    enqueue(url, headers, body)

    return {}, 200
