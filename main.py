#IMPORTS 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


#DATABASE DECLARETION
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


#APP AND SQL CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)

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

@app.route('/say_hello')
def say_hello():
    return render_template('say_hello.html')


#INITIALISATION
if __name__ == '__main__':
    app.run(debug=True)