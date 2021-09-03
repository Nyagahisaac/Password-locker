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
        
        