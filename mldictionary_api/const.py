from random import randint as random


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
