print()
word = 'commitment'
fav_letter = input('What is your favorite letter? ').lower()

for i,letter in enumerate (word):
    if fav_letter == letter: 
        print(f'{letter.upper()}')
    else: 
        print(letter)
    
    
    