from mainAdmin import admin
from mainUser import user


if(__name__ == "__main__"):
    print("\t1.Admin Menu")
    print("\t2.User Menu")

    choice = int(input("Enter your choice:"))
    if(choice == 1):
        username = input("Enter username :")
        password = input("Enter password :")
        if(username == "Admin" and password == "Admin123"):
            admin()
        else:
            print("Invalid credentials...")

    elif(choice == 2):
        username = input("Enter username :")
        password = input("Enter password :")
        if(username == "RohitRahatal" and password == "Rohit2408"):
            user()
        else:
            print("Invalid credentials...")
        
        
        
    
