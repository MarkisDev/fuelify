from models.database import Database


class Insights(Database):

    def total_sales_month(self, employee_id=None):
        cursor = self.conn.cursor()
        if employee_id:
            cursor.execute(
                """
                SELECT SUM(price)
                FROM fuel_purchases
                WHERE employee_id = ? AND strftime('%m', purchase_date) = strftime('%m', 'now')
                """,
                (employee_id,)
            )
            return cursor.fetchone()
        else:
            cursor.execute(
                """
                SELECT SUM(price)
                FROM fuel_purchases
                WHERE strftime('%m', purchase_date) = strftime('%m', 'now')
                """)
            return cursor.fetchone()

    def avg_sales(self, employee_id=None):
        cursor = self.conn.cursor()
        if employee_id:
            cursor.execute(
                """
                SELECT AVG(price)
                FROM fuel_purchases
                WHERE employee_id = ?
                """,
                (employee_id,)
            ),
            return cursor.fetchone()
        else:
            cursor.execute(
                """
                SELECT AVG(price)
                FROM fuel_purchases
                """
            ),
            return cursor.fetchone()

    def total_hours_worked_week(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT SUM(hours_worked)
            FROM employee_hours
            WHERE employee_id = ?
            AND strftime('%W', date) = strftime('%W', 'now')
            """,
            (employee_id,)
        )
        return cursor.fetchone()

    def avg_hours_worked_day(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT AVG(hours_worked)
            FROM employee_hours
            WHERE employee_id = ?
            """,
            (employee_id,)
        )
        return cursor.fetchone()

    def top_performing_employee(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT e.first_name, e.last_name, SUM(p.price) as 'sales'
            FROM fuel_purchases p
            JOIN employees e ON p.employee_id = e.employee_id
            GROUP BY e.employee_id
            ORDER BY sales DESC
            LIMIT 1
            """
        )
        return cursor.fetchone()

    def top_selling_fuel(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
        SELECT f.fuel_type, SUM(p.quantity) as 'total_sold'
        FROM fuel_purchases p
        JOIN fuel_inventory f ON p.fuel_id = f.fuel_id
        GROUP BY f.fuel_type
        ORDER BY total_sold DESC
        LIMIT 1
        """
        )
        return cursor.fetchone()

    def number_of_transations(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
        SELECT COUNT(*)
        FROM fuel_purchases
        """
        )
        return cursor.fetchone()
