from models.database import Database


class Customer(Database):

    def create(self, first_name, last_name, phone_number, email):
        self.execute(
            """
            INSERT INTO customer_information (first_name, last_name, phone_number, email)
            VALUES (?, ?, ?, ?)
            """,
            (first_name, last_name, phone_number, email)
        )

    def get(self, customer_id=None):

        if customer_id:
            cursor = self.execute(
                """
                SELECT * FROM customer_information
                WHERE customer_id = ?
                """,
                (customer_id,)
            )
            return cursor.fetchone()
        else:
            cursor = self.execute(
                """
                SELECT * FROM customer_information
                """
            )
            return cursor.fetchall()

    def update(self, customer_id, first_name, last_name, phone_number, email):
        self.execute(
            """
            UPDATE customer_information
            SET first_name = ?, last_name = ?, phone_number = ?, email = ?
            WHERE customer_id = ?
            """,
            (first_name, last_name, phone_number, email, customer_id)
        )

    def delete(self, customer_id):
        self.execute(
            """
            DELETE FROM customer_information
            WHERE customer_id = ?
            """,
            (customer_id,)
        )
