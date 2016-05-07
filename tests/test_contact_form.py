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

    def test_empty_title_in_form(self):
        rv = self.contact('', 'I have something to say', 'user1@contoso.com')
        assert b'Oh, title is missing >_<' in rv.data


    def test_empty_enquiry_in_form(self):
        rv = self.contact('new enquiry', '', 'user2@contoso.com')
        assert b'So what are you going to tell us ?_?' in rv.data

    def test_invalid_email_in_form_case1(self):
        rv = self.contact('new enquiry', 'I have something to say', 'user2*contoso.com') # email missing "@"
        assert b'Email address is invalid.'

    def test_invalid_email_in_form_case2(self):
        rv = self.contact('new enquiry', 'I have something to say', 'user2@contoso0com') # email with invalid domain name
        assert b'Email address is invalid'

    def test_empty_email_in_form(self):
        rv = self.contact('new enquiry', 'I have something to say', '')
        assert b'So we cannot tell you what we think >_<'

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()