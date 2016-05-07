import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp() # what does db_fd mean and what is mkstemp()?
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])


def test_signup_as_a_new_user(self):
    rv = self.signup('newuser', 'newpassword', 'user1@contoso.com')
    assert b'Yay! You are now a member here.^_^' in rv.data


def test_signup_as_an_existed_user(self):
    rv = self.signup('newuser', 'password', 'user2@contoso.com')
    assert b'Sorry, this name has been used.-_-' in rv.data


def test_signup_with_an_used_email(self):
    rv = self.signup('anotheruser', 'password', 'user1@contoso.com')
    assert b'Sorry, email has been registered.-_-' in rv.data


def test_signup_with_mixed_cases_name(self):
    rv = self.signup('NewUsertwo', 'newpassword', 'user3@contoso.com')
    assert b'Yay! You are now a member here.^_^' in rv.data


def test_signup_with_mixed_cases_password(self):
    rv = self.signup('newuserthree', 'NEWPASSword', 'user4@contoso.com')
    assert b'Yay! You are now a member here.^_^' in rv.data


def test_signup_with_invalid_email_case1(self):
    rv = self.signup('newuserfour', 'newpassword', 'user5!contoso.com') # email miss "@"
    assert b'Sorry. Email should be something like "example@example.com"' in rv.data


def test_signup_with_invalid_email_case2(self):
    rv = self.signup('newuserfive', 'newpassword', 'user6@contoso0com') # email with incorrect domain name
    assert b'Sorry. Email should be something like "example@example.com"' in rv.data


def test_signup_password_only_have_digits(self):
    rv = self.signup('newusersix', '0123456789', 'user7@contoso.com')
    assert b'Sorry. Password too weak.' in rv.data


def test_signup_password_too_short_case1(self):
    rv = self.signup('newuserseven','pswd', 'user8@contoso.com') # password only have 4 characters
    assert b'Sorry. Password too short.' in rv.data


def test_signup_password_too_short_case2(self):
    rv = self.signup('newusereight','pswd123', 'user9@contoso.com') # password only have 7 characters
    assert b'Sorry. Password too short.' in rv.data


if __name__ == '__main__':
    unittest.main()