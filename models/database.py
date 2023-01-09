import sqlite3
import bcrypt


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('fuelify.db')

        # Create employees table if it does not exist
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                phone_number VARCHAR(255),
                address VARCHAR(255),
                email VARCHAR(255),
                job_role VARCHAR(255),
                salary FLOAT
            )
            """
        )

    # Create employee_schedules table if it does not exist
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS employee_hours (
                employee_hours_id INTEGER PRIMARY KEY,
                employee_id INTEGER,
                hours_worked FLOAT,
                entry_date DATE,
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
            )
            """
        )

        # Create user_accounts table if it does not exist
        self.execute(
            """
                CREATE TABLE IF NOT EXISTS user_accounts (
                    user_id INTEGER PRIMARY KEY,
                    employee_id INTEGER,
                    username VARCHAR(255),
                    password VARCHAR(255),
                    role VARCHAR(255),
                    FOREIGN KEY(employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
                )
                """
        )

        # Create fuel_inventory table if it does not exist
        self.execute(
            """
                CREATE TABLE IF NOT EXISTS fuel_inventory (
                    fuel_id INTEGER PRIMARY KEY,
                    fuel_type VARCHAR(255),
                    quantity FLOAT,
                    price FLOAT
                )
                """
        )
        # Create customer_information table if it does not exist
        self.execute(
            """
                CREATE TABLE IF NOT EXISTS customer_information (
                    customer_id INTEGER PRIMARY KEY,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    phone_number VARCHAR(255),
                    email VARCHAR(255)
                )
                """
        )

        # Create fuel_purchases table if it does not exist
        self.execute(
            """
                CREATE TABLE IF NOT EXISTS fuel_purchases (
                    purchase_id INTEGER PRIMARY KEY,
                    employee_id INTEGER,
                    customer_id INTEGER,
                    fuel_id INTEGER,
                    quantity INTEGER,
                    price FLOAT,
                    purchase_date DATE,
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE, 
                FOREIGN KEY (customer_id) REFERENCES customer_information(customer_id) ON DELETE CASCADE,
                FOREIGN KEY (fuel_id) REFERENCES fuel_inventory(fuel_id) ON DELETE CASCADE
                )
                """
        )
        # Create trigger to update fuel quantity
        self.execute(
            """
                CREATE TRIGGER IF NOT EXISTS update_fuel_quantity AFTER INSERT ON fuel_purchases
                BEGIN
                    UPDATE fuel_inventory SET quantity = quantity - NEW.quantity
                    WHERE fuel_id = NEW.fuel_id;
                END;
            """
        )
        self.create_employee_and_user('Rijuth', 'Menon', '8217784182', 'Pai Layout',
                                      'rijuthm@gmail.com', 'owner', 00.00,  'admin', 'admin@password', 'Owner')

    def create_employee_and_user(self, first_name, last_name, phone_number, address, email, job_role, salary, username, password, role):

        cursor = self.execute("SELECT COUNT(*) FROM user_accounts")
        if cursor.fetchone()[0] == 0:
            # Create employee
            self.execute(
                """
                    INSERT INTO employees (first_name, last_name, phone_number, address, email, job_role, salary)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                (first_name, last_name, phone_number,
                 address, email, job_role, salary)
            )

            # Get employee_id of newly created employee
            cursor = self.execute(
                "SELECT employee_id FROM employees ORDER BY employee_id DESC LIMIT 1"
            )
            employee_id = cursor.fetchone()[0]

            # Create user account linked to employee
            hashed_password = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt())
            self.execute(
                """
                    INSERT INTO user_accounts (employee_id, username, password, role)
                    VALUES (?, ?, ?, ?)
                    """,
                (employee_id, username, hashed_password, role)
            )

    def execute(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor
