# Let's built automated barista
menu = "Black coffee, Espresso, Latte, Cappucino"
print("Hello welcome to NetworkChuck Coffee!!!")
name = input("What is your name? ")

if name == "Ben" or "Patricia":
    evil_status = input("Are you Evil?\n")
    good_deeds = int(input("How many good deeds have you done today? \n")) 
    if evil_status == "Yes" and good_deeds < 4 :
        print("Your are not welcome here Evil, get out!")
        # Exit the programm inmmediately 
        exit()
    else:
     print("Oh, so you are a good guy")   
else:
    print(" Hello " + name + " what would like get from our menu: " + menu )

    order = input()
    
    if order == "Black coffee":
        price = 2
    elif order == "Espresso":
        price = 3
    elif order == "Latte":
        price = 4
    elif order == "Cappuicino":
        price = 5
    else:
        print("Sorry, we do not have that there.")
        
    quantity = input("How many coffees you would like?\n")

    # The Input funtion has always output string, int() does conversion to integer
    total = price * int(quantity)

    # The similar conversion can be done also from integer to string str()
    print("Your order is " + order + "the price is gonna be $" + str(total) )


# Another operator can be if not ... :