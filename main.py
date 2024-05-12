#IMPORTS 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from forms import SayHello
import os
from os.path import join, dirname
from dotenv import load_dotenv

#DATABASE DECLARETION
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

#ENV CONFIG
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#APP AND SQL CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)
app.secret_key = os.environ.get('SECRET_KEY_FLASK')

#DATABASE
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

with app.app_context():
    db.create_all()

#ROUTES
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/say_hello', methods=["GET", "POST"])
def say_hello():
    cform = SayHello()
    return render_template('say_hello.html', form=cform)


#INITIALISATION
if __name__ == '__main__':
    app.run(debug=True)