import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards2 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_scr():
    os.system('cls')


def random_card_computer():
    a = cards[random.randint(0, 12)]
    return a


def random_user_card():
    a = cards2[random.randint(0, 12)]
    return a


def initial_scores():
    a = []
    for i in range(0, 2):
        a.append(random_card_computer())
    return a


def add(a):
    a = sum(a)
    return a


def add_card_user(a):
    a.append(random_user_card())
    return a


def add_card_computer(a):
    a.append(random_card_computer())
    return a


def final():
    print(
        f'Your final hand: {user_score}, final score: {add(user_score)}')
    print(
        f"Computer's final hand: {computer_score}, final score: {add(computer_score)}")


def again():
    choice = input('Would you like to play again? ').lower()
    while (choice != 'yes' and choice != 'y' and choice != 'no' and choice != 'n'):
        choice = input('Enter choice again: ').lower()
    if (choice == 'yes' or choice == 'y'):
        clear_scr()
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
        main()
    elif(choice == 'no' or choice == 'n'):
        print('Glad to meet you. See you again😊')
        exit()


def main():
    global computer_score
    global user_score
    computer_score = initial_scores()
    user_score = initial_scores()
    if (add(user_score) == 21):
        final()
        print('You win, well done👍')
        again()
    if (11 in computer_score and add(computer_score) > 21):
        computer_score.remove(11)
        computer_score.append(1)
        cards.remove(11)
        cards.append(1)
    print(f"\nYour cards: {user_score}, current score: {sum(user_score)}")
    print(f"Computer's first card: {computer_score[0]}")
    choice = input(
        "Type 'y/yes' to get another card or type 'n/no' to pass: ").lower()
    while (choice != 'yes' and choice != 'y' and choice != 'no' and choice != 'n'):
        choice = input('Enter choice again: ').lower()

    if (choice == 'yes' or choice == 'y'):
        while (choice == 'yes' or choice == 'y'):
            user_score = add_card_user(user_score)
            if (11 in user_score and add(user_score) > 21):
                user_score.remove(11)
                user_score.append(1)
                cards2.remove(11)
                cards2.append(1)
                final()
            if (add(user_score) > 21):
                final()
                print('You went over...lol. You lose🤣🤣')
                again()
            if (add(user_score) == 21):
                final()
                print('You win, well done👍')
                again()
            else:
                print(
                    f"Your cards: {user_score}, current score: {sum(user_score)}")
                print(f"Computer's first card: {computer_score[0]}")
                choice = input(
                    "Type 'y/yes' to get another card or type 'n/no' to pass: ").lower()
            while (choice != 'yes' and choice != 'y' and choice != 'no' and choice != 'n'):
                choice = input('Enter choice again: ').lower()
    if (choice == 'no' or choice == 'n'):
        while (add(computer_score) < 17):
            computer_score = add_card_computer(computer_score)
        if (add(computer_score) == 21):
            final()
            print('Opponent Wins, you lose🤣🤣')
            again()
        if (11 in computer_score and add(computer_score) > 21):
            computer_score.remove(11)
            computer_score.append(1)
            cards.remove(11)
            cards.append(1)
            while (add(computer_score) < 17):
                computer_score = add_card_computer(computer_score)
        if (add(computer_score) > 21):
            final()
            print('Opponent went over. You win. Well done👍')
            again()
    if (add(user_score) > add(computer_score)):
        final()
        print("Your score is more than the opponent. You win. Well done👍")
        again()
    elif (add(user_score) < add(computer_score)):
        final()
        print("Opponent's score is more than your score. You lose🤣🤣")
        again()
    elif (add(user_score) == add(computer_score)):
        final()
        print("Both the scores are same. It's a draw😒. No worries, let's go again😉")
        again()


choice = input('Would you like to play a game of Jack Jack? ').lower()
while (choice != 'yes' and choice != 'y' and choice != 'no' and choice != 'n'):
    choice = input('Enter choice again: ').lower()
if (choice == 'yes' or choice == 'y'):
    clear_scr()
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
    main()
elif(choice == 'no' or choice == 'n'):
    print('You seem to be having a bad day🤔. No worries, i hope you be happy very soon. Take care😊')
    exit()
