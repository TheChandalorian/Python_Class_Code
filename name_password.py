name = input("What is your name? ")

while name != "Gareth":
    print("Sorry thats not your name \n")
    name = input("What is your name? ")

password = input("What is the password? ")

while password != "WorldCup":
    print("Access Denied")
    password = input("what is the password? ")
    
print("You are authorized")