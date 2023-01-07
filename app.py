import uuid
from functools import wraps
from flask import Flask, request, session, redirect, url_for, flash, render_template
from models import database, user
# , fuel_inventory, fuel_purchase, customer_information
app = Flask(__name__)
app.secret_key = str(uuid.uuid4())


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_id' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_model = user.User()
        result = user_model.validate_login(username, password)
        if result:
            session['user_id'] = result[0]
            session['username'] = result[1]
            session['role'] = result[4]
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    user_id = session['user_id']
    user_model = user.User()
    user_data = user_model.get_user_data(user_id)
    return render_template('home.html', user_data=user_data)


if __name__ == '__main__':
    app.run(debug=True)
