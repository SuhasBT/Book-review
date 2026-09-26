from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (you can replace with SQLite later)
reviews = []


@app.route('/')
def index():
    return render_template('index.html', reviews=reviews)


@app.route('/add', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        reviews.append({'title': title, 'text': text})
        return redirect(url_for('index'))
    return render_template('add_review.html')


@app.route('/reviews')
def get_reviews():
    return {"reviews": reviews}


if __name__ == '__main__':
    app.run(debug=True)
