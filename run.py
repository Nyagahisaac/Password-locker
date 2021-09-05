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
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(username):
    '''
    Function that check if user exists with that username and return a Boolean
    '''
    return User.user_exist(username)
