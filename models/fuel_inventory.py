from models.database import Database


class FuelInventory(Database):

    def create_fuel(self, fuel_type, quantity, price):
        self.execute(
            """
            INSERT INTO fuel_inventory (fuel_type, quantity, price)
            VALUES (?, ?, ?)
            """,
            (fuel_type, quantity, price)
        )

    def get(self, fuel_id=None):
        if fuel_id:
            cursor = self.execute(
                """
                SELECT * FROM fuel_inventory
                WHERE fuel_id = ?
                """,
                (fuel_id,)
            )
            return cursor.fetchone()
        else:
            cursor = self.execute(
                """
                SELECT * FROM fuel_inventory
                """
            )
            return cursor.fetchall()

    def update_fuel(self, fuel_id, price=None, quantity=None):
        if price and quantity:
            self.execute(
                """
                UPDATE fuel_inventory
                SET price = ?, quantity = ?
                WHERE fuel_id = ?
                """,
                (price, quantity, fuel_id)
            )
        elif price:
            self.execute(
                """
                UPDATE fuel_inventory
                SET price = ?
                WHERE fuel_id = ?
                """,
                (price, fuel_id)
            )
        elif quantity:
            self.execute(
                """
                UPDATE fuel_inventory
                SET quantity = ?
                WHERE fuel_id = ?
                """,
                (quantity, fuel_id)
            )

    def delete_fuel(self, fuel_id):
        self.execute(
            """
            DELETE FROM fuel_inventory
            WHERE fuel_id = ?
            """,
            (fuel_id,)
        )
