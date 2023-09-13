buy_nails_amount = int(input('How many nails would you like to purchase: '))

nail_cost = buy_nails_amount / 10
 
if buy_nails_amount >= 151:
    order_cost = nail_cost * 0.8
    print('the cost of your order before P&P is: € ' + str(round(order_cost,3)))
elif buy_nails_amount >= 51:
    order_cost = nail_cost * 0.9
    print('the cost of your order before P&P is: € ' + str(round(order_cost,3)))
else:
    order_cost = nail_cost
    print('the cost of your order before P&P is: € ' + str(round(order_cost,3)))

total_cost = float(order_cost) + 2.00

print('The total cost of your order today inc P&P is: € ' + str(round(total_cost,3)))
