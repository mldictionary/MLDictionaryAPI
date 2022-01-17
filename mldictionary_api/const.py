from random import randint as random

from mldictionary import English, Portuguese, Spanish

from mldictionary_api.resources import Translator


VIEWS_PREFIX = '/'

API_PREFIX = '/v1'

API_ROUTES_EXAMPLES = [
    API_PREFIX + '/dictionary/en/',
    API_PREFIX + '/translator/en-pt/',
]


API_USE_EXAMPLES = [
    API_ROUTES_EXAMPLES[random(0, 1)] + 'example',
    API_ROUTES_EXAMPLES[random(0, 1)] + 'current',
    API_ROUTES_EXAMPLES[random(0, 1)] + 'store',
    API_ROUTES_EXAMPLES[random(0, 1)] + 'life',
    API_ROUTES_EXAMPLES[random(0, 1)] + 'get',
    API_ROUTES_EXAMPLES[random(0, 1)] + 's',
    API_ROUTES_EXAMPLES[random(0, 1)] + 'sadness',
    API_ROUTES_EXAMPLES[random(0, 1)] + 'crazy',
    API_ROUTES_EXAMPLES[random(0, 1)] + 'mad',
]

DICTIONARIES = {
    'en': English(),
    'pt': Portuguese(),
    'es': Spanish(),
    'en-pt': Translator(),
    'pt-en': Translator(),
}


LOCAL_ADDR = "127.0.0.1"
TOTAL_REQUESTS_ALLOW = 50
TTL_REQUEST = 60 * 60
