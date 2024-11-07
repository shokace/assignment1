from flask import Flask
from models import db, Message  
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy 
db.init_app(app)

@app.route("/")
def hello():
    return "Assingment 1 Initialized"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(host="0.0.0.0")