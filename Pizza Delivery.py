# Python Pizza Delivery System

# Variables
# These can be changed as per future needs
pricings_per_size = {
  "l": 25,
  "m": 20,
  "s": 15,
}

pizza_sizes = pricings_per_size.keys()
affirmatives = ['y', 'yes']
negatives = ['n', 'no']
valid_confirmations = affirmatives + negatives
pizza_sizes_comma_separated_string = ', '.join([f"'{i}'" for i in pizza_sizes])

def process_order(size: str, add_pepperoni: bool = False, extra_cheese: bool = False):
    global pricings_per_size
    
    money = pricings_per_size.get(size[0].lower())

    money += 3*(add_pepperoni.lower().strip() in affirmatives)
    money += (extra_cheese[0].lower().strip in affirmatives)
    print(f'Total payable amount: ${money:,.2f}')

#print('You have to pay $%d' % money)

if __name__ == "__main__":
    # Welcome Banner
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

    print('Welcome to Python Pizza Delivery')

    # User Inputs and Checks
    size = input('What size pizza do you want to order? ').lower().strip()
    if size not in pizza_sizes:
        print(f"Invalid pizza size, choose from either of {pizza_sizes_comma_separated_string} and try again.")

    add_pepperoni = input('Do you want pepperoni? ').lower().strip()
    if add_pepperoni not in valid_confirmations:
        print(f"Invalid choice, choose either '{affirmatives[0]}' or '{negatives[0]}' for adding pepperoni and try again.")

    extra_cheese = input('Do you want extra cheese? ').lower().strip()
    if extra_cheese not in valid_confirmations:
        print(f"Invalid choice, choose either '{affirmatives[0]}' or '{negatives[0]}' for extra cheese and try again.")

    place_order()
    process_order(size = size,
                  add_pepperoni = add_pepperoni,
                  extra_cheese = extra_cheese)
