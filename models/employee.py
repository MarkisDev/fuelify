import bcrypt
from models.database import Database


class Employee(Database):

    def get(self, employee_id=None):
        cursor = self.conn.cursor()
        if employee_id:
            cursor.execute(
                """
                SELECT *
                FROM employees
                WHERE employee_id=?
                """,
                (employee_id,)
            )
            return cursor.fetchone()
        else:
            cursor.execute(
                """
                SELECT *
                FROM employees
                """
            )
        return cursor.fetchall()

    def create(self, first_name, last_name, phone_number, address, email, job_role, salary):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO employees (first_name, last_name, phone_number, address, email, job_role, salary)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (first_name, last_name, phone_number, address, email, job_role, salary)
        )
        self.conn.commit()

    def delete(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            DELETE FROM employees
            WHERE employee_id=?
            """,
            (employee_id,)
        )
        self.conn.commit()

    def update(self, employee_id, first_name, last_name, phone_number, address, email, job_role, salary):
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
