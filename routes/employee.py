import datetime
from ntpath import join
from models.employee import Employee
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template, session

employee_routes = Blueprint('employee_routes', __name__)


@employee_routes.route('/employees')
@login_required
def employees():
    employees_data = Employee().get()
    employee_hours = Employee().get_employee_hours()
    print(employee_hours)
    return render_template('employee.html', employee_hours=employee_hours, employees=employees_data, request_path=request.path,  role=session['role'], logged_in=True)


@employee_routes.route('/add_employee', methods=['POST'])
@login_required
def add_employee():
    if request.form['first_name'] and request.form['last_name'] and request.form['phone'] and request.form['address'] and request.form['job_role'] and request.form['email'] and request.form['salary']:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        job_role = request.form['job_role']
        address = request.form['address']
        salary = request.form['salary']
        Employee().create(first_name, last_name, phone, address, email, job_role, salary)
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('employee_routes.employees'))


@employee_routes.route('/add_hours', methods=['POST'])
@login_required
def add_hours():
    if request.form['employee_id'] and request.form['hours']:
        employee_id = request.form['employee_id']
        hours = request.form['hours']
        entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Employee().insert_employee_hours(employee_id,  entry_date, hours)
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('employee_routes.employees'))


@employee_routes.route('/update_hours', methods=['POST'])
@login_required
def update_hours():
    if request.form['employee_hours_id'] and request.form['hours']:
        employee_hours_id = request.form['employee_hours_id']
        hours = request.form['hours']
        entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Employee().update_employee_hours(employee_hours_id, hours, entry_date)
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('employee_routes.employees'))


@employee_routes.route('/delete_hours/<int:employee_hours_id>', methods=['POST'])
@login_required
def delete_hours(employee_hours_id):
    Employee().delete_employee_hours(employee_hours_id)
    return redirect(url_for('employee_routes.employees'))


@employee_routes.route('/delete_employee/<int:employee_id>', methods=['POST'])
@login_required
def delete_employee(employee_id):
    Employee().delete(employee_id)
    return redirect(url_for('employee_routes.employees'))


@employee_routes.route('/update_employee', methods=['POST'])
@login_required
def update_employee():
    employee_id = request.form['employee_id']
    if request.form['first_name'] and request.form['last_name'] and request.form['phone'] and request.form['address'] and request.form['job_role'] and request.form['email'] and request.form['salary']:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        job_role = request.form['job_role']
        address = request.form['address']
        salary = request.form['salary']
        Employee().update(employee_id, first_name, last_name,
                          phone, address, email, job_role, salary)
    return redirect(url_for('employee_routes.employees'))
