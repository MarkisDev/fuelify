from models.fuel_inventory import FuelInventory
from helpers.utils import login_required

from flask import Blueprint, request, redirect, url_for, flash, render_template, session

fuel_inventory_routes = Blueprint('fuel_inventory_routes', __name__)


@fuel_inventory_routes.route('/fuel_inventory')
@login_required
def fuel_inventory():
    fuel_inventory_data = FuelInventory().get()
    return render_template('fuel_inventory.html', fuel_inventory=fuel_inventory_data, request_path=request.path,  role=session['role'], logged_in=True)


@fuel_inventory_routes.route('/add_fuel', methods=['POST'])
@login_required
def add_fuel():
    if request.form['fuel_type'] and request.form['quantity'] and request.form['price']:
        fuel_type = request.form['fuel_type']
        quantity = request.form['quantity']
        price = request.form['price']
        FuelInventory().create_fuel(fuel_type, quantity, price)
        flash('Success!', 'success')
    else:
        flash('Enter all details!', 'error')
    return redirect(url_for('fuel_inventory_routes.fuel_inventory'))


@fuel_inventory_routes.route('/delete_fuel/<int:fuel_id>', methods=['POST'])
@login_required
def delete_fuel(fuel_id):
    FuelInventory().delete_fuel(fuel_id)
    flash('Success!', 'success')
    return redirect(url_for('fuel_inventory_routes.fuel_inventory'))


@fuel_inventory_routes.route('/update_fuel', methods=['POST'])
@login_required
def update_fuel():
    fuel_id = request.form['fuel_id']
    if request.form['new_quantity'] and request.form['price']:
        FuelInventory().update_fuel(
            fuel_id, quantity=request.form['new_quantity'], price=request.form['price'])
        flash('Success!', 'success')
    elif request.form['new_quantity']:
        FuelInventory().update_fuel(
            fuel_id, quantity=request.form['new_quantity'])
        flash('Success!', 'success')
    elif request.form['price']:
        FuelInventory().update_fuel(fuel_id, price=request.form['price'])
        flash('Success!', 'success')
    else:
        flash('Enter details!', 'error')
    return redirect(url_for('fuel_inventory_routes.fuel_inventory'))
