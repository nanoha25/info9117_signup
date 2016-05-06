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

# first test

    def test_empty_db(self):
        rv = self.app.get('/')
        assert "No entries here so far" in rv.data


if __name__ == '__main__':
    unittest.main()