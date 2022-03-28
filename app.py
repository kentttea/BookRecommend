from crypt import methods
from email import message
import os
import sys 
from flask import (
     Flask, 
     request, 
     render_template)
from test import recommend

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
	return render_template('index.html')


# @app.route("/", methods=['POST'])
# def post():
#     book = request.form.get('now')
#     return render_template('index.html', message = '{}の本がおすすめです！'.format(book))

@app.route("/", methods=['POST'])
def book_recommend():
    now = request.form.get('now')
    genre = request.form.get('genre')
    excepting = request.form.get('excepting')
    book = recommend(now=now, genre=genre, excepting=excepting)
    return render_template('index.html', message = '{}の本がおすすめです！'.format(book))

if __name__ == "__main__":
    app.run(debug=True)


