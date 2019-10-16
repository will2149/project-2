import random


class dice:
    pass


def main():
    global input2, input4
    print("Hello this is a dice game between two players player 1 and player 2 you will need to log in first tho")

    input1 = input("please log in player one type your username")

    if input1 == "player1":
        input2 = input("please type your password")
    else:
        var = input1 == "player1"

    if input2 == "password1":
        print("welcome to the game")

    else:
        var = input2 == "password1"

    input3 = input("please type your username player2")

    if input3 == "player2":
        input4 = input("please type your password player2")

    else:
        var = input3 == "player2"

    if input4 == "password2":
        print("welcome to the game")

    else:
        var = input4 == "password2"

    game()


def game(total=None):
    global input5
    input6: int = 0
    input7: int = 0
    print("this is now the actual game the rules are simple you get two dice roles each and there are 1round of the "
          "game and the person with the highest score at the ends wins")

    input1 = input("please type roll to roll the dice")

    if input1 == "roll":
        input6 = (random.randint(0, 6))
        print(input6)
    else:
        if input1 == "roll":
            input6 = (random.randint(0, 6))
            print(input6)
    input1 = input("please type roll to begin your second role player 1")

    if input1 == "roll":
        input7 = (random.randint(0, 6))
        print(input7)
    else:
        if input1 == "roll":
            input7 = (random.randint(0, 6))
            print(input7)
    total1: int = int(input6) + int(input7)
    print("your total is", total1)

    input8 = input('player 2 it is you go now please type roll to begin your first dice roll')

    if input8 == "roll":
        input5 = (random.randint(0, 6))
        print(input5)

    input9 = input('please type roll for your second go')

    if input9 == "roll":
        input6 = (random.randint(0, 6))
        print(input6)

    total2: int = int(input5) + int(input6)
    print('your total is', total2)

    if total1 > total2:
        print('player1 you win')
    else:
        print('player2 you win')


if __name__ == '__main__':
    main()
