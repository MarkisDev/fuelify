
from models.database import Database


class FuelPurchases(Database):
    def create(self, employee_id, customer_id, fuel_id, quantity, price, purchase_date):
        self.execute(
            """
            INSERT INTO fuel_purchases (employee_id, customer_id, fuel_id, quantity, price, purchase_date)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (employee_id, customer_id, fuel_id, quantity, price, purchase_date)
        )

    def get_all(self):
        cursor = self.execute(
            """
            SELECT p.purchase_id, e.first_name, e.last_name, c.first_name, c.last_name, f.fuel_type, p.quantity, p.price, p.purchase_date
            FROM fuel_purchases p
            JOIN employees e ON p.employee_id = e.employee_id
            JOIN customer_information c ON p.customer_id = c.customer_id
            JOIN fuel_inventory f ON p.fuel_id = f.fuel_id
            """
        )
        return cursor.fetchall()
