import time

def login():
     print("===CHECKING IDENTITY=====")
     time.sleep(1.1)
     time.sleep(1.1)
     print("-----Are you Ready----?")
     userid = (input("Please enter your name:"))
     password = input("Please enter your password :")

     if userid == 'kangni'   and     password == 'fanta2004':
        print("You are login ")
     else :
        print("access denied")
     facebook()

def facebook():
  print("Welcome to Facebook")
  print("====You logged in succesfully!!!!======")

login()