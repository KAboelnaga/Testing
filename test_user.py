import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('test', 'test')

    def test_name(self):
        self.assertEqual(self.user.get_name(), 'test')
    
    def test_name_change(self):
        self.user.set_name('test2')
        self.assertEqual(self.user.get_name(), 'test2')
    
    def test_email(self):
        self.assertEqual(self.user.get_email(), 'test')
    
    def test_email_change(self):
        self.user.set_email('test2')
        self.assertEqual(self.user.get_email(), 'test2')
    

if __name__ == '__main__':
    unittest.main()
    
    