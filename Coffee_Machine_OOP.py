from menu import Menu  # import menu.py from python repository
from coffee_maker import CoffeeMaker # import coffee_maker.py from python repository
from money_machine import MoneyMachine # import money_machine.py from python repository
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
print('''
:=*%@@@@@@@@@@@@@@@@@@@@@@@@@.                        .@@@@@@@@@@@@@@@@@@@@@@@@@%*=: 
  .=#@@@@@@@@@@@@@@@@@@@@@@#           i    i           #@@@@@@@@@@@@@@@@@@@@@@#=.     
     .=@@@@@@@@@@@@@@@@@@@@@%:         #%%%%#         :%@@@@@@@@@@@@@@@@@@@@@=.        
        =@@@@@@@@@@@@@@@@@@@@@@%#######@@@@@@#######%@@@@@@@@@@@@@@@@@@@@@@=           
         :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                         
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             
          .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.             
         -%%###%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%###%%-             
                         .:-=+*%@@@@@@@@@@@@@@@@@@@@%*+=-:.                            
                                 :=#@@@@@@@@@@@@#=:                                    
                                    .+@@@@@@@@+.                                       
                                      .#@@@@#.                                         
                                        =@@=                                           
                                        'l'
  ________               ____        __                              ______          __   
 /_  __/ /_  ___        / __ )____ _/ /_____ ___  ____ _____        / ____/___  ____/ /__ 
  / / / __ \/ _ \______/ __  / __ `/ __/ __ `__ \/ __ `/ __ \______/ /   / __ \/ __  / _ \\
 / / / / / /  __/_____/ /_/ / /_/ / /_/ / / / / / /_/ / / / /_____/ /___/ /_/ / /_/ /  __/
/_/ /_/ /_/\___/     /_____/\__,_/\__/_/ /_/ /_/\__,_/_/ /_/      \____/\____/\__,_/\___/                      ''')
while is_on:
    options = menu.get_items()
    choice = input(f'\nWhat would you like? {options}: ')
    if choice == 'off':
        exit()
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
