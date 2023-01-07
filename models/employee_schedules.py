from models.database import Database


class EmployeeSchedules(Database):
    def __init__(self):
        super().__init__()

    def create(self, employee_id, start_time, end_time):
        self.execute(
            """
            INSERT INTO employee_schedules (employee_id, start_time, end_time)
            VALUES (?, ?, ?)
            """,
            (employee_id, start_time, end_time)
        )

    def update(self, employee_id, start_time, end_time):
        self.execute(
            """
            UPDATE employee_schedules
            SET start_time = ?, end_time = ?
            WHERE employee_id = ?
            """,
            (start_time, end_time, employee_id)
        )

    def delete(self, employee_id):
        self.execute(
            """
            DELETE FROM employee_schedules
            WHERE employee_id = ?
            """,
            (employee_id,)
        )

    def get_all(self):
        cursor = self.execute(
            """
            SELECT e.employee_id, e.first_name, e.last_name, s.start_time, s.end_time
            FROM employee_schedules s
            JOIN employees e ON s.employee_id = e.employee_id
            """
        )
        return cursor.fetchall()

    def get_by_employee_id(self, employee_id):
        cursor = self.execute(
            """
            SELECT e.employee_id, e.first_name, e.last_name, s.start_time, s.end_time
            FROM employee_schedules s
            JOIN employees e ON s.employee_id = e.employee_id
            WHERE e.employee_id = ?
            """,
            (employee_id,)
        )
        return cursor.fetchone()
