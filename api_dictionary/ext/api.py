from flask import Flask, jsonify

from .webscrapy import English, Portuguese, Spanish

def init_app(app: Flask):
    
    @app.route('/v1/en/<word>/')
    def api_en(word: str):
        dictionary = English()
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
    
    @app.route('/v1/pt/<word>/')
    def api_pt(word):
        dictionary = Portuguese()
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
    
    @app.route('/v1/es/<word>/')
    def api_es(word):
        dictionary = Spanish()
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