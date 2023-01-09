from models.customer import Customer
from models.employee import Employee
from models.fuel_inventory import FuelInventory
from models.fuel_purchases import FuelPurchases
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from routes.employee import employees
import datetime

fuel_purchases_routes = Blueprint('fuel_purchases_routes', __name__)


@fuel_purchases_routes.route('/fuel_purchases')
@login_required
def fuel_purchases():
    fuel_purchase_data = FuelPurchases().get()
    customer_data = Customer().get()
    employee_data = Employee().get()
    fuel_data = FuelInventory().get()
    return render_template('fuel_purchases.html', fuel_purchases=fuel_purchase_data, customers=customer_data, employees=employee_data, fuels=fuel_data, request_path=request.path,  role=session['role'], logged_in=True)


@fuel_purchases_routes.route('/add_purchase', methods=['POST'])
@login_required
def add_purchase():
    if request.form['employee_id'] and request.form['quantity'] and request.form['customer_id'] and request.form['fuel_id']:
        customer_id = request.form['customer_id']
        quantity = request.form['quantity']
        employee_id = request.form['employee_id']
        fuel_id = request.form['fuel_id']
        fuel_data = FuelInventory().get(fuel_id=fuel_id)
        if fuel_data[-2] < float(request.form['quantity']):
            flash('Not enough fuel available!', 'error')
        else:
            price = fuel_data[-1]*float(request.form['quantity'])
            purchase_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            FuelPurchases().create(employee_id, customer_id,
                                   fuel_id, quantity, price, purchase_date)
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('fuel_purchases_routes.fuel_purchases'))


@fuel_purchases_routes.route('/delete_purchase/<int:purchase_id>', methods=['POST'])
@login_required
def delete_purchase(purchase_id):
    FuelPurchases().delete(purchase_id)
    return redirect(url_for('fuel_purchases_routes.fuel_purchases'))


@fuel_purchases_routes.route('/update_purchase', methods=['POST'])
@login_required
def update_purchase():
    purchase_id = request.form['purchase_id']
    if request.form['employee_id'] and request.form['quantity'] and request.form['customer_id']:
        customer_id = request.form['customer_id']
        quantity = request.form['quantity']
        employee_id = request.form['employee_id']
        fuel_id = request.form['fuel_id']
        fuel_data = FuelInventory().get(fuel_id=fuel_id)
        price = fuel_data[-1]*float(request.form['quantity'])
        purchase_date = datetime.datetime.now()
        FuelPurchases().update(purchase_id, employee_id, customer_id,
                               fuel_id, quantity, price, purchase_date)
    return redirect(url_for('fuel_purchases_routes.fuel_purchases'))
