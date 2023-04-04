import re


# Password Strength Checker


def check_strength(password):
    
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."
    
    if not re.search(r'\d', password):
        return "Password should contain at least one digit."
    
    return True
    
