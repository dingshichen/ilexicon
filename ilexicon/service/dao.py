from sqlalchemy import Column, BigInteger, String, Boolean, ForeignKey, Integer

from ilexicon import db

term_fragment = db.Table("term_fragment",
                         Column("term_id", BigInteger, ForeignKey("term.term_id"), primary_key=True),
                         Column("word_id", BigInteger, ForeignKey("word.word_id"), primary_key=True),
                         Column("sort_no", Integer))


class Word(db.Model):
    word_id = Column(BigInteger, primary_key=True)
    chn_name = Column("chn_nm", String)
    eng_name = Column("eng_nm", String)
    eng_abbr = Column("eng_abbr", String)
    std_word_id = Column(BigInteger, ForeignKey("word.word_id"), nullable=True)
    std_word = db.relationship("Word", uselist=False)


class Domain(db.Model):
    domain_id = Column(BigInteger, primary_key=True)
    word_id = Column(BigInteger, ForeignKey("word.word_id"))
    logic_data_type = Column("logic_data_typ", String)
    length = Column("len", BigInteger, primary_key=True)
    precision = Column("prcsn", BigInteger)
    default_flag = Column("deflt_flg", Boolean)
    word = db.relationship("Word", uselist=False)


class Term(db.Model):
    term_id = Column(BigInteger, primary_key=True)
    chn_name = Column("chn_nm", String)
    eng_name = Column("eng_nm", String)
    eng_abbr = Column("eng_abbr", String)
    std_term_flag = Column("std_term_flg", Boolean)
    words = db.relationship("Word", secondary=term_fragment, lazy="dynamic")