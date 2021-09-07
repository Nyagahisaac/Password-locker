import unittest 
from user import User
from credentials import Credentials

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
        self.new_user = User("Nyagah","isaac","Izooh The Duke","nyagahisaac21@gmail.com","124vg3 sdx")
        
    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
    
        '''
        self.assertEqual(self.new_user.firstname,"Nyagah")
        self.assertEqual(self.new_user.lastname,"isaac")
        self.assertEqual(self.new_user.username,"Izooh The Duke")
        self.assertEqual(self.new_user.email,"nyagahisaac21@gmail.com")
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
        test_user = User("Nyagah","isaac","james","nyagahisaac21@gmail","pass1234") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
    def tearDown(self):
        '''
        tearDown method cleans up after each test case has run
        '''
        User.user_list = []
        
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user object to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Nyagah","isaac","james","nyagahisaac21@gmail.com","pass1234")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Nyagah","isaac","james","nyagahisaac@gmail.com","pass1234")
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
  
  
    
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''
        self.new_user.save_user()
        test_user = User("Nyagah","isaac","james","nyagahisaac@gmail.com","pass1234")
        test_user.save_user()
        
        found_user = User.find_by_username("james")
        
        self.assertEqual(found_user.username,test_user.username)
      
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user.
        '''
        self.new_user.save_user()  
        test_user = User("Nyagah","isaac","james","nyagahisaac@gmail.com","pass1234")
        test_user.save_user()
        
        user_exists = User.user_exist("james")
        
        self.assertTrue(user_exists)
  

    
class TestCredentials(unittest.TestCase):
    '''
    Test class  defies test cases for the user class behaviours
    
    Args:
    unittest.Testcase:Test case that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Twitter","Izooh The Duke","nyagahisaac21@gmail.com","twitter1234")
        
    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
    
        '''
       
        self.assertEqual(self.new_credentials.handle,"Twitter")
        self.assertEqual(self.new_credentials.username,"Izooh The Duke")
        self.assertEqual(self.new_credentials.email,"nyagahisaac21@gmail.com")
        self.assertEqual(self.new_credentials.password,"twitter1234")
    
    def test_save_credentials(self):
        '''
        test_save_credentials testcase to set if the the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credentials_list
        '''
        self.new_credentials.test_save_credentials()
        test_credentials = Credentials("Twitter","james","nyagahisaac21@gmail","pass1234") 
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def tearDown(self):
        '''
        tearDown method cleans up after each test case has run
        '''
        Credentials.credential_list = []
  
    
    def test_delete_credentials(self):
        '''
        test_delete_user to test if we can remove a credentials from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","james","nyagahisaac@gmail.com","pass1234")
        test_credentials.save_credentials()
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)
  
  
    
    def test_find_user_by_username(self):
        '''
        test to check if we can find a credentials by username and display information
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","james","nyagahisaac@gmail.com","pass1234")
        test_credentials.save_credentials()
        
        found_credentials = Credentials.find_by_username("james")
        
        self.assertEqual(found_credentials.username,test_credentials.username)
      
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the credentials.
        '''
        self.new_credentials.save_credentials()  
        test_credentials = Credentials("Twitter","james","nyagahisaac@gmail.com","pass1234")
        test_credentials.save_credentials()
        
        credentials_exists = Credentials.credentials_exist("james")
        
        self.assertTrue(user_exists)
            
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)  

        
if __name__ == '__main__':
    unittest.main()    