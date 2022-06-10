MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coffee_machine = '''
   ___       __  __                               _     _            
  / __\___  / _|/ _| ___  ___    /\/\   __ _  ___| |__ (_)_ __   ___ 
 / /  / _ \| |_| |_ / _ \/ _ \  /    \ / _` |/ __| '_ \| | '_ \ / _ \\
/ /__| (_) |  _|  _|  __/  __/ / /\/\ \ (_| | (__| | | | | | | |  __/
\____/\___/|_| |_|  \___|\___| \/    \/\__,_|\___|_| |_|_|_| |_|\___|
                                                                     
'''
symbol = '''
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
/_/ /_/ /_/\___/     /_____/\__,_/\__/_/ /_/ /_/\__,_/_/ /_/      \____/\____/\__,_/\___/                      '''
print(symbol)
print(coffee_machine)


def money():
    global total
    while True:
        try:
            penny = int(input('How many pennies? '))
            break
        except:
            print('Enter the correct value.')
    while True:
        try:
            nickel = int(input('How many nickels? '))
            break
        except:
            print('Enter the correct value.')
    while True:
        try:
            dime = int(input('How many dimes? '))
            break
        except:
            print('Enter the correct value.')
    while True:
        try:
            quarter = int(input('How many quarters? '))
            break
        except:
            print('Enter the correct value.')
    total = penny*0.01 + nickel*0.05 + dime*0.10 + quarter*0.25


def order_coffee(coffee):
    if total < MENU[coffee]['cost']:
        print('Not enough money. Money Returned')
        main()
    else:
        print(
            f'The change is ${round(total-MENU[coffee]["cost"],2)}\nEnjoy your coffee☕')
        resources['water'] = resources['water'] - \
            MENU[coffee]['ingredients']['water']
        resources['milk'] = resources['milk'] - \
            MENU[coffee]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - \
            MENU[coffee]['ingredients']['coffee']
        main()


def check(coffee):
    global resources
    global MENU
    if (resources['water']-MENU[coffee]['ingredients']['water']) < 0:
        print('Not enough water. Money returned.')
        main()
    if (resources['milk']-MENU[coffee]['ingredients']['milk']) < 0:
        print('Not enough milk. Money returned')
        main()
    if (resources['coffee']-MENU[coffee]['ingredients']['coffee']) < 0:
        print('Not enough coffee. Money returned')
        main()


def order():
    global coffee
    coffee = input(
        'What would you like to order today? (Espresso, Latte, Cappuccino) :').lower()
    if coffee == 'off':
        exit()
    if coffee == 'report':
        print(
            f"Water :{resources['water']}ml\nMilk :{resources['milk']}ml\nCoffee :{resources['coffee']}gm")
        main()
    while coffee != 'espresso' and coffee != 'latte' and coffee != 'cappuccino':
        coffee = input(('Enter the correct coffee😅: '))
    check(coffee)


def main():
    order()
    check(coffee)
    money()
    order_coffee(coffee)


main()
