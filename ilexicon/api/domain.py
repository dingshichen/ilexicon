from flask import request

from ilexicon import db
from ilexicon.api import api
from ilexicon.api.model import DomainDetail, DomainItem
from ilexicon.exception import EntityNotFoundException
from ilexicon.id import generate_unique_id
from ilexicon.service.dao import Domain

@api.get("/domain/<domain_id>")
def load_domain(domain_id):
    domain = Domain.query.get(domain_id)
    return DomainDetail(domain) if domain else None

@api.get("/domain")
def list_domains():
    page = request.args.get("page", type=int, default=1)
    size = request.args.get("size", type=int, default=10)
    paging = Domain.query.paginate(page=page, per_page=size)
    paging.items = [DomainItem(domain) for domain in paging]
    return paging

@api.post("/domain")
def add():
    body = request.json
    domain_id = generate_unique_id()
    domain = Domain(domain_id=domain_id,
                    logic_data_type=body["logicDataType"],
                    length=body["length"],
                    precision=body["precision"],
                    default_flag=body["defaultFlag"],
                    word_id=body.get("wordId"))
    db.session.add(domain)
    db.session.commit()
    return domain_id

@api.put("/domain/<domain_id>")
def update(domain_id):
    body = request.json
    domain = Domain.query.get(domain_id)
    if not domain:
        raise EntityNotFoundException("")
    domain.logic_data_type = body["logicDataType"]
    domain.length = body["length"]
    domain.precision = body["precision"]
    domain.default_flag = body["defaultFlag"]
    # TODO 有且仅有一个默认域
    db.session.commit()

@api.delete("/domain/<domain_id>")
def delete(domain_id):
    Domain.query.filter_by(domain_id=domain_id).delete()
    db.session.commit()
