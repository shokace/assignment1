from flask import Flask
from models import db, Message
from config import Config
from routes import messages_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(messages_bp)

    @app.route("/")
    def hello():
        return "Hello, world!"

    with app.app_context():
        db.create_all()  #Create tables

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")