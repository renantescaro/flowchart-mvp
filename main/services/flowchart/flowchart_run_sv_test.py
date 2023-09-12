import json
from requests.models import Response
from main.services.flowchart.flowchart_run_sv import FlowchartRunSv
from faker import Faker
from unittest.mock import patch


fake = Faker()
sut = FlowchartRunSv()


def make_params():
    return {
        "class": fake.word(),
        "nodeDataArray": [
            {
                "color": fake.word(),
                "dataContent": {
                    "nodeType": "getRequest",
                    "params": "",
                    "url": fake.word(),
                },
                "key": -1,
                "text": fake.word(),
            },
            {
                "color": fake.word(),
                "dataContent": {
                    "dataExit": {
                        "content": "latitude: ((latitude)) - longitude: ((longitude)) \nData:((hourly_time1)) -> Temperatura: ((hourly_temperature_2m1))",
                        "tts": False,
                    },
                    "dataInput": {
                        "hourly": {
                            "temperature_2m": ["((hourly_temperature_2m1))"],
                            "time": ["((hourly_time1))"],
                        },
                        "latitude": "((latitude))",
                        "longitude": "((longitude))",
                    },
                    "nodeType": "parserData",
                },
                "key": -2,
                "text": "parser",
            },
            {
                "color": fake.word(),
                "dataContent": {
                    "body": {},
                    "headers": {
                        "Authorization": fake.word(),
                    },
                    "nodeType": "postRequest",
                    "url": fake.word(),
                },
                "key": -3,
                "text": fake.word(),
            },
        ],
        "linkDataArray": [{"from": -1, "to": -2}, {"from": -2, "to": -3}],
    }


@staticmethod
def make_get_mock():
    response = Response()
    response.status_code = 200
    response._content = str.encode(
        json.dumps(
            {
                "latitude": fake.random_number(),
                "longitude": fake.random_number(),
                "generationtime_ms": fake.random_number(),
                "utc_offset_seconds": fake.random_number(),
                "timezone": fake.word(),
                "timezone_abbreviation": fake.word(),
                "elevation": fake.random_number(),
                "hourly_units": {
                    "time": fake.word(),
                    "temperature_2m": fake.word(),
                },
                "hourly": {
                    "time": [
                        "2023-09-12T00:00",
                    ],
                    "temperature_2m": [
                        fake.random_number(),
                    ],
                },
            }
        )
    )
    return response


@staticmethod
def make_post_mock():
    response = Response()
    response.status_code = 200
    response._content = str.encode(json.dumps({}))
    return response


@patch("requests.get", return_value=make_get_mock())
@patch("requests.post", return_value=make_post_mock())
def test_ok(requests_get, requests_post):
    params = make_params()
    content, status_code = sut.execute(params)
    assert status_code == 200


def test_parser_bad_request():
    params = make_params()
    params["linkDataArray"] = [
        {fake.word(): fake.word()},
        {fake.word(): fake.word()},
    ]

    content, status_code = sut.execute(params)
    assert status_code == 400
