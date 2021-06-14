'''
adapted code from:
    https://github.com/PabloEmidio/MultiLanguage-Dictionary/blob/main/webscrapy/dictionary.py
'''

from abc import ABC, abstractmethod
import unicodedata
import re
import requests
from typing import List, Union

from parsel import Selector

class Dictionary(ABC):
    URL: str
    XPATH: str
    
    @abstractmethod
    def __repr__(self)->str:
        return 'Dictionary'

    
    @classmethod
    def _search(cls, word: str)->str:
        with requests.get(cls.URL.format(word), \
                            headers={'User-Agent': 'Mozilla/5.0'}) as response:
            return response.text
        
        
    @classmethod
    def _get_meanings(cls, word: str)->List[str]:
        response = Selector(text=cls._search(word))
        meanings = list(dict.fromkeys(response.xpath(cls.XPATH).getall())) # don't allow duplicated item
        return meanings


    @abstractmethod
    def return_meaning(self, word: str)->Union[List[str], bool]:
        ...


class English(Dictionary):
    URL = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
    XPATH = '//div[has-class("def", "ddef_d", "db")]'
    
    def __repr__(self)->str:
        return 'English'


    def return_meaning(self, word: str)->Union[List[str], bool]:
        try:
            if len(meanings := self._get_meanings(word))>0:
                def text_formatter(mean: str)->str:
                    mean = mean.replace('\n    \t                ', '').replace(':', '.')
                    mean = mean.replace('\n        \n         ', '')
                    return re.sub('<[^>]*>', '', mean)
                return list(map(text_formatter, meanings)) or False
            else:
                return False
        except Exception as error:
            print(error)
            return False


class Portuguese(Dictionary):
    URL = 'https://www.dicio.com.br/{}/'
    XPATH = '//p[@itemprop="description"]/span'
    
    def __repr__(self)->str:
        return 'Portuguese'


    def return_meaning(self, word: str)->Union[List[str], bool]:
        word = unicodedata.normalize('NFD', word)
        word = re.sub('[\u0300-\u036f]', '', word)
        try:
            if len(meanings := self._get_meanings(word))>0:
                def text_formatter(mean: str)->str:
                    if 'class="cl"' in mean or 'class="etim"' in mean:
                        return ''
                    return re.sub('<[^>]*>', '', mean)
                return [re.sub('<[^>]*>', '', mean) for mean in meanings \
                        if not('class="cl"' in mean or 'class="etim"' in mean)] or False
            else:
                return False
        except Exception as error:
            print(error)
            return False
        

class Spanish(Dictionary):
    URL = 'https://www.wordreference.com/definicion/{}'
    XPATH = '//ol[@class="entry"]//li'
    
    def __repr__(self)->str:
        return 'Spanish'
    
    
    def return_meaning(self, word: str)->Union[List[str], bool]:
        word = unicodedata.normalize('NFD', word)
        word = re.sub('[\u0300-\u036f]', '', word)
        try:
            if len(meanings := self._get_meanings(word))>0:
                def text_formatter(mean: str)->str:
                    mean = mean.replace('<br>', ' \n ')
                    return  re.sub('<[^>]*>', '', mean)
                return list(map(text_formatter, meanings)) or False
            else:
                return False
        except Exception as error:
            print(error)
            return False
