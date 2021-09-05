#!/usr/bin/env python3.8
from user import User

def create_user(fname,lname,newname,email,newpassword):
    '''
    Function to create a new user
    '''
    new_user = User(newname,newpassword)
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
    
def find_user(email):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_email(email)

def check_existing_users(email):
    '''
    Function that check if user exists with that email and return a Boolean
    '''
    return User.user_exist(email)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your user list.What is your name?")
    user_username = input()
        
    print(f"Hello {user_username}. What would you like to do?")  
    print('\n')
    
    while True:
        print("use the short codes: cu - create a new user, du - display user, fu - find a user, ex - exit the user list" )
        
        short_code = input().lower()
        
        
        
        
        
        
        
        
        
        if short_code == 'cu':
            print("New User")
            print("_"*50)
            
            print("First name.......")
            f_name = input()
            
            print("Last name........")
            l_name = input()
            
            print("User username.....")
            u_username = input()
            
            print("Email address ......")
            e_address = input()
            
            print("User password......")
            U_password =  input()
            
            
    
    