import random
c_score = 0
u_score = 0
a = ['rock','scissors','paper']
while True:
    user_input = input("enter Rock/Paper/Scissors or q to quit : ").lower()
    if user_input == 'q':
        break
    if user_input not in ['rock','scissors','paper']:
        continue
    else:
        r = random.randint(0,2)
        c = a[r]
        if user_input == 'paper' and c == 'rock':
          print(f"you : {user_input} | computer :{c}")
          print("You Won got 1 point! ")
          u_score += 1
          continue
        elif user_input == 'rock' and c == 'scissors':
            print(f"you : {user_input} | computer :{c}")
            print("You won got 1 point! ")
            u_score += 1
            continue
        elif user_input == 'scissors' and c == 'paper':
            print(f"you : {user_input} | computer :{c}")
            print("You won got 1 point!")
            u_score += 1
            continue
        elif user_input == c:
            print(f"you : {user_input} | computer :{c}")
            print("Tie , No points!")
        else:
            print(f"you : {user_input} | computer :{c}")
            print("I won got 1 point!")
            c_score += 1
            continue

print("----------------------")
if u_score == c_score:
    print("Final standing")
    print(f"you : {u_score} | computer :{c_score}")
    print("Tie")
elif u_score > c_score:
    print("Final standing")
    print(f"you : {u_score} | computer :{c_score}")
    print("you won the  game")
elif u_score < c_score:
    print("Final standing")
    print(f"you : {u_score} | computer :{c_score}")
    print("I won the game")
print("Good bye!!!")
print("----------------------")