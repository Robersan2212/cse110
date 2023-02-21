again = 'yes'
print('Welcome to the Word Guessing Name!')
print('')
while again == 'yes':
    guess = input('What is your guess? ')
    magic_word = 'mosiah'
    number_guess = 1

    while guess != magic_word:
        if guess != magic_word:
            print('Wrong answer.')
            guess = input('What is your new guess? ')
        else:
            print('error')
        number_guess += 1
    print(f'You guessed right! It took you {number_guess} tries.')
    again = input('Do you want to keep playing again? ').lower ()
print ('Thank you for playing! :)')

