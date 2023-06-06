# convert cups to fluid ounces

def main():
    # display the intro screen
    intro()
    # receives input to how many cups the user has
    cups_needed = int(input('Please enter how many cups of fluid? '))
    # convert cup to ounces function
    cups_to_ounces(cups_needed)


def intro():
    # explain to the user what is happening, introductions creen
    print('Hello there\nThis function will convert\nThe amount of cups you enter to ounces')
    print('1 cup to 8 ounces')
    print()


# accpets number of cups and displays the converted amount into ounces
def cups_to_ounces(cups):
    ounces = cups * 5
    print('This converts to', ounces, ' ounces')


# call main function
main()
