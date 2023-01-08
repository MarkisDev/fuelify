from flask import Flask, session, redirect, url_for, render_template
from routes.fuel_inventory import fuel_routes
from routes.auth import auth_routes
from routes.customer import customer_routes
from routes.employee import employee_routes

app = Flask(__name__)
app.secret_key = 'secretKey'

app.register_blueprint(fuel_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(customer_routes)
app.register_blueprint(employee_routes)


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('auth_routes.dashboard'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
