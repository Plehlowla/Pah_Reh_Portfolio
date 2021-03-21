import random

print("Let's Play!\nDifficulty is 1 to 10!")

secret = random.randint(1,10)

guess = None
count = 1

while guess != secret:
    guess = input('Please guess a number between 1 to 10: ')

    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print('Congrats you got it! the number was ' + str(secret))
    else:
        print('Please try again!')
        count += 1

print('It took you', count, 'guesses!')

#Credit : Tech With Tim
