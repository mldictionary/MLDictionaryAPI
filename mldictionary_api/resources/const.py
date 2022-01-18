from mldictionary import English, Portuguese, Spanish

from mldictionary_api.resources.translator import Translator

LIMITED_REQUESTS_DICTIONARIES = [Translator]
LOCAL_ADDR = '127.0.0.1'
TOTAL_REQUESTS_ALLOW = 50
TTL_REQUEST = 60 * 60
TTL_MEANINGS_CACHE = 24 * 60 * 60


ENGLISH_REPR = 'en'
PORTUGUESE_REPR = 'pt'
SPANISH_REPR = 'es'
ENGLISH_TO_PORTUGUESE_REPR = 'en-pt'
PORTUGUESE_TO_ENGLISH = 'pt-en'


DICTIONARIES = {
    ENGLISH_REPR: English(),
    PORTUGUESE_REPR: Portuguese(),
    SPANISH_REPR: Spanish(),
    ENGLISH_TO_PORTUGUESE_REPR: Translator(),
    PORTUGUESE_TO_ENGLISH: Translator(),
}
