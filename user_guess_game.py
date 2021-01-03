import random

def computer_guess(x):
    low,high,feedback=1,x,''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C):').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The computer guessed the number correctly {guess}')
    
computer_guess(80)
