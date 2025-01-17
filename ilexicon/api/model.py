from ilexicon import ApiModel
from ilexicon.service.dao import Word


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
