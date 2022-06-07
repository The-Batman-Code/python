import random
import time
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
print('''




   _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
                                                                                      
''')


def ans():
    a = random.randint(1, 100)
    return a


def main(round):
    a = ans()
    i = 0
    if (choice == 'hard'):
        normalize = 5
    else:
        normalize = 10
    print(a)
    for i in range(0, round-1):
        count = normalize-i
        print(f'You have {count} attempts to guess the number')
        while True:
            try:
                user_ans = int(input('Make a guess: '))
                break
            except:
                print('That is not a valid option. Enter integers')
        if (user_ans > a):
            print('Too high \nGuess again.')
        elif (user_ans < a):
            print('Too low \nGuess again.')
        elif (user_ans == a):
            print('That is the correct guess. Well done😊😊')
            exit()
    print(f'You have 1 attempt to guess the number')
    user_ans = int(input('Make a guess: '))
    if (user_ans > a):
        print('Too high \nYou have run out of guesses.')
    elif (user_ans < a):
        print('Too low \nYou have run out of guesses.')
    elif (user_ans == a):
        print('That is the correct guess. Well done😊😊')


print('Welcome to The Number Guessing Game😊')
print('Loading...')
time.sleep(2)
print('I am thinking of a number between 1 and 100')
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while (choice != 'hard' and choice != 'easy'):
    choice = input('Enter the correct choice: ')
if (choice == 'hard'):
    main(5)
else:
    main(10)
