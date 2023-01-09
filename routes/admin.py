from models.employee import Employee
from models.user import User
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from routes.employee import employees

admin_routes = Blueprint('admin_routes', __name__)


@admin_routes.route('/admin')
@login_required
def admin():
    users_data = User().get_user_data()
    employees_data = Employee().get()
    return render_template('admin.html', employees=employees_data, users=users_data, request_path=request.path,  role=session['role'], logged_in=True)


@admin_routes.route('/add_user', methods=['POST'])
@login_required
def add_user():
    if request.form['employee_id'] and request.form['username'] and request.form['password'] and request.form['role']:
        employee_id = request.form['employee_id']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        User().add_user(employee_id, username, password, role)
        flash('Success!', 'success')
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('admin_routes.admin'))


@admin_routes.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    User().delete_user(user_id)
    flash('Success!', 'success')
    return redirect(url_for('admin_routes.admin'))


@admin_routes.route('/update_user', methods=['POST'])
@login_required
def update_user():
    if request.form['user_id'] and request.form['employee_id'] and request.form['username'] and request.form['password'] and request.form['role']:
        user_id = request.form['user_id']
        employee_id = request.form['employee_id']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        User().update_user(user_id, employee_id, username, password, role)
        flash('Success!', 'success')
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('admin_routes.admin'))
