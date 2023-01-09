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

    def get_employee_hours(self, employee_id=None, employee_hours_id=None):
        cursor = self.conn.cursor()
        if employee_id:
            cursor.execute(
                """
                SELECT e.first_name, e.last_name, h.*
                FROM employee_hours h, employees e
                WHERE employee_id = ?
                """,
                (employee_id,),
            )
            return cursor.fetchall()
        elif employee_hours_id:
            cursor.execute(
                """
                SELECT e.first_name, e.last_name, h.*
                FROM employee_hours h, employees e
                WHERE employee_hours_id = ?
                """,
                (employee_hours_id,),
            )
            return cursor.fetchone()
        else:
            cursor.execute(
                """
                SELECT e.first_name, e.last_name, h.*
                FROM employee_hours h, employees e
                """,
            )
            return cursor.fetchall()

    def insert_employee_hours(self, employee_id, entry_date, hours_worked):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO employee_hours (employee_id, entry_date, hours_worked)
            VALUES (?, ?, ?)
            """,
            (employee_id, entry_date, hours_worked),
        )
        self.conn.commit()

    def delete_employee_hours(self, employee_hours_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            DELETE FROM employee_hours
            WHERE employee_hours_id = ?
            """,
            (employee_hours_id,),
        )
        self.conn.commit()

    def update_employee_hours(self, employee_hours_id, hours_worked, entry_date):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            UPDATE employee_hours
            SET hours_worked = ?, entry_date =?
            WHERE employee_hours_id = ?
            """,
            (hours_worked, entry_date, employee_hours_id),
        )
        self.conn.commit()
