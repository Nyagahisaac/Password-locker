# Password Locker
Built By Nyagah Isaac

# Description

Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts and handles.

# User Stories

These are the behaviours/features that the application implements for use by a user.

## As a user I would like:

    To create an account with my credentials - log in and password
    Store my existing login credentials
    Generate a password for a new credential/account
    Delete my credentials incase i wannah make changes.

## Specifications

# Behaviour 	#Input 	#Output
Display codes for navigation 	In terminal: $./password_locker.py 	Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit
Display prompt for creating an account 	Enter: ca 	Enter your first name, last name and password
Display prompt for login in 	Enter: li 	Enter your account name and password
Display codes for navigation 	Successful login 	Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit
Display prompt for creating a credential 	Enter: cc 	Enter the site name, your username and password
Display a list of credentials 	Enter: dc 	Prints a list of saved credentials
Exit application 	Enter: ex 	Exit the current navigation stage
# SetUp / Installation Requirements

## Prerequisites

   . python3.8/
   . pip3/
   . virtual/
    .xclip/

# Cloning

    In your terminal:

      $ git clone https://github.com/Nyagahisaac/Password-locker.git
      $ cd PasswordLocker

# Running the Application

    .To run the application, in your terminal:

      $ chmod +x run.py
      or
      $ python3.8  run.py

# Testing the Application

    .To run the tests for the class file:

      $ python3.8 user_test.py

# Technologies Used

    Python3.8

# License

# MIT ©2021 Nyagah Isaac