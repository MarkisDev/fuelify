from models.database import Database


class Insights(Database):

    def total_sales_month(self, employee_id=None):
        
        if employee_id:
            cursor = self.execute(
                """
                SELECT SUM(price)
                FROM fuel_purchases
                WHERE employee_id = ? AND strftime('%m', purchase_date) = strftime('%m', 'now')
                """,
                (employee_id,)
            )
            return cursor.fetchone()
        else:
            cursor = self.execute(
                """
                SELECT SUM(price)
                FROM fuel_purchases
                WHERE strftime('%m', purchase_date) = strftime('%m', 'now')
                """)
            return cursor.fetchone()

    def avg_sales(self, employee_id=None):
        
        if employee_id:
            cursor = self.execute(
                """
                SELECT AVG(price)
                FROM fuel_purchases
                WHERE employee_id = ?
                """,
                (employee_id,)
            ),
            return cursor.fetchone()
        else:
            cursor = self.execute(
                """
                SELECT AVG(price)
                FROM fuel_purchases
                """
            ),
            return cursor.fetchone()

    def total_hours_worked_week(self, employee_id):
        
        cursor = self.execute(
            """
            SELECT SUM(hours_worked)
            FROM employee_hours
            WHERE employee_id = ?
            AND strftime('%W', entry_date) = strftime('%W', 'now')
            """,
            (employee_id,)
        )
        return cursor.fetchone()

    def avg_hours_worked_day(self, employee_id):
        
        cursor = self.execute(
            """
            SELECT AVG(hours_worked)
            FROM employee_hours
            WHERE employee_id = ?
            """,
            (employee_id,)
        )
        return cursor.fetchone()

    def top_performing_employee(self):
        
        cursor = self.execute(
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
        
        cursor = self.execute(
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

    def total_money_spent(self, customer_id):
        
        cursor = self.execute(
            """
                SELECT SUM(p.price)
                FROM fuel_purchases p
                WHERE p.customer_id = ?
                """,
            (customer_id,)
        )
        return cursor.fetchone()[0]

    def avg_fuel_purchase(self, customer_id):
        
        cursor = self.execute(
            """
            SELECT AVG(p.quantity)
            FROM fuel_purchases p
            WHERE p.customer_id = ?
            """,
            (customer_id,)
        )
        return cursor.fetchone()[0]

    def frequent_fuel_type(self, customer_id):
        
        cursor = self.execute(
            """
            SELECT f.fuel_type, SUM(p.quantity) as 'total_purchased'
            FROM fuel_purchases p
            JOIN fuel_inventory f ON p.fuel_id = f.fuel_id
            WHERE p.customer_id = ?
            GROUP BY f.fuel_type
            ORDER BY total_purchased DESC
            LIMIT 1
            """,
            (customer_id,)
        )
        return cursor.fetchone()

    def top_performing_employee(self):
        
        cursor = self.execute(
            """
            SELECT e.first_name, e.last_name, SUM(p.quantity) as 'total_sold'
            FROM fuel_purchases p
            JOIN employees e ON p.employee_id = e.employee_id
            GROUP BY e.first_name, e.last_name
            ORDER BY total_sold DESC
            LIMIT 1
            """
        )
        return cursor.fetchone()

    def popular_fuel_type(self):
        
        cursor = self.execute(
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

    def avg_purchase_quantity(self):
        
        cursor = self.execute(
            """
            SELECT AVG(quantity) as 'avg_quantity'
            FROM fuel_purchases
            """
        )
        return cursor.fetchone()
