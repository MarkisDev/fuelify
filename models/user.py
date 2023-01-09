import bcrypt
from models.database import Database


class User(Database):
    def validate_login(self, username, password):
        cursor = self.execute(
            'SELECT * FROM user_accounts WHERE username=?',
            (username,)
        )
        user = cursor.fetchone()
        if user:
            hashed_password = user[3]
            if bcrypt.checkpw(password.encode(), hashed_password):
                return user
            else:
                return None
        else:
            return None

    def get_user_data(self, user_id=None):
        if user_id:
            cursor = self.execute(
                """
                SELECT * FROM user_accounts u, employees e 
                WHERE u.employee_id=e.employee_id AND user_id = ?
                """,
                (user_id,)
            )
            return cursor.fetchone()
        else:
            cursor = self.execute(
                """
                SELECT * FROM user_accounts u, employees e 
                WHERE u.employee_id=e.employee_id
                """,
            )
            return cursor.fetchall()

    def add_user(self, employee_id, username, password, role):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.execute(
            'INSERT INTO user_accounts (employee_id, username, password, role) VALUES (?, ?, ?, ?)',
            (employee_id, username, hashed_password, role)
        )

    def update_user(self, user_id, employee_id, username, password, role):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.execute(
            'UPDATE user_accounts SET employee_id=?, username=?, password=?, role=? WHERE user_id=?',
            (employee_id, username, hashed_password, role, user_id)
        )

    def delete_user(self, user_id):
        self.execute(
            'DELETE FROM user_accounts WHERE user_id=?',
            (user_id,)
        )
