#metric, to select the metric eg F or C
#temp, to know the number value to convert accordingly 

def temperature_converter(metric=None, temp=None):
    if metric == "F":
        return(temp - 32.0) * 0.5666
    elif metric == "C":
        return(temp * 1.8) + 32.0
    else:
        print("Needs to be (F) or (C)!")

#ask user to select Fagrenhet or Celsius
metric = input("Select (F) or (C): " )
#ask user to input temperature value
temp = int(input("What is the temperature: " ))
#converter and to print function
m = temperature_converter(metric, temp)
print(temp, "degrees", metric, "is", m, "degrees", metric)



