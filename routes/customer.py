from models.customer import Customer
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template, session

customer_routes = Blueprint('customer_routes', __name__)


@customer_routes.route('/customers')
@login_required
def customers():
    customers_data = Customer().get()
    return render_template('customer.html', customers=customers_data, request_path=request.path,  role=session['role'], logged_in=True)


@customer_routes.route('/add_customer', methods=['POST'])
@login_required
def add_customer():
    if request.form['first_name'] and request.form['last_name'] and request.form['phone'] and request.form['email']:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        Customer().create(first_name, last_name, phone, email)
        flash('Success!', 'success')
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('customer_routes.customers'))


@customer_routes.route('/delete_customer/<int:customer_id>', methods=['POST'])
@login_required
def delete_customer(customer_id):
    Customer().delete(customer_id)
    flash('Success!', 'success')
    return redirect(url_for('customer_routes.customers'))


@customer_routes.route('/update_customer', methods=['POST'])
@login_required
def update_customer():
    customer_id = request.form['customer_id']
    if request.form['first_name'] and request.form['last_name'] and request.form['phone'] and request.form['email']:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        Customer().update(customer_id, first_name, last_name, phone, email)
        flash('Success!', 'success')
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('customer_routes.customers'))
