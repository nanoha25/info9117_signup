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
        assert "No entries here so far" in rv.data


if __name__ == '__main__':
    unittest.main()