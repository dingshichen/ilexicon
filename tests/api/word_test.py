import json

from flask import url_for

from ilexicon.app import app

with app.test_request_context():
    body = json.dumps(url_for("/api/word/17370258481252573"))
    print(body)