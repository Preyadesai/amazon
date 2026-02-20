import hashlib
from storage import Storage

class UserManager:
    FILE = "users.json"

    def __init__(self):
        self.users = Storage.load(self.FILE)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def username_exists(self, username):
        return any(u["username"] == username for u in self.users)

    def register(self, username, password):
        if self.username_exists(username):
            return False, "Username already exists."
        if len(password) < 6:
            return False, "Password must be at least 6 characters."
        self.users.append({
            "username": username,
            "password": self.hash_password(password)
        })
        Storage.save(self.FILE, self.users)
        return True, "Registration successful."

    def login(self, username, password):
        hashed = self.hash_password(password)
        for user in self.users:
            if user["username"] == username and user["password"] == hashed:
                return True
        return False