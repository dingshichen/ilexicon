from ilexicon import ApiModel
from ilexicon.service.dao import Word, Domain, Term


class WordOption(ApiModel):
    word_id: int
    chn_name: str

    def __init__(self, word: Word):
        self.word_id = word.word_id
        self.chn_name = word.chn_name

    def as_dict(self) -> dict:
        return {
            "wordId": self.word_id,
            "chnName": self.chn_name,
        }


class WordItem(WordOption):
    eng_abbr: str
    std_word: WordOption | None

    def __init__(self, word: Word):
        super().__init__(word)
        self.eng_abbr = word.eng_abbr
        self.std_word = WordOption(word.std_word) if word.std_word else None

    def as_dict(self) -> dict:
        return {
            "wordId": self.word_id,
            "chnName": self.chn_name,
            "engAbbr": self.eng_abbr,
            "stdWord": self.std_word.as_dict() if self.std_word else None,
        }


class WordDetail(WordItem):

    def __init__(self, word: Word):
        super().__init__(word)


class DomainOption(ApiModel):
    domain_id: int
    word: WordOption

    def __init__(self, domain: Domain):
        self.domain_id = domain.domain_id
        self.word = WordOption(domain.word)

    def as_dict(self) -> dict:
        return {
            "domainId": self.domain_id,
            "word": self.word.as_dict(),
        }


class DomainItem(DomainOption):
    logic_data_type: str
    length: int
    precision: int
    default_flag: bool

    def __init__(self, domain: Domain):
        super().__init__(domain)
        self.logic_data_type = domain.logic_data_type
        self.length = domain.length
        self.precision = domain.precision
        self.default_flag = domain.default_flag

    def as_dict(self) -> dict:
        return {
            "domainId": self.domain_id,
            "word": self.word.as_dict(),
            "logicDataType": self.logic_data_type,
            "length": self.length,
            "precision": self.precision,
            "defaultFlag": self.default_flag,
        }


class DomainDetail(DomainItem):

    def __init__(self, domain: Domain):
        super().__init__(domain)


class TermOption(ApiModel):
    term_id: int
    chn_name: str

    def __init__(self, term: Term):
        self.term_id = term.term_id
        self.chn_name = term.chn_name

    def as_dict(self) -> dict:
        return {
            "termId": self.term_id,
            "chnName": self.chn_name,
        }

class TermItem(TermOption):
    eng_name = str
    eng_abbr = str
    std_term_flag = bool

    def __init__(self, term: Term):
        super().__init__(term)
        self.eng_name = term.eng_name
        self.eng_abbr = term.eng_abbr
        self.std_term_flag = term.std_term_flag

    def as_dict(self) -> dict:
        return {
            "termId": self.term_id,
            "chnName": self.chn_name,
            "engName": self.eng_name,
            "engAbbr": self.eng_abbr,
            "stdTermFlag": self.std_term_flag,
        }


class TermDetail(TermItem):
    words = tuple[WordOption]

    def __init__(self, term: Term):
        super().__init__(term)

    def as_dict(self) -> dict:
        return {
            "termId": self.term_id,
            "chnName": self.chn_name,
            "engName": self.eng_name,
            "engAbbr": self.eng_abbr,
            "stdTermFlag": self.std_term_flag,
            "words": [word.as_dict() for word in self.words],
        }

