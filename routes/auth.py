from models.customer import Customer
from models.employee import Employee
from models.user import User
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template, session

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('auth_routes.dashboard'))

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
    return render_template('login.html', request_path=request.path,  role=session['role'], logged_in=False)


@auth_routes.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('auth_routes.login'))


@auth_routes.route('/dashboard')
@login_required
def dashboard():
    customer_data = Customer().get()
    employee_data = Employee().get()
    return render_template('dashboard.html', employees=employee_data, customers=customer_data, request_path=request.path,  role=session['role'], logged_in=True)
