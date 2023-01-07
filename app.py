from flask import Flask, render_template, request, redirect, url_for
from models import user

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_model = user.User()
        username = request.form['username']
        password = request.form['password']
        user = user_model.validate_login(username, password)
        if user:
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid login credentials'
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
