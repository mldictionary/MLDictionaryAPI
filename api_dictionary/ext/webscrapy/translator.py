from mldictionary import Dictionary

class Translator(Dictionary):
    URL = 'https://www.linguee.com/english-portuguese/search?source=auto&query={}'
    LANGUAGE = 'Translator(en-pt)'
    TARGET_TAG = 'span'
    TARGET_ATTR = {'class': 'tag_trans'}
