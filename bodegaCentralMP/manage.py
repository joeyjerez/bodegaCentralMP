#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from flask import Flask, Config, app, render_template


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bodegaCentralMP.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    from webpayplus import bp as webpay_plus_bp


    app.register_blueprint(webpay_plus_bp, url_prefix="/webpay-plus")
 

    @app.route('/')
    def index():
        return render_template('base.html')

    return app


create_app().run()