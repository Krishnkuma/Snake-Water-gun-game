import random

def play_game(player_choice,computer_choice):
    if player_choice==computer_choice:
        print("match tie")
        
    elif player_choice=="snake":
        if computer_choice=="water":
            print("you won the match")
        else:
            print("you lose the game")
    elif player_choice=="water":
        if computer_choice=="snake":
            print("you lose the game")
        else:
            print("you won the match")
    else:
        if computer_choice=="snake":
            print("you won the game")
        else:
            print("you lose the game")

def my_computer_choice():
    choices=["snake","water","gun"]
    return random.choice(choices)
def my_choice():
    
    print("welcome to Snake Water Gun game")
    print("please chose one: snake, water, gun")
    player_choice=input("enter your choice:")
    if player_choice not in ["snake","water","gun"]:
        print("invalid chose, please chose again")
        return
    computer_choice=my_computer_choice()
    print(f"computer chose:{computer_choice}")
    result=play_game(player_choice,computer_choice)
    print(result)


if __name__=="__main__":
    my_choice()