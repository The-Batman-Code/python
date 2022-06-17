import random
import os
import data  # import data file placed in python repository
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
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
print(logo)


def clr_scr():
    os.system('cls')


def random_index():
    return random.randint(0, 49)


def question(index):
    return f"{data.data[index]['name']}, {data.data[index]['description']}, {data.data[index]['country']}"


def main():
    choice = input('Who has more instagram followers? Type A or B: ').lower()
    while choice != 'a' and choice != 'b':
        choice = input('Enter correct choice: ').lower()
    if data.data[index_A]['follower_count'] > data.data[index_B]['follower_count'] and choice == 'a':
        correct()
    elif data.data[index_A]['follower_count'] > data.data[index_B]['follower_count'] and choice == 'b':
        print('Wrong. You Lose😉')
    elif data.data[index_A]['follower_count'] < data.data[index_B]['follower_count'] and choice == 'a':
        print('Wrong. You Lose😉')
    elif data.data[index_A]['follower_count'] < data.data[index_B]['follower_count'] and choice == 'b':
        correct()


def correct():
    global index_A
    global index_B
    global score
    index_A = index_B
    index_B = random_index()
    while index_A == index_B:
        index_B == random_index()
    score += 1
    print(f'\nThats right👌. Your current score is {score}')
    print(f'Compare A: {question(index_A)}')
    print(vs)
    print(f'Against B: {question(index_B)}')
    main()


score = 0
index_A = random_index()
index_B = random_index()
while index_A == index_B:
    index_B == random_index()
print(f'\nCompare A: {question(index_A)}')
print(vs)
print(f'Against B: {question(index_B)}')
choice = input('Who has more instagram followers? Type A or B: ').lower()
while choice != 'a' and choice != 'b':
    choice = input('Enter correct choice: ').lower()
if data.data[index_A]['follower_count'] > data.data[index_B]['follower_count'] and choice == 'a':
    correct()
elif data.data[index_A]['follower_count'] > data.data[index_B]['follower_count'] and choice == 'b':
    print('Wrong. You Lose😉')
elif data.data[index_A]['follower_count'] < data.data[index_B]['follower_count'] and choice == 'a':
    print('Wrong. You Lose😉')
elif data.data[index_A]['follower_count'] < data.data[index_B]['follower_count'] and choice == 'b':
    correct()
