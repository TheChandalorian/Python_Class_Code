height = input("Please enter your height in cm's: ")
weight = input("Please enter your weight in kg: ")

BMI = ((float(weight)/float(height))/float(height))*10000
BMI = round(BMI,1)

if (BMI) < 18.5:
    print("Your BMI is " + str(BMI) + ", this falls within the  underweight range")
elif (BMI >= 18.5) and (BMI <= 24.9):
    print("Your BMI is " + str(BMI) + ", this falls within the healthy range")
elif (BMI >= 25.0) and (BMI <= 29.9):
    print("Your BMI is " + str(BMI) + ", this falls within the overweight range")
else:
    print("Your BMI is " + str(BMI) + ", this falls within the obese weight range")