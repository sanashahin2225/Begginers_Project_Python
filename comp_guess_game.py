import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry guess again too low!")
        elif guess > random_number:
            print("Sorry guess again too high!")

    print(f'yaayyy...Congrats...You have guess the number {random_number}')

guess(50)
