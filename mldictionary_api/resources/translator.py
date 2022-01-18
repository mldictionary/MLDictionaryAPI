from mldictionary import Dictionary


class Translator(Dictionary):
    URL = 'https://www.linguee.com/english-portuguese/search?source=auto&query={}'
    LANGUAGE = 'Translator(en-pt)'
    TARGET_TAG = 'a'
    TARGET_ATTR = {'class': 'featured'}
    REPLACES = {}
