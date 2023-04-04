import random
import string
import re


# Password Generation


def generate_password(sentence):
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', sentence):
        return False
    
    words = sentence.split()
    password = ""
    password += words[0]
    for i in range(1, len(words)):
        if len(words[i]) >= 4:
            password += words[i][:4]
        else:
            password += words[i]
    password += "".join(random.choices(string.digits, k=4))
    
    while len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        password += random.choice(string.ascii_letters + string.digits)

    return password

