from ntpath import join
from models.employee import Employee
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template

employee_routes = Blueprint('employee_routes', __name__)


@employee_routes.route('/employees')
@login_required
def employees():
    employees_data = Employee().get()
    return render_template('employee.html', employees=employees_data)


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
