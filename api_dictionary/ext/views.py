from flask import Flask, render_template

def init_app(app: Flask)->None:
    
    @app.route('/')
    @app.route('/index.html/')
    def index():
        return render_template('index.html')
