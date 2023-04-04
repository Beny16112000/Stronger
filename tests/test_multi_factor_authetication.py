from stronger.multi_factor_authetication import MultiFactorAuth


# Test Multi Factor Authentication


def test_multi_factor_auth():
    mfa = MultiFactorAuth()
    otp = mfa.generate_otp()
    assert mfa.verify_otp('123456') == False
    assert mfa.verify_otp(otp) == True


test_multi_factor_auth()

