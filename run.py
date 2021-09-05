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
            
            save_user(create_user(f_name,l_name,u_username,e_address,U_password))
            
            print('\n')
            print(f"New user {f_name}{l_name} created")
            print('\n')
            
        elif short_code == 'dc':
            
            if display_users():
            print("Here is a list of all your users")
            print('\n')
            
                for user in display_users():
                    print(f"{user.first_name} {user.last_name} {user.email}")
                    
            
            else:
                print('\n')
                print("You dont seem to hve any account saved yet")
                print('\n')
                    
        elif short_code == 'fc':
        
            print("Enter the email you want to serach for")
            
            search_email = input()
            if check_existing_users(search_email):
                search_email = find_user(search_email)
                print(f"{search_email.first_name} {search_email.last_name}")
                print('_'*20)
                
                print(f"username .....{search_email.username}")
                
                print(f"password......{search_email.password}")
        
            else:
                print("Tht user does not exist")
            
        elif short_code == "ex":
            print("Bye .......")
            break
        
        else:
            print("I really didn't get that. PLease use the short codes")
        
    
        
    
    
            
    