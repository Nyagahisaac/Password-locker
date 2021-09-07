class Credentials:
    '''
    Class that generates new instance credentials
    '''
    pass

    credentials_list = []
    
    def __init__(self,handle,username,email,password):
        '''
        __init__method helps us define properties for our objects.
        
        Args:
        handle : New credentials handle.
        username : New credentials username.
        emil : New credentials email.
        password :New credentials password.
        '''
        
        self.handle = handle
        self.username = username
        self.email = email
        self.password = password
        
    def save_credentials(self):
        
        '''
        save_user method sves usetobject into credential_list
        '''
        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        
        '''
        delete_user method deletes a saved user from the credential_list
        '''
        
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def credentials_exist(cls,username):
        '''
        Method that checks if a user exists from the credentials list.
        
        Args:
            username:Credentials to search if it exists 
        Returns:
            Boolean: True or false depending if the user exists
        '''
        for user in cls.credentials_list:
            if user.username == username:
                return True
            
        return False 

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credetial list
        '''
        return cls.credentials_list   
    