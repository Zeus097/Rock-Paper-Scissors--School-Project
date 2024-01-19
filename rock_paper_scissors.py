import random


rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_name = input("What is your name: ")
print(f"Welcome {player_name} to \033[1;36m Rock -- \033[1;33m Paper -- \033[1;31m Scissors \n")
print("\033[1;33m If your hand is equal, You will play your turn again ! \n")
number_of_games = int(input("\033[1;34m  Make your bet: positive number in a range [ 1 - 101 ] \n"))
game_counter = 0
player_counter = 0
computer_counter = 0

while game_counter < number_of_games < 102:
    game_counter += 1

    player_move = input("\033[1;32m Choose [r]rock🗻 || [p]paper🧻 || [s]scissors️✂️:  \n")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("\033[1;31m Invalid Input. Try again... \n")
        game_counter -= 1
        continue
        # raise SystemExit("Invalid Input. Try again...")

    computer_choice = random.randint(1, 3)
    computer_move = ""

    if computer_choice == 1:
        computer_move = rock
    elif computer_choice == 2:
        computer_move = paper
    elif computer_choice == 3:
        computer_move = scissors
    print(f"\033[1;35m 30 * '-' \n")
    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_counter += 1
        print("\033[1;32m WooHoo...\n", end=" ")
        print(f"\033[1;32m ---{player_name} win {player_counter} game/s! ---\n")
    elif player_move == computer_move:
        game_counter -= 1
        print(f"\033[1;35m 30 * '-' \n")
        print("\033[1;33m Equal, draw again! \n")
        print(30 * "-")
    else:
        computer_counter += 1
        print(f"\033[1;35m 30 * '-' \n")
        print("\033[1;31m You loose! \n")
        print(30 * "-")

if game_counter >= 1:

    if player_counter > computer_counter:
        print(f"\033[1;35m 30 * '-' \n")
        print(f"\033[1;32m You totally smashed your opponent with {player_counter} - {computer_counter} \n")
        print(f"\033[1;32m {player_name} you are a Rock Star !! \n")
        print(f"You played {game_counter} game/s. See You again :)  !! ")
        print(f"\033[1;32m 30 * '-' \n")
    else:
        print(f"\033[1;35m 30 * '-' \n")
        print(f"{player_name} won {player_counter} game/s ^_^ !")
        print(f"The Computer won {computer_counter} game/s !")
        print(f"You played {game_counter} game/s. See You again :)  !! ")
        print(30 * "-")

    print(f"\033[1;36m *****  Game developed by Vasil, Thank you for playing !  -----    ***** \n")
else:
    print("\033[1;31m  Your number is invalid !! --- End of the game --- \n")
