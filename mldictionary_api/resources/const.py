import os

from mldictionary import English, Portuguese, Spanish

from mldictionary_api.domains.environment import EnvironmentEnum
from mldictionary_api.resources.translator import Translator
from .utils import limit_requests

LIMITED_REQUESTS_DICTIONARIES = [Translator]

# change to Environment.DEVELOPMENT based if it will or won't be necessary make cache
ENVIRONMENT = os.getenv('ENVIRONMENT', EnvironmentEnum.LOCAL.name)

LIMITED_REQUESTS = limit_requests[getattr(EnvironmentEnum, ENVIRONMENT)]


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
