from flask import Flask, redirect

def init_app(app: Flask)->None:
    
    @app.route('/')
    def index():
        return redirect('https://github.com/PabloEmidio/api-dictionary')
