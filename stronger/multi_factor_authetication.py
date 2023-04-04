import pyotp


# Multi Factor Authentication


class MultiFactorAuth:

    def __init__(self, secret_key=None):
        if secret_key is None:
            self.secret_key = pyotp.random_base32()
        else:
            self.secret_key = secret_key

    
    def generate_otp(self):
        totp = pyotp.TOTP(self.secret_key)
        return totp.now()
    

    def verify_otp(self, otp):
        totp = pyotp.TOTP(self.secret_key)
        return totp.verify(otp)
    
