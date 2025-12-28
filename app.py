from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.routes.task_routes import task_bp

db = SQLAlchemy()

def create_app():
 app = Flask(__name__)
 app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

 db.init_app(app)
 app.register_blueprint(task_bp, url_prefix='/tasks')

 with app.app_context():
     db.create_all()

 return app

if __name__ == "__main__":
 app = create_app()
 app.run(debug=True)
