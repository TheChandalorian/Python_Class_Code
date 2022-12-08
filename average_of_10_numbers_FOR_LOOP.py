print("you are not going to enter 10 numbers")

number_total = 0

for n in range (10):
    
    num = float(input("Enter number: "))
    
    number_total += num


avgerage = number_total / 10

print("The average of your 10 numbers is = %0.2f" %avgerage)