from lib.password_validator import is_valid


def test_whether_the_program_validates():
    assert is_valid("1234567") == False, "returns false when the password is less than 8 chars"
    assert is_valid("123456789") == False, "returns false when the password does not contain a special character"

    assert is_valid("1234567!") == True, "returns true when the password is 8 characters long and includes '!'"
    assert is_valid("1234567@") == True, "returns true when the password is 8 characters long and includes '@'"