from classes import CoffeeMachine


machine_on = True
coffee_machine = CoffeeMachine()
while machine_on:
    user_choice = coffee_machine.coffee_choice()
    if user_choice == 'report':
        coffee_machine.show_status()
        continue
    if user_choice == 'refill':
        to_refill = ""
        while to_refill not in ['coffee', 'milk', 'water']:
            to_refill = input("What do you want to refill? [coffee] [milk] [water]\n")
        coffee_machine.refill(to_refill)
        continue
    if user_choice == 'off':
        break

    price = coffee_machine.define_price(user_choice)

    to_unpack = coffee_machine.money_io(price)

    change = round(to_unpack[0])
    money_paid = to_unpack[1]
    enough_money = to_unpack[2]

    if not enough_money:
        print(f'Not enough money, here is your money back: ${money_paid}')
    elif change == 0:
        refilled_failed = coffee_machine.make_coffee(user_choice)
        if refilled_failed:
            print(f"Failed to refill. Couldn't make your {user_choice}.\n"
                  f"Here is your money back {money_paid}")
            coffee_machine.money -= money_paid
            continue
        print(f"Here is your {user_choice}, enjoy!")
    else:
        refilled_failed = coffee_machine.make_coffee(user_choice)
        if refilled_failed:
            print(f"Failed to refill. Couldn't make your {user_choice}.\n"
                  f"Here is your money back {money_paid}")
            coffee_machine.money -= money_paid
            continue
        print(f'Here is your change: ${change}.\nAnd here is your {user_choice}. Enjoy!')
