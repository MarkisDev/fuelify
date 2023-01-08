from models.user import User
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template, session

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_model = User()
        result = user_model.validate_login(username, password)
        if result:
            session['user_id'] = result[0]
            session['username'] = result[1]
            session['role'] = result[4]
            return redirect(url_for('auth_routes.dashboard'))
        else:
            flash('Incorrect username or password')
    return render_template('login.html')


@auth_routes.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('auth_routes.login'))


@auth_routes.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    user_data = User().get_user_data(user_id)
    return render_template('dashboard.html', user=user_data)
