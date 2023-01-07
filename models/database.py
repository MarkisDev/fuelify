import sqlite3


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
        CREATE TABLE IF NOT EXISTS employee_schedules (
            employee_id INTEGER PRIMARY KEY,
            start_time DATE,
            end_time DATE,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
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
                FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
            )
            """
    )

    # Create fuel_inventory table if it does not exist
    self.execute(
        """
            CREATE TABLE IF NOT EXISTS fuel_inventory (
                fuel_id INTEGER PRIMARY KEY,
                fuel_type VARCHAR(255),
                quantity FLOAT
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
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
            FOREIGN KEY (customer_id) REFERENCES customer_information(customer_id),
            FOREIGN KEY (fuel_id) REFERENCES fuel_inventory(fuel_id)
            )
            """
    )

    def execute(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor
