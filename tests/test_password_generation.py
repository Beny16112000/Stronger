from stronger.password_generation import generate_password


# Test Password Generation


def test_generate_password():
    assert generate_password('Hello i am benny and i like @') == False


test_generate_password()

