import unittest

def validate_password(password):
    if len(password) < 8:
        return False
    elif password.isdigit():
        return False
    elif password.isalpha():
        return False
    else:
        return True


class TestPasswordValidation(unittest.TestCase):
    '''
        Testing password validation
        to run with each test result printed run:
        `python -m unittest -v W1D4PM-testing.py`
    '''
    def test_valid_password(self):
        self.assertTrue(validate_password('abc123#!'))

    def test_short_password(self):
        self.assertFalse(validate_password('abc123'))

    def test_all_digits(self):
        self.assertFalse(validate_password('12345678'))

    def test_all_letters(self):
        self.assertFalse(validate_password('abcdefgh'))

if __name__ == '__main__':
    unittest.main()