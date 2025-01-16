from flask import request

from ilexicon import db
from ilexicon.api import api
from ilexicon.id import generate_unique_id
from ilexicon.service.dao import Word


@api.get("/word/<id>")
def load_word(id):
    pass


@api.post("/word/list")
def list_words():
    pass


@api.post("/word")
def add():
    body = request.json
    word = Word(word_id=generate_unique_id(),
                chn_name=body["chnName"],
                eng_name=body["engName"],
                eng_abbr=body["engAbbr"],
                std_word_flag=body["stdWordFlag"],
                std_word_id=body.get("stdWordId"))
    db.session.add(word)
    db.session.commit()
    return "ok"


@api.put("/word/<id>")
def update():
    pass


@api.delete("/word/<id>")
def delete():
    pass