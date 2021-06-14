import re
from typing import Union, List

from .dictionary import Dictionary

class Translator(Dictionary):
    URL = 'https://www.linguee.com/english-portuguese/search?query={}'
    XPATH = '//span[@class="tag_trans"]'
    
    def __repr__(self) -> str:
        return 'Translator'
    
    
    def return_meaning(self, word: str) -> Union[List[str], bool]:
        try:
            if len(meanings := self._get_meanings(word))>0:
                def text_formatter(mean: str)->str:
                    mean = mean.replace('\n    \t                ', '').replace(':', '.')
                    mean = mean.replace('\n        \n         ', '')
                    return  re.sub('<[^>]*>', '', mean).split()[0].strip()
                meanings = list(map(text_formatter, meanings))
                return [meanings[i] for i in range(len(meanings)) \
                            if not len(meanings[i].split())>1 \
                                if not meanings[i]==word and not '-' in meanings[i]]
            else:
                return False
        except Exception as error:
            print(error)
            return False