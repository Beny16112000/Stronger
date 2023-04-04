from stronger.strength_checker import check_strength


# Test Password Strength Checker


def test_check_strength():
    assert check_strength('Abcdefg123') == True
    assert check_strength('abc123') == "Password is too short. It should be at least 8 characters long."
    assert check_strength('abcdefgh') == "Password should contain at least one uppercase letter."
    assert check_strength('ABCDEFGH') == "Password should contain at least one lowercase letter."


test_check_strength()

