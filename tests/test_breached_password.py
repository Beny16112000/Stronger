from stronger.breached_password import password_breached


# Test Breached Password


def test_password_breached():
    assert password_breached('abcd') == "The password was found in compromised password lists!"


test_password_breached()

