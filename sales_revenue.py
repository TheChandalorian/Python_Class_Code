# declare the list to store the sales persons name
salespeople = []

# declare the list to store the sales value
sales = []

# declare variable to hold total sales
total_sales = 0

# user input total number of sales people
no_salespeople = int(input("Please enter the amount of sales people on your team: "))

# populate the salespeople list with names from user input
for i in range(no_salespeople):
    salesperson = input("please enter the firstname of the sales person: ")
    salespeople.append(salesperson)

# polulate the sales list with sales from user input and calculate total sales amount
for i in range(no_salespeople):
    sales_amount = float(input("please enter the amount of sales in €: "))
    sales.append(sales_amount)
    total_sales += sales_amount

# print out the two lists vertically side by side
for x, y in zip(salespeople, sales):
    print(x, y, sep="\t\t")

# print total sales
print ("The total amount of sales is:", total_sales)

# calculate the average sales
average_sales = total_sales/no_salespeople

# print the average sales
print("The average sales is:", average_sales)

# determine the max and min sales
max_sales = max(sales)
min_sales = min(sales)

# print the max and min sales
print("The maximum sales by any one salesperson is:", max_sales)
print("The minimum sales by any one salesperson is:", min_sales)