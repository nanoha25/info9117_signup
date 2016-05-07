import os
import flaskr_win
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr_win.app.config['DATABASE_WIN'] = tempfile.mkstemp() # what does db_fd mean and what is mkstemp()?
        flaskr_win.app.config['TESTING'] = True
        self.app = flaskr_win.app.test_client()
        flaskr_win.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr_win.app.config['DATABASE_WIN'])

# first test

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data

# logging in and out

def login(self, username, password):
    return self.app.post('/login', data=dict
    (
        username = username,
        password = password
    ), follow_redirects=True)

def logout(self):
    return self.app.get('/logout', follow_redirects=True)

def test_login_logout(self):
    rv = self.login('admin', 'default')
    assert 'You are logged in' in rv.data
    rv = self.logout()
    assert 'You were logged out' in rv.data
    rv = self.login('nanoha', 'default')
    assert 'Invalid username' in rv.data
    rv = self.login('admin', 'nanoha')
    assert 'Invalid password' in rv.data

# test adding messages

def test_messages(self):
    self.login('admin', 'default')
    rv = self.app.post('/add', data=dict
    (
        title='<Hello>',
        text='<strong>なのは</strong> allowed here'
    ), follow_redirects=True)
    assert 'No entires here so far' not in rv.data
    assert '&lt;Hello&gt;' in rv.data
    assert '<strong>なのは</strong> allowed here' in rv.data


if __name__ == '__main__':
    unittest.main()