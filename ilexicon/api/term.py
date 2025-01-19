from flask import request

from ilexicon import db
from ilexicon.api import api
from ilexicon.api.model import TermDetail, TermItem
from ilexicon.exception import EntityNotFoundException
from ilexicon.id import generate_unique_id
from ilexicon.service.dao import Term


@api.get("/term/<term_id>")
def load_term(term_id):
    term = Term.query.get(term_id)
    return TermDetail(term) if term_id else None

@api.get("/term")
def list_terms():
    page = request.args.get("page", type=int, default=1)
    size = request.args.get("size", type=int, default=10)
    paging = Term.query.paginate(page=page, per_page=size)
    paging.items = [TermItem(term) for term in paging.items]
    return paging

@api.post("/term")
def add():
    body = request.json
    term_id = generate_unique_id()
    # TODO 计算是否是标准用语
    std_term_flag = True
    term = Term(term_id=term_id,
                chn_name=body["chnName"],
                eng_name=body["engName"],
                eng_abbr=body["engAbbr"],
                std_term_flag=std_term_flag,
                words=body["words"])
    # TODO 保存词素结构
    db.session.add(term)
    db.session.commit()
    return term_id

@api.put("/term/<term_id>")
def update(term_id):
    body = request.json
    term = Term.query.get(term_id)
    if not term:
        raise EntityNotFoundException()
    term.chn_name = body["chnName"]
    term.eng_name = body["engName"]
    term.eng_abbr = body["engAbbr"]
    term.words = body["words"]
    # TODO 计算是否是标准用语
    db.session.commit()

@api.delete("/term/<term_id>")
def delete(term_id):
    Term.query.filter_by(term_id=term_id)
    db.session.commit()

