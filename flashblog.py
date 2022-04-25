from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '79a12b36c38394040b2af0a00197e585'


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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

