from flask import Flask 
from bricks.config import Config

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  from bricks.item import item_bp 
  app.register_blueprint(item_bp)

  return app




