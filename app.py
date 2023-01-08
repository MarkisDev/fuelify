from flask import Flask, session, redirect, url_for, render_template
from routes.fuel_inventory import fuel_routes
from routes.auth import auth_routes
from helpers.utils import login_required

app = Flask(__name__)
app.secret_key = 'secretKey'

app.register_blueprint(fuel_routes)
app.register_blueprint(auth_routes)


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('auth_routes.dashboard'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
