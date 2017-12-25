import os
import logging
from flask import Flask
from frame import config
from logging.handlers import TimedRotatingFileHandler
from views import home, manager
import json
from models.baseModel import db

from models.users import User


class NonASCIIJSONEncoder(json.JSONEncoder):
    def __init__(self, **kwargs):
        kwargs['ensure_ascii'] = False
        super(NonASCIIJSONEncoder, self).__init__(**kwargs)

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, bytes):
            return o.decode('utf-8')

        return json.JSONEncoder.default(self, o)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    logfile = os.path.join(app.root_path, 'log/log.log')
    if not os.path.exists(os.path.dirname(logfile)):
        os.mkdir(os.path.dirname(logfile))
    file_handler = TimedRotatingFileHandler(logfile, 'D', 1, 15)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
    # app.logger.setLevel(app.config.get('LOGGING_LEVEL'))
    file_handler.setLevel(app.config.get('LOGGING_LEVEl', logging.DEBUG))
    app.logger.addHandler(file_handler)
    app.register_blueprint(home.bp)
    app.register_blueprint(manager.bp, url_prefix='/manager')

    app.json_encoder = NonASCIIJSONEncoder
    db.init_app(app)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=app.config.get('PORT'),
        debug=app.debug,
        threaded=True)
