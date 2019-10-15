import random


class dice:
    pass


def main(input3=None):
    global input2, input4
    print("Hello this is a dice gam between two players player 1 and player 2 you will need to log in first tho")

    input1 = input("please log in player one type your username")

    if input1 == "player1":
        input2 = input("please type your password")
    else:
        input1 = input("please log in player one type your username")

    if input2 == "password1":
        print("welcome to the game")

    else:
        input2 = input("please type your password")

    if input3 == "player2":
        print("welcome to the game")

    else:
        input3 = input("please type your username player2")

        input4 = input("player2 please type your password")

    if input4 == "password2":
        print("welcome to the game")

    else:
        input4 = input("please type your password playerd")

    game()

def game():
    print("this is now the actual game the rules are simple you get two dice roles each and there are 5 rounds of the "
           "game and the persdn with the highest score at the ends wins")

    input1 = input("please type roll to roll the dice")

    if input1 == "roll":
        print(random.randint(0, 6))
    else:
        input1 = input("please type roll to begin")

if __name__ == '__main__':
    main()
