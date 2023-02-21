import random
again = 'yes'
while again == 'yes':
    number = random.randint(1, 100)
    guess = int(input('What is your guess? '))
    number_of_guesses = 1

    while guess != number:
        if guess > number:
            print ('Lower')
            guess = int(input('What is your new guess? '))
        elif guess < number:
            print('Higher')
            guess = int(input('What is your new guess? '))
        number_of_guesses += 1
    print(f'You got it! It took you {number_of_guesses} tries. ')

    again = (input ("Do you want to keep playing? ")).lower()

print('Thank you for playing :)')
    