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
        self.assertEqual(self.new_user.password,"124vg3 sdx")
    
    def test_save_user(self):
        '''
        test_save_user testcase to set if the the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("username","password") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
    
    
if __name__ == '__main__':
    unittest.main()    