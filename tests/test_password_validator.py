from lib.password_validator import is_valid


def test_whether_the_program_validates():
    assert is_valid("1234567") == False, "returns false when the password is less than 8 chars"