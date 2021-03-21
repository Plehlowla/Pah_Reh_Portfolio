import random

flag = True
while flag:
    num = input('Select Difficulty, 1 to ')

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False
    else:
        print('Invalid input! Try Again! *Hint : Pick a number*')

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    guess = input('Please guess a number between 1 to ' + str(num) + ': ')

    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print('Congrats you got it! the number was ' + str(secret))
    elif guess < secret:
        print('Higher!')
        count += 1
    elif guess > secret:
        print('Lower!')
        count += 1
        
        

print('It took you', count, 'guesses!')