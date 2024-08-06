import random

number = input("Enter a number: ")
if number.isdigit():
   number = int(number)
else:
    print("""NOTE: please enter a digit ,if digit enter a value greater than zero""")
random_number = random.randint(0,number)
guesses =0
while True:
    guesses += 1
    user_guess = input("make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number(greater than zero)")
        continue
    if user_guess == random_number:
        print("Correct : you guessed it buddy!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number !")
print("you got it in",guesses,"guesses")
