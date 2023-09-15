import os
from typing import Dict
import redis
import requests
from rq import Worker, Queue, Connection
from dotenv import load_dotenv

listen = ["high", "default", "low"]

load_dotenv()
redis_url = os.getenv("REDISCLOUD_URL")
conn = redis.from_url(redis_url)


def _redis_queue_request(url: str, headers: Dict, body: Dict):
    requests.post(url=url, data=body, headers=headers)


def enqueue(url: str, headers: Dict, body: Dict):
    q = Queue(connection=conn)
    return q.enqueue("worker._redis_queue_request", url, headers, body)


if __name__ == "__main__":
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
