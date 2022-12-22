User_Req = input("1\tCalculate area of a circle\n2\tCalculate volume of a sphere\n3\tExit\nEnter option 1-3: ")
i = 0
while i == 0:
    if User_Req == str(1):
        Radius = int(input("Enter radius: "))
        Area_Of_Circle = 3.14*(Radius**2)
        print("Area is " + str(Area_Of_Circle))
        User_Req = input("1\tCalculate area of a circle\n2\tCalculate volume of a sphere\n3\tExit\nEnter option 1-3: ")
        i += 0

    elif User_Req == str(2):
        Radius_Sphere = int(input("Enter radius: "))
        Volume_Of_Sphere = (4/3*(3.14*(Radius_Sphere**3)))
        print("Area is " + str(Volume_Of_Sphere))
        User_Req = input("1\tCalculate area of a circle\n2\tCalculate volume of a sphere\n3\tExit\nEnter option 1-3: ")
        i += 0

    elif User_Req == str(3):
        print("You chose to exit the program")
        i += 1

    else:
        print("Sorry, please select from ")
        User_Req = input("1\tCalculate area of a circle\n2\tCalculate volume of a sphere\n3\tExit\nEnter option 1-3: ")
        i += 0