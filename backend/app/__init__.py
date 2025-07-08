from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # DB初期化
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint登録
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# アプリケーションコンテキスト外でのインポートを避けるため、最後にインポート
from app import models