import random
import sys

# exec makes python to look for the thing before dropping error
def rps():
    while True:
        enemy_choice = ["rock", "paper", "scissors"]
        your_choice = input("type your thing (paper, scissors, rock) ")
        your_choice_lower = your_choice.lower().strip()
        enemy_choice_random = random.choice(enemy_choice)

        if your_choice_lower in enemy_choice:
            if (
                enemy_choice_random == enemy_choice[0]
                and your_choice_lower == "paper"
                or enemy_choice_random == enemy_choice[1]
                and your_choice_lower == "scissors"
                or enemy_choice_random == enemy_choice[2]
                and your_choice_lower == "rock"
            ):
                print(f"you won!: {enemy_choice_random} {your_choice_lower}")
                exec("choice()")
                
            elif (
                enemy_choice_random == enemy_choice[0]
                and your_choice_lower == "scissors"
                or enemy_choice_random == enemy_choice[1]
                and your_choice_lower == "rock"
                or enemy_choice_random == enemy_choice[2]
                and your_choice_lower == "paper"
            ):
                print(f"you lose!: {enemy_choice_random} {your_choice_lower}")
                exec("choice()")
                
            elif your_choice_lower == enemy_choice_random:
                print(f"draw: {enemy_choice_random} {your_choice_lower}")
                exec("choice()")
                
                
        else:
            print("not thing in rock paper scissors")


def infmode():
    while True:
        enemy_choice = ["rock", "paper", "scissors"]
        your_choice = input("type your thing (paper, scissors, rock) ")
        your_choice_lower = your_choice.lower().strip()
        enemy_choice_random = random.choice(enemy_choice)
        if your_choice_lower in enemy_choice:
            if (
                enemy_choice_random == enemy_choice[0]
                and your_choice_lower == "paper"
                or enemy_choice_random == enemy_choice[1]
                and your_choice_lower == "scissors"
                or enemy_choice_random == enemy_choice[2]
                and your_choice_lower == "rock"
            ):
                print(f"you won!: {enemy_choice_random} {your_choice_lower}")
                
            elif (
                enemy_choice_random == enemy_choice[0]
                and your_choice_lower == "scissors"
                or enemy_choice_random == enemy_choice[1]
                and your_choice_lower == "rock"
                or enemy_choice_random == enemy_choice[2]
                and your_choice_lower == "paper"
            ):
                print(f"you lose!: {enemy_choice_random} {your_choice_lower}")
                
            elif your_choice_lower == enemy_choice_random:
                print(f"draw: {enemy_choice_random} {your_choice_lower}")
                
        else:
            print("not thing in a paper rock scissors")


def choice():
    answer = ["yes", "no", "infinity mode"]
    users_choice = input("do you want to countinue(yes, no, infinity mode) ")

    if users_choice in answer:
        if users_choice == "yes":
            input("press enter to countinue")
            rps()
        elif users_choice == "no":
            input("press enter to countinue")
            sys.exit()
        elif users_choice == "infinity mode":
            input("press enter to countinue")
            infmode()
    else:
        print("I think you tried typing (yes, no, infinity mode) please try again")
        choice()


choice()
