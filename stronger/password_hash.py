import hashlib
import os


# Password Hash


class HashPassword:

    def __init__(self):
        self.salt = os.urandom(16)


    def hash_password(self, password):
        salted_password = self.salt + password.encode('utf-8')
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return (hashed_password, self.salt)


    def verify_password(self, password, salt, hashed_password):
        salted_password = salt + password.encode('utf-8')
        new_hashed_password = hashlib.sha256(salted_password).hexdigest()
        if new_hashed_password == hashed_password:
            return True
        else:
            return False

