
from flask import Flask
from application.database import db
from flask_cors import CORS
from application.worker import *
import redis
import os

basedir = os.path.abspath(os.path.dirname(__file__))

 
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'kanaban.sqlite3')

    app.config["DEBUG"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.secret_key = "deveshisgreat"
    db.init_app(app)
    return app


app = create_app()
app.app_context().push()
from application.api import *
from application.models import *
# from application.controllers import *

 


celery=celery
CELERY_BROKER_URL="redis://0.0.0.0:6379/1"
CELERY_RESULT_BACKEND="redis://0.0.0.0:6379/2"

celery.conf.update(
    broker_url="redis://0.0.0.0:6379/1",
    result_backend="redis://0.0.0.0:6379/2",
    timezone="Asia/Kolkata"
)

celery.Task = ContextTask




if __name__ == "__main__":
    # db.create_all()
    app.run(host='0.0.0.0', port=5001)
    
