"""
Question: In Bagels, a deductive logic game, you 
must guess a secret three-digit number 
based on clues. The game offers one of 
the following hints in response to your guess: 
“Pico” when your guess has a correct digit in the 
wrong place, “Fermi” when your guess has a correct 
digit in the correct place, and “Bagels” if your guess 
has no correct digits. You have 10 tries to guess the 
secret number;

output: in output_bagels.py

"""

#import modules

import pprint 
import random

#Steps

# 1. Tell the user what the game is about

print('Welcome to bagels test your cognitive prowess 🦍\nDesigned by SJA\n')
print('These are the rules of the game:\n\t1. I will generate a three digit number\n\t2. I will then ask you to enter these 3 digit numbers at a go.')
print("\n\t3. if I say 'Fermi' it means one correct digit in the correct place\n\t4. if I say 'Pico' it means one correct digit at a wrong place\n\t5. if i say 'Bagels' it means no correct digits ")

print('\n   YOU HAVE 10 ATTEMPTS')





# 2. Generate a 3 digit secret number

three_digit_number = []
for num in range(3):
    rand_num=random.randint(0,9)
    three_digit_number.append(rand_num)
    
print(f'Create list{three_digit_number}')


# 3. Ask user to enter the 3 digit secret number
user_input = input('Enter a 3 digit number >> ')

print(f' Guess #{1} {user_input}')
# 4. After receiving the input show hints

user_input=list(user_input) # returns a list of strings

print(user_input)

def counter(d,v):
    if v in d:
        d[v]+=1
    else: d[v]=1

hints = {}
for id_ai, num in enumerate(three_digit_number):
    for id_user, num_str in enumerate(user_input):
        if id_ai==id_user and num==int(num_str): #convert num str for comparison
            counter(hints,'Fermi')
        elif id_ai!=id_user and num==int(num_str):
           counter(hints,'Pico')
        else: counter(hints,'Bagels')

print(hints)
        
        

            
        




# Hints:
#   a. Pico means one digit is correct but in the wrong place
#   b. Fermi means one correct digit in the correct place
#   c. Bagels no correct answer.    

# Repeat for 10 times