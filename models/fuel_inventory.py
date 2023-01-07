from database import Database


class FuelInventory(Database):

    def create_fuel(self, fuel_type, quantity):
        self.execute(
            """
            INSERT INTO fuel_inventory (fuel_type, quantity)
            VALUES (?, ?)
            """,
            (fuel_type, quantity)
        )

    def get_fuel(self, fuel_id=None):
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

    def update_fuel(self, fuel_id, fuel_type=None, quantity=None):
        if fuel_type:
            self.execute(
                """
                UPDATE fuel_inventory
                SET fuel_type = ?
                WHERE fuel_id = ?
                """,
                (fuel_type, fuel_id)
            )
        if quantity:
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
