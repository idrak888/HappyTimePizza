def discount(subtotal, disc):
    return subtotal * ((100-disc)/100)

def delivery_distance_premium (distance):
    charge = None

    if distance < 10:
        charge = 0
    elif distance >= 10 and distance <= 19:
        charge = 2
    elif distance >= 20 and distance <= 29:
        charge = 4

    return charge

def tip(subtotal, tip):
    tipAmount = (tip/100) * subtotal
    return tipAmount

def tax(subtotal):
    return 0.13 * subtotal

def is_valid_option(choice):
    choice = choice.lower()
    valid = False

    if choice == "meal":
        valid = True
    elif choice == "appetizer":
        valid = True
    elif choice == "dessert":
        valid = True
    elif choice == "beverages":
        valid = True
    elif choice == "done":
        valid = True

    return valid

def customer_order():
    orderRunning = True
    subtotal = 0
    meal = False
    appetizer = False
    dessert = False
    beverages = False

    while(orderRunning):
        valid = False
        choice = None
        while valid is not True:
            choice = input("What would you like to order? OPTIONS: meal, appetizer, dessert, beverages: ")
            valid = is_valid_option(choice)
            if valid is not True:
                print("Sorry, but this option is not recognized. Please try again.")

        if choice == "done":
            orderRunning = False
            break

        if choice == "meal":
            item = input("What meal would you like to order? OPTIONS: pizza, calzone: ")
            quantity = int(input(f"How many {item}s would you like?"))
            meal = True
            veganFees = 0

            for i in range(0, quantity):
                vegan = input(f"Is {item} #{i + 1} vegan? y/n")
                if vegan == "y":
                    veganFees = veganFees + 2.5

            if item == "pizza":
                subtotal = subtotal + (21.99 * quantity)
            elif item == "calzone":
                subtotal = subtotal + (10.99 * quantity)

            subtotal = subtotal + veganFees

        elif choice == "appetizer":
            item = input("What appetizer would you like to order? OPTIONS: cheese bread, garlic bread: ")
            quantity = int(input(f"How many {item}s would you like?"))
            appetizer = True

            if item == "cheese bread":
                subtotal = subtotal + (4.99 * quantity)
            elif item == "garlic bread":
                subtotal = subtotal + (3.99 * quantity)

        elif choice == "dessert":
            item = input("What dessert would you like to order? OPTIONS: cinnamon sticks, cookies: ")
            quantity = int(input(f"How many {item}s would you like?"))
            dessert = True

            if item == "cinnamon sticks":
                subtotal = subtotal + (4.59 * quantity)
            elif item == "cookies":
                subtotal = subtotal + (3.59 * quantity)

        elif choice == "beverages":
            item = input("What beverages would you like to order? OPTIONS: pop, bottled water: ")
            quantity = int(input(f"How many {item}s would you like?"))
            beverages = True

            if item == "pop":
                subtotal = subtotal + (2.5 * quantity)
            elif item == "bottled water":
                subtotal = subtotal + (1.5 * quantity)

        runAgain = input("Would you like to order another item? y/n: ")
        if runAgain == "n":
            orderRunning = False

    if meal is True and appetizer is True and dessert is True and beverages is True:
        print("You ordered an item from each category. Please enjoy your 15% discount!")
        print(f"Your subtotal prior to the discount was: ${subtotal}")
        subtotal = discount(subtotal, 15)
        print(f"Your new subtotal after the discount is: ${subtotal:.2f}")
    elif meal is True and beverages is True:
        print("You ordered a meal and a drink. Please enjoy your 5% discount!")
        print(f"Your subtotal prior to the discount was: ${subtotal}")
        subtotal = discount(subtotal, 5)
        print(f"Your new subtotal after the discount is: ${subtotal:.2f}")

    return subtotal


def main():
    print("Thanks for visiting HappyTime Pizza!")

    distance = int(input("How many km are you from the restaurant?"))
    delivery_charge = 3.99 + delivery_distance_premium(distance)
    subtotal_final = 0

    if delivery_charge == None:
        print("Too far")

    print(f"Your delivery charge will be {delivery_charge}.")
    proceed = input("Do you still wish to continue? y/n ")

    if proceed == "n":
        print("We understand. Have a good day!")
    else:
        subtotal_final = customer_order()

    # check if subtotal is 0

    tipPercentage = int(input("Please enter a tip percentage for the order: "))
    tipAmount = tip(subtotal_final, tipPercentage)
    taxAmount = tax(subtotal_final)

    total = subtotal_final + delivery_charge + tipAmount + taxAmount

    print("")
    print(f"SUBTOTAL:   {subtotal_final:5.2f}")
    print(f"TAX:        {taxAmount:5.2f}")
    print(f"TIP:        {tipAmount:5.2f}")
    print(f"DELIVERY:   {delivery_charge:5.2f}")
    print(f"TOTAL:      {total:5.2f}")


main()