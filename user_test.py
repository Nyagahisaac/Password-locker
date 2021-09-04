import unittest 
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class  defies test cases for the user class behaviours
    
    Args:
    unittest.Testcase:Test case that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Izooh The Duke","124vg3 sdx")
        
    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
    
        '''
        self.assertEqual(self.new_user.username,"Izooh The Duke")
        self.assertEqual(self.new_user.password,"2434tfdg8")
        
    
if __name__ == '__main__':
    unittest.main()    