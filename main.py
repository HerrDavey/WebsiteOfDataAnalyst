from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/say_hello')
def say_hello():
    return render_template('say_hello.html')

if __name__ == '__main__':
    app.run(debug=True)