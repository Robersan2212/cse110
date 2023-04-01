x = 0
max_life = -1
year = -1
country = ""
y = 0
min_life = 1000
years = 1000
countries = ""
average = 0
sum_life = 0
life1 = 1000
year1 = 1000
country1 = ""
life2 = -1
selection = 'yes'
year2 = -1
country2 = ""
print()
choice = int(input("Enter the year of interest: ")) 
print()
with open("life-expectancy.csv") as life_file:
    for line in life_file:
        x += 1
        life = line.strip()
        parts = life.split(",")            
        if x > 1:
            country = parts[0]
            year = int(parts[2])
            age = float(parts[3])
            if max_life < age:
                max_life = age
                year = year                
                country = country                                
            if min_life > age:
                min_life = age
                years = year                
                countries = country                                                 
            if choice == year:
                sum_life += age      
                y += 1                           
                if life2 < age:
                    life2 = age
                    year2 = year
                    country2 = country  
                if life1 > age:
                    life1 = age
                    year1 = year
                    country1 = country                   
average = sum_life / y      
print(f"The overall max life expectancy is: {max_life} from {country} in {year}")
print(f"The overall min life expectancy is: {min_life} from {countries} in {years}")
print()
print(f"For the year {choice}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {country2} with {life2}")
print(f"The min life expectancy was in {country1} with {life1}")
print()
            
again = input("Was this information helpful? ")
if again != 'yes':
    print('We are sorry that this information was not helpful.')
else:
    print('Thank you for letting us know. Have a good day.')
