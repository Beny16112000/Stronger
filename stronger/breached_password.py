import requests
import hashlib


# Check Breached Password


def password_breached(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Error fetching breached passwords")
    for line in response.content.decode('utf-8').splitlines():
        line_suffix, count = line.split(':')
        if line_suffix == suffix:
            return "The password was found in compromised password lists!"
    return True

