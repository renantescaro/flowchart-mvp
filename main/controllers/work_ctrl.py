from flask import Blueprint, render_template, request

bp = Blueprint(
    "work",
    __name__,
    template_folder="templates",
    url_prefix="/work",
)


class WorkCtrl:
    @bp.route("/save", methods=["POST"])
    def save_work():
        

    @bp.route("/list", methods=["GET"])
    def list_work():
        params = [{"id": 1, "name": "teste", "description": "only a test"}]
        return params, 200

    @bp.route("/load/<id>", methods=["GET"])
    def load_work(id):
        params = {
            "class": "GraphLinksModel",
            "nodeDataArray": [
                {
                    "text": "consultar temperatura",
                    "color": "#ff0f0f",
                    "dataContent": {
                        "nodeType": "getRequest",
                        "url": "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&forecast_days=1",
                        "params": "",
                    },
                    "key": -1,
                },
                {
                    "text": "parser",
                    "color": "#0ffffb",
                    "dataContent": {
                        "nodeType": "parserData",
                        "dataInput": {
                            "latitude": "((latitude))",
                            "longitude": "((longitude))",
                            "hourly": {
                                "time": ["((hourly_time1))"],
                                "temperature_2m": ["((hourly_temperature_2m1))"],
                            },
                        },
                        "dataExit": {
                            "content": "latitude: ((latitude)) - longitude: ((longitude)) \nHora:((hourly_time1)) -> Temperatura: ((hourly_temperature_2m1))",
                            "tts": False,
                        },
                    },
                    "key": -5,
                },
                {
                    "text": "send discord",
                    "color": "#0f2bff",
                    "dataContent": {
                        "nodeType": "postRequest",
                        "url": "https://discord.com/api/channels/1130554954017419357/messages",
                        "body": {},
                        "headers": {"Authorization": "Bot "},
                    },
                    "key": -3,
                },
            ],
            "linkDataArray": [{"from": -1, "to": -5}, {"from": -5, "to": -3}],
        }
        return params, 200
