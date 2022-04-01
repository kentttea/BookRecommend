from flask import (
     Flask, 
     request, 
     render_template)
from test import recommend

app = Flask(__name__)

@app.route('/', methods=['GET'])
def layout():
	return render_template('layout.html')


# @app.route('/question', methods=['POST'])
# def book_recommend():
#     genre = request.form.get('genre')
#     now = request.form.get('now')
#     after = request.form.get('after')
#     want = request.form.get('want')
#     excepting = request.form.get('excepting')
#     book = recommend(genre=genre, now=now, after=after, want=want, excepting=excepting)
#     return book



@app.route('/question', methods=['POST'])
def question():
    return render_template('question.html')

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        genre = request.form.get('genre')
        now = request.form.get('now')
        after = request.form.get('after')
        want = request.form.get('want')
        excepting = request.form.get('excepting')
        book = recommend(genre=genre, now=now, after=after,
                         want=want, excepting=excepting)
        if len(book) > 1:
            return render_template('result.html', message='"{}"か"{}"の本がおすすめです！'.format(book[0], book[1]))
        else:
            return render_template('result.html', message='{}の本がおすすめです！'.format(book))



if __name__ == "__main__":
    app.run(debug=True, port="8888")


