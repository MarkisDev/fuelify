
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

    def update(self, purchase_id, employee_id, customer_id, fuel_id, quantity, price, purchase_date):
        self.execute(
            """
            UPDATE fuel_purchases
            SET employee_id=?, customer_id=?, fuel_id=?, quantity=?, price=?, purchase_date=?
            WHERE purchase_id=?
            """,
            (employee_id, customer_id, fuel_id,
             quantity, price, purchase_date, purchase_id)
        )

    def delete(self, purchase_id):
        self.execute(
            """
            DELETE FROM fuel_purchases
            WHERE purchase_id=?
            """,
            (purchase_id,)
        )

    def get(self, purchase_id=None):
        if purchase_id:
            cursor = self.execute(
                """
                SELECT p.purchase_id, e.first_name, e.last_name, c.first_name, c.last_name, f.fuel_type, p.quantity, p.price, p.purchase_date
                FROM fuel_purchases p
                JOIN employees e ON p.employee_id = e.employee_id
                JOIN customer_information c ON p.customer_id = c.customer_id
                JOIN fuel_inventory f ON p.fuel_id = f.fuel_id
                WHERE p.purchase_id = ?
                """,
                (purchase_id,)
            )
            return cursor.fetchone()
        else:
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
