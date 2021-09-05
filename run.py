#!/usr/bin/env python3.8
from user import User

def create_user(newusername,newpassword):
    '''
    Function to create a new user
    '''
    new_user = User(newusername,newpassword)
    return new_user
    
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
    
