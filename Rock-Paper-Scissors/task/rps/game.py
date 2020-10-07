from random import choice


def user_details() -> int:
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    score: int = 0

    ratings = open('rating.txt', 'r')
    for rating in ratings:
        values = rating.split()
        if user_name == values[0]:
            score = int(values[1])
            break
    ratings.close()
    return score


def decision(user_choice, computer_choice, score) -> int:
    winners = {"rock": {"scissors": "win", "paper": "lose"}, "scissors": {"paper": "win", "rock": "lose"},
               "paper": {"rock": "win", "scissors": "lose"}}
    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        return score + 50
    elif winners[user_choice][computer_choice] == "win":
        print(f"Win -> Well done. The computer chose {computer_choice} and failed")
        return score + 100
    else:
        print(f'Sorry, but the computer chose {computer_choice}')
        return score


def user_input():
    score_user: int = user_details()
    option: str = input()
    choices: list = ["rock", "paper", "scissors"]

    while option != "!exit":
        if option == "!rating":
            print(f"Your rating: {score_user}")
        elif option in choices:
            computer_option = choice(choices)
            score_user = decision(option, computer_option, score_user)
        else:
            print(f"Invalid input")

        option: str = input()

    print("Bye!")
 

user_input()
