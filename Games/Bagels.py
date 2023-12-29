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
def get_three_digit_number():
    three_digit_number = []
    for num in range(3):
        rand_num=random.randint(0,9)
        three_digit_number.append(rand_num)
        
    print(f'Create list{three_digit_number}') #to be removed
    
    return three_digit_number


# 3. Ask user to enter the 3 digit secret number
def get_user_input():
    user_input = input('Enter a 3 digit number >> ')

    print(f' Guess #{1} {user_input}')
    # 4. After receiving the input show hints

    user_input=[int(x) for x in user_input] # process the input

    print(user_input)
    
    return user_input

def compare(user_input, three_digit_number):
    hints = []
    #base case
    if user_input==three_digit_number:
        print('Great you got it correct')
        return 'correct'
    else:
        for num in range(len(user_input)):
            if user_input[num]==three_digit_number[num]:
            #correct input at the same index
                hints.append('Fermi')
            #correct input at different position
            elif user_input[num] in three_digit_number:
                hints.append('Pico')
            
    if len(hints)==0:
        print('Bagels')
    else: hints.sort()

    return ' '.join(hints)



#print(hints)
        
        

            
        




# Hints:
#   a. Pico means one digit is correct but in the wrong place
#   b. Fermi means one correct digit in the correct place
#   c. Bagels no correct answer.    

# Repeat for 10 times


def main():
    while True:
        num_iterations=10
        
        #generate the 3 digit number
        three_digit_number=get_three_digit_number()
        
        attempts=0
        while attempts < num_iterations:
            user_input=get_user_input()
            results=compare(user_input,three_digit_number)
            if 'correct' in results:
                break
            attempts += 1
            print(f'{results}\nyou have {10-attempts} attempts left')
        prompt=input('Would you want to play again: yes/no').lower()
        if prompt.startswith('y'):
            continue
        else: break
    print('Thanks for playing')

            
        
#Ask User if they want to play again


    
        
if __name__ == "__main__":
    main()
    
    
    