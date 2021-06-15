from flask import Flask, jsonify, request, redirect

from .webscrapy import English, Portuguese, Spanish, Translator

def init_app(app: Flask):
    
    @app.route('/v1/dictionary/en/<word>/', methods=['get'])
    @app.route('/v1/dictionary/pt/<word>/', methods=['get'])
    @app.route('/v1/dictionary/es/<word>/', methods=['get'])
    @app.route('/v1/translator/en-pt/<word>/', methods=['get'])
    @app.route('/v1/translator/pt-en/<word>/', methods=['get'])
    def api(word: str):
        current_route_work = request.url.split('/')[5]
        route_dictionary = {
            'en': English(),
            'pt': Portuguese(),
            'es': Spanish(),
            'en-pt': Translator(),
            'pt-en': Translator()
        }
        dictionary = route_dictionary[current_route_work]
        if meanings:=dictionary.return_meaning(word):
            api_return = {
                'source': dictionary.URL.format(word),
                'meanings': meanings
                }
            code_status = 200
        else:
            api_return = {'message': 'Not Found'}
            code_status = 404     
        return jsonify(api_return), code_status

    @app.errorhandler(404)
    def error(error):
        return jsonify({'message': 'Not Found'}), 404