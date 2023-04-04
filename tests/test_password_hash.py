from stronger.password_hash import HashPassword


# Test Password Hash


def test_hash_password():
    hasher = HashPassword()

    hashed_password, salt = hasher.hash_password('Abcde1234')

    assert hasher.verify_password('wrong_password', salt, hashed_password) == False


test_hash_password()

