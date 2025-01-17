from flask import request

from ilexicon import db
from ilexicon.api import api
from ilexicon.api.model import WordDetail
from ilexicon.exception import EntityNotFoundException
from ilexicon.id import generate_unique_id
from ilexicon.service.dao import Word


@api.get("/word/<word_id>")
def load_word(word_id):
    word = Word.query.get(word_id)
    return WordDetail(word) if word else None

@api.get("/word")
def list_words():
    page = request.args.get("page", type=int, default=1)
    size = request.args.get("size", type=int, default=10)
    paging = Word.query.paginate(page=page, per_page=size)
    paging.items = [WordDetail(word) for word in paging.items]
    return paging

@api.post("/word")
def add():
    body = request.json
    word_id = generate_unique_id()
    word = Word(word_id=word_id,
                chn_name=body["chnName"],
                eng_name=body["engName"],
                eng_abbr=body["engAbbr"],
                std_word_id=body.get("stdWordId"))
    db.session.add(word)
    db.session.commit()
    return word_id

@api.put("/word/<word_id>")
def update(word_id):
    body = request.json
    word = Word.query.get(word_id)
    if not word:
        raise EntityNotFoundException("")
    word.chn_name = body["chnName"]
    word.eng_name = body["engName"]
    word.eng_abbr = body["engAbbr"]
    word.std_word_id = body.__contains__("stdWord") and body["stdWord"]["wordId"] or None
    db.session.commit()

@api.delete("/word/<word_id>")
def delete(word_id):
    Word.query.filter_by(word_id=word_id).delete()
    db.session.commit()