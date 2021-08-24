from flask import Flask
from config import Config
from flask_mail import Mail

# def create_app(config_class=Config):

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail()
mail.init_app(app)

from app import routes