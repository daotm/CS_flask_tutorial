from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Triet Dao',
        'title': 'Post 1',
        'content': 'First post',
        'date_post': 'April 22, 2022'
    },
    {
        'author': 'Tom Schafer',
        'title': 'Post 2',
        'content': 'Second post',
        'date_post': 'April 25, 2018'
    },
]





@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

