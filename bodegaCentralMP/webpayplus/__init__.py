from flask import Flask, Config, app, render_template
import os

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, '/bodega/templates')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    from webpay_plus import bp as webpay_plus_bp

    app.register_blueprint(webpay_plus_bp, url_prefix="/webpay-plus")


    @app.route('/')
    def index():
        return render_template('base.html')

    return app


create_app().run()
#create_app()