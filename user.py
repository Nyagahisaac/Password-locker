class User:
    '''
    Class that generates new instance users
    '''
    pass

    user_list = []
    
    def __init__(self,firstname,lastname,username,email,password):
        '''
        __init__ method helps us define properties for our objects.
        
        Args:
        firstname : New user firstname.
        lastname : New user lastname.
        username : New user username.
        emil : New user email.
        password :New user password.
        '''
        
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        
    def save_user(self):
        
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
        
    def delete_user(self):
        
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
        
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.
        
        Args:
            username: User's to search for
        Return:
            User of person that matches the username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user
            
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        
        Args:
            username:User's to search if it exists 
        Returns:
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
            
        return False 
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list