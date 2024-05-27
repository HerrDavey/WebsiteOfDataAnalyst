#IMPORTS 
from flask import Flask, render_template, redirect, url_for, request
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from forms import SayHello
import os
from os.path import join, dirname
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Email Data

OWN_EMAIL = os.environ.get('OWN_EMAIL')
OWN_EMAIL_PASSWORD = os.environ.get('OWN_EMAIL_PASSWORD')

#DATABASE DECLARETION
# class Base(DeclarativeBase):
#     pass

# db = SQLAlchemy(model_class=Base)

#ENV CONFIG
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#APP AND SQL CONFIG
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# db.init_app(app)
app.secret_key = os.environ.get('SECRET_KEY_FLASK')

# #DATABASE
# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(unique=True)
#     email: Mapped[str]

# with app.app_context():
#     db.create_all()

#ROUTES
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/my_bacheldor')
def my_bacheldor():
    return render_template('my_bacheldor.html')

@app.route('/say_hello', methods=["GET", "POST"])
def say_hello():
    cform = SayHello()
    if request.method == "POST":
        name_sender = cform.name.data
        email_sender = cform.email.data
        message_sender = cform.message.data
        send_email(name_sender, email_sender, message_sender)
        return redirect(url_for('say_hello'))
    return render_template('say_hello.html', form=cform)

def send_email(name, email, message):
    email_message = MIMEMultipart()
    email_message['From'] = OWN_EMAIL
    email_message['To'] = OWN_EMAIL
    email_message['Subject'] = 'New Message From Website'

    body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    email_message.attach(MIMEText(body, 'plain', 'utf-8'))

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_EMAIL_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message.as_string())

def send_email(name, email, message):
    email_message = MIMEMultipart()
    email_message['From'] = OWN_EMAIL
    email_message['To'] = OWN_EMAIL
    email_message['Subject'] = 'New Message From Website'

    body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    email_message.attach(MIMEText(body, 'plain', 'utf-8'))

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_EMAIL_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message.as_string())


#INITIALISATION
if __name__ == '__main__':
    app.run(debug=False)