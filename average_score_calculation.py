module_1 = int(input('Enter your first Module score: '))

module_2 = int(input('Enter your second Module score: '))

module_3 = int(input('Enter your third Module score: '))

total = (module_1 + module_2 + module_3) / 3

if total > 70:
    print('Congratulations, your average score is: ' + str(total))

elif total < 40:
    print('oh dear, your average score is: ' + str(total) + ', better study more')

else:
    print('Your average score is: ' + str(total))

    