## hello the is the second game of this mini apps folder


import random

user_number = input('type a number:')

# block of the top ran

if user_number.isdigit():
    user_number = int(user_number)

    if user_number <= 0:
        print('please choose a number larger than 0')

        quit()
        # this method is used to stop the programme and quit from it
else:
    print('please enter a number next time')
    quit()

random_number = random.randint(0, user_number)

#the while loop block

count = 0
while True:
    count +=1
    user_guess = input('make a guess: \n')

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('please enter a number next time')
        continue

    if user_guess == user_number:
        print('you got it')
        break
    elif user_guess > user_number:
        print('you were above the number ')
    elif user_guess < user_number:
        print('you were below the number')

print('you got it in ', count,'guesses')




