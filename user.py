class User:
    '''
    Class that generates new instance users
    '''
    pass

    user_list = []
    
    def __init__(self,username,password):
        '''
        __init__ method helps us define properties for our objects.
        
        Args:
        username : New user username.
        password :New user password.
        '''
        self.username = username
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