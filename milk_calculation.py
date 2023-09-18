
# empty list to store hour input for days
hours = []
# how many days receiving input for
days = 7
# how many hours stephen spends at home in through the days
total_hours = 0
# how much milk stephen drinks per hour
milk_rate = 0.5
# how much dad charges for milk 
dads_rate = 1.35

# for loop to get hours for all the day s, and store the information into a list
for i in range(0, days):
    hour = int(input(
        'enter the hours Stephen is at home for each day, from Monday to Sunday :'))
    hours.append(hour)
    total_hours += hour

# calculate the total milk for the week
total_milk = total_hours * milk_rate

# calculate the total cost for the milk
cost_milk = total_milk * dads_rate

# display how much milk stephen drinks in 7 days
print(f'Stephen drinks a toal of ', total_milk, ' liters in 7 days')
# display how much stephen has to pay to his dad for the milk
print(f'Stephen needs to pay his dad a toal of $', round(cost_milk, 2))
