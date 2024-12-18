# loop
# ask roll the dice
# if user enter y
# generate two random number
#print them
# if user enter n
# Print thank you message
# terminate
# else
# print invalid choice

import random

while True:
 choice =input("Rool the dice? (y/n):").lower()
 if choice == "y":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f'({die1},{die2})')
 elif choice =='n':
    print('Thank you for playing !!!')
    break
else:
    print('invalid choice')
    