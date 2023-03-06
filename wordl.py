again = 'yes'
print('Welcome to the Word Guessing Name!')
print('')
while again == 'yes':
    guess = input('What is your guess? ')
    magic_word = 'mosiah'
    number_guess = 1
    correct_letter = ''

    while guess != magic_word:
        guess = input('What is your new guess? ')
        if guess != magic_word:
            for i in range(len(magic_word)):
                if guess[i]==magic_word[i]:
                    correct_letter += guess[i]
                else:
                    print('_')
            print (f'Hint: {correct_letter}')
            number_guess = 1
            correct_letter = ''

        else:
            print('')
        number_guess += 1
        correct_letter = ''
    print(f'You guessed right! It took you {number_guess} tries.')
    again = input('Do you want to keep playing again? ').lower ()
print ('Thank you for playing! :)')