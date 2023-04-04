import random
import string


# Suggest Password Improvements


def improvements_suggest(password):

    improvements = []

    if len(password) < 8:
        improvements.append("Password should be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        improvements.append("Password should contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        improvements.append("Password should contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        improvements.append("Password should contain at least one digit.")

    if len(improvements) == 0:
        return True
    
    else:
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        new_password = password + random_chars
        improvements.append(new_password)

        return improvements
    
