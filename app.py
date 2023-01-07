import uuid
from functools import wraps
from flask import Flask, request, session, redirect, url_for, flash, render_template
from models.user import User
from models.employee import Employee
from models.fuel_inventory import FuelInventory
from models.fuel_purchases import FuelPurchases
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
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username or password')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    user_data = User().get_user_data(user_id)
    employee_data = Employee
    return render_template('dashboard.html', user=user_data)


if __name__ == '__main__':
    app.run(debug=True)
