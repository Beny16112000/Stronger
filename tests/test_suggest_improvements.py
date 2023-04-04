from stronger.suggest_improvements import improvements_suggest


# Test Suggest Password Improvements


def test_improvements_suggest():
    assert improvements_suggest('Abcd1234') == True
    assert improvements_suggest('Abc123')[0] == "Password should be at least 8 characters long."
    assert improvements_suggest('abcde1234')[0] == "Password should contain at least one uppercase letter."
    assert improvements_suggest('ABCDE1234')[0] == "Password should contain at least one lowercase letter."
    assert improvements_suggest('Abcdefgeh')[0] == "Password should contain at least one digit."


test_improvements_suggest()

