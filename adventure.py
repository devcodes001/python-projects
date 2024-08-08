name = input("type your name: ")
print("Welcome",name,"to this adventure!")
print("You are on a dirt road,it has come to an end and you can go left or right , Which way do you like to go?")
answer = input("type (left/right) to continue").lower()

if answer == 'left':
    answer = input("You come to a river,you can walk around it or swim across | enter (swim/walk): ").lower()
    if answer == 'swim':
        print("you swam across and were eaten by an alligator")
    if answer == 'walk':
        print("You walked for many miles ,ran out of water and died , LOST!!!!")
    else:
        print("Not a valid option you loose!!")

elif answer == "right":
    answer = input("you came across a bridge,it looks wobbly ,do you want to cross or go back type(back/lose").lower()

    if answer == "back":
        print("You go back and lose")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger do you want to talk to him type[yes/no]").lower()
        if answer == "yes":
           print("You talk to the stranger and you were rewarded with gold")
           print("You won!!!")
        elif answer == 'no':
            print("you ignore the stranger and missed a fortune of plenty gold")
            print("You lost!!!!")
        else:
             print("invalid input you lost")
else:
    print("invalid input you lost")