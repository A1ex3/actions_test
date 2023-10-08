from curses import OK
from http.client import BAD_REQUEST
from fastapi.testclient import TestClient

from .__main__ import app

client = TestClient(app)

def test_main():
    bad_request = client.get("/?count="+"-5345")
    ok_request = client.get("/?count="+"534543543")

    assert bad_request.status_code == BAD_REQUEST
    assert ok_request.status_code == OK