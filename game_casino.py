from random import randint
from decouple import config

# print('hello world')

def prize_number():
    money = config('MY_MONEY', cast=int)
    balance = money
    print(f"Your starting balance is: {balance}")
    while True:
        random_list = randint(1, 31)
        bet = int(input("Make your bet: "))
        if bet > balance:
            print("Yuo are out of balance")
            continue
        slot_of_numbers = int(input("Choose slot: "))
        if slot_of_numbers > 30:
            print("Choose slot from 1 to 30")
            continue
        if slot_of_numbers == random_list:
            balance += bet * 2
        else:
            balance -= bet
        print(f"Prize slot is: {random_list}")
        continue_game = input("Wish you to continue game : yes/y or no/n").lower()
        if continue_game == "yes":
            print(f"Your balance is: {balance}$")
            continue
        elif continue_game == 'no':
            print(f"Your balance is: {balance}$")
            break
        else:
            print("Enter yes/y or no/n to continue or stop the game")


if __name__ == '__main__':
    prize_number()

