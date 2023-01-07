import bcrypt
from models import database


class Employee(database.Database):

    def init(self):
        super().init()

    def get_all_employees(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM employees
            """
        )
        employees = cursor.fetchall()
        return employees

    def get_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM employees
            WHERE employee_id=?
            """,
            (employee_id,)
        )
        employee = cursor.fetchone()
        return employee

    def add_employee(self, first_name, last_name, phone_number, address, email, job_role, salary):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO employees (first_name, last_name, phone_number, address, email, job_role, salary)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (first_name, last_name, phone_number, address, email, job_role, salary)
        )
        self.conn.commit()

    def delete_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            DELETE FROM employees
            WHERE employee_id=?
            """,
            (employee_id,)
        )
        self.conn.commit()

    def update_employee(self, employee_id, first_name, last_name, phone_number, address, email, job_role, salary):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            UPDATE employees
            SET first_name=?, last_name=?, phone_number=?, address=?, email=?, job_role=?, salary=?
            WHERE employee_id=?
            """,
            (first_name, last_name, phone_number, address,
             email, job_role, salary, employee_id)
        )
        self.conn.commit()
