from bammysite.uploads import images
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_mail import Mail,Message
from flask_script import Manager
from flask_ckeditor import CKEditor
from flask_uploads import configure_uploads
from config import config
import os

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
manager = Manager()
ckeditor = CKEditor()

def __call__(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    ckeditor.init_app(app)

    # configure image set with app
    configure_uploads(app,images)

    # register blueprint
    from bammysite.site import sitemod

    app.register_blueprint(sitemod)

    app.secret_key = os.urandom(24)

    return app