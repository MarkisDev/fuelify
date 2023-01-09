from flask import Flask, session, redirect, url_for, render_template, request
from models.database import Database
from routes.fuel_inventory import fuel_inventory_routes
from routes.fuel_purchases import fuel_purchases_routes
from routes.auth import auth_routes
from routes.customer import customer_routes
from routes.employee import employee_routes
from routes.insights import insights_routes
from routes.admin import admin_routes


app = Flask(__name__)
app.secret_key = 'secretKey'

app.register_blueprint(fuel_inventory_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(customer_routes)
app.register_blueprint(employee_routes)
app.register_blueprint(fuel_purchases_routes)
app.register_blueprint(insights_routes)
app.register_blueprint(admin_routes)


@app.route('/')
def index():
    logged_in = False
    role = None
    if 'username' in session:
        logged_in = True
        role = session['role']
    return render_template('index.html', request_path=request.path, logged_in=logged_in, role=role)


@app.route('/home')
def home():
    return index()


if __name__ == '__main__':
    app.run(debug=True)
