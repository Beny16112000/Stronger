<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<h1>Stronger</h1>
<p>This package provides several features related to password to your application.</p>

<h2>Features</h2>
<ul>
    <li>Password Generation</li>
    <li>Strength Checker</li>
    <li>Suggest Improvements</li>
    <li>Breacher Password</li>
    <li>Multi-factor authentication</li>
    <li>Password Hash</li>
</ul>

<h2>Installation</h2>
<p>To install the package, run the following command:</p>
<code>pip install stronger</code>

<h2>Usage</h2>
<h5>Here's an example of how to use Stronger</h5>

<p>How to use Password-generation:</p>
<code>from stronger.password_generator import generate_password

sentence = "Im Benny and i like pizza"
password = generate_password(sentence)
print(f"Generated password: {password}")
</code>

<p>How to use Strength-checker:</p>
<code>from stronger.strength_checker import check_strength
password = "MySecurePassword123"
strength = your_package_name.check_strength(password)

if strength == True:
    print("Password is strong")
else:
    print(strength)
</code>

<p>How to use Suggest-improvements:</p>
<code>from stronger import check_strength

password = "MyPassw0rd"
strength = check_strength(password)
if strength == True:
    print("Password is strong.")
else:
    print(strength)</code>


<p>How to use Breacher-password:</p>
<code>from stronger import password_breached

password = "MySecurePassword123"
result = password_breached(password)
if result != True:
    print(result)
</code>


<p>How to use Multi-factor-authentication:</p>
<code>import my_package

mfa = my_package.MultiFactorAuth()

otp = mfa.generate_otp()

is_valid = mfa.verify_otp(otp)

if is_valid:
    print("OTP code is valid!")
else:
    print("OTP code is not valid.")
</code>


<p>How to use Password-hash:</p>
<code>from hashpassword import HashPassword

hp = HashPassword()

hashed_password, salt = hp.hash_password('my_password')

result = hp.verify_password('my_password', salt, hashed_password)

if result:
    print("Password is valid.")
else:
    print("Password is invalid.")
</code>


<h2>Contributing</h2>
<p>Contributions are welcome. Please submit a pull request to contribute to this project.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>
</body>
</html>
