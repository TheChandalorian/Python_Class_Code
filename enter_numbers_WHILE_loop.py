i = 1
y = 0
number_total = 0

while 1 != 0:    
    num = float(input("Please enter number: "))
    number_total += num
    y += 1
    if num == 0:
        break
    i = -1
    # number_total += num        only if we are including '0' to be considered in the numbers and average
    

avgerage = number_total / y

print("The average of your " + str(y) + " entered numbers is = %0.2f" %avgerage)



