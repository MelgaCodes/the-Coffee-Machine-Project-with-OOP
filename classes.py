WATER_MAX = 100
MILK_MAX = 100
COFFEE_MAX = 25
ESPRESSO_WATER = 30
ESPRESSO_COFFEE = 7
CAPUCCINO_WATER = 30
CAPUCCINO_MILK = 30
CAPUCCINO_COFFEE = 7
LATTE_WATER = 30
LATTE_MILK = 50
LATTE_COFFEE = 7


class CoffeeMachine:

    def __init__(self):
        self.money = 0
        self.water = WATER_MAX
        self.milk = MILK_MAX
        self.coffee = COFFEE_MAX
        self.last_price_paid = 0

    @staticmethod
    def coffee_choice():
        """Prompts the user for a choice and returns it"""
        choice = ""
        while choice not in ["espresso", "capuccino", "latte", "off", "report", "refill"]:
            choice = input("Choose your drink\n"
                           "Espresso    - $1\n"
                           "Capuccino   - $2\n"
                           "Latte       - $3\n").lower()
        return choice

    @staticmethod
    def define_price(user_choice):
        """Establishes the price to pay depending on the user's choice and returns it"""
        if user_choice == 'espresso':
            price = 1
        elif user_choice == 'capuccino':
            price = 2
        else:
            price = 3

        return price

    def show_status(self):
        """Prints the coffee machine's status"""
        print(f"Water:  {self.water}mL\n"
              f"Milk:   {self.milk}mL\n"
              f"Coffee: {self.coffee}g\n"
              f"Money:  ${self.money}")

    def money_io(self, price):
        quarters = ""
        dimes = ""
        nickels = ""
        pennies = ""
        while type(quarters) is not int:
            quarters = int(input("How many quarters are you paying? "))
        while type(dimes) is not int:
            dimes = int(input("How many dimes are you paying? "))
        while type(nickels) is not int:
            nickels = int(input("How many nickels are you paying? "))
        while type(pennies) is not int:
            pennies = int(input("How many pennies are you paying? "))

        price_paid = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies

        enough_money = True

        if price_paid >= price:
            change = price_paid - price
            self.money += price
            self.last_price_paid = price_paid
        else:
            change = 0
            enough_money = False
        return [change, price_paid, enough_money]

    def refill(self, substance):
        """Sets the value of the chosen substance to the maximum"""
        if substance == 'coffee':
            self.coffee = COFFEE_MAX
        elif substance == 'milk':
            self.milk = MILK_MAX
        else:
            self.water = WATER_MAX

    def enough_reserves(self, coffee_type, substance):
        if coffee_type == 'espresso':
            if substance == 'water':
                return self.water > ESPRESSO_WATER
            elif substance == 'coffee':
                return self.coffee > ESPRESSO_COFFEE
        elif coffee_type == 'capuccino':
            if substance == 'water':
                return self.water > CAPUCCINO_WATER
            elif substance == 'coffee':
                return self.coffee > CAPUCCINO_COFFEE
            elif substance == 'milk':
                return self.milk > CAPUCCINO_MILK
        elif coffee_type == 'latte':
            if substance == 'water':
                return self.water > LATTE_WATER
            elif substance == 'coffee':
                return self.coffee > LATTE_COFFEE
            elif substance == 'milk':
                return self.milk > LATTE_MILK

    def make_coffee(self, choice):
        """If there are enough resources to make the selected coffee, subtracts the necessary quantity of resources from
        machine to make it. If there are not enough resources it prompts the user for a refill, if the user fails to
        refill it goes back to the main menu"""

        if choice == 'espresso':
            if self.enough_reserves(choice, 'water') and self.enough_reserves(choice, 'coffee'):
                self.water -= ESPRESSO_WATER
                self.coffee -= ESPRESSO_COFFEE
                return
            else:
                for substance in ['coffee', 'water']:
                    if not self.enough_reserves(choice, substance):
                        refilling = input(f"Not enough {substance}. Please type [refill] to refill,\n"
                                          "or type anything else to come back to the main menu: ").lower()
                        if refilling == 'refill':
                            self.refill(substance)
                            self.make_coffee(choice)
                        else:
                            return True
        elif choice == 'capuccino':
            if self.enough_reserves(choice, 'water') and self.enough_reserves(choice, 'coffee')\
                    and self.enough_reserves(choice, "milk"):
                self.water -= CAPUCCINO_WATER
                self.coffee -= CAPUCCINO_COFFEE
                self.milk -= CAPUCCINO_MILK
                return
            else:
                for substance in ['coffee', 'water', 'milk']:
                    if not self.enough_reserves(choice, substance):
                        refilling = input(f"Not enough {substance}. Please type [refill] to refill,\n"
                                          "or type anything else to come back to the main menu: ").lower()
                        if refilling == 'refill':
                            self.refill(substance)
                            self.make_coffee(choice)
                            return
                        else:
                            return True
        elif choice == 'latte':
            if self.enough_reserves(choice, 'water') and self.enough_reserves(choice, 'coffee') \
                    and self.enough_reserves(choice, "milk"):
                self.water -= LATTE_WATER
                self.coffee -= LATTE_COFFEE
                self.milk -= LATTE_MILK
                return
            else:
                for substance in ['coffee', 'water', 'milk']:
                    if not self.enough_reserves(choice, substance):
                        refilling = input(f"Not enough {substance}. Please type [refill] to refill,\n"
                                          "or type anything else to come back to the main menu: ").lower()
                        if refilling == 'refill':
                            self.refill(substance)
                            self.make_coffee(choice)
                        else:
                            return True
