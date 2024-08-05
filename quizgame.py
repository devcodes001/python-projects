print('~'*10)
print("QUIZ GAME")
print('~'*10)
a = input("DO you want to play (yes/no): ")
print("~"*30)
if a.lower()=='yes':
    print("Let's Play !!!!!!")
else:
    quit()
print("~"*30)
q = {
    "What is 2 + 2?":"4",
    "What shape has three sides?":"triangle",
    "How many days are there in a week?":"7",
    "What is 5 - 3?":"2",
    "What is the first month of the year?": "january",
    "What color are bananas?": "yellow",
    "How many legs does a spider have?": "8",
    "What is 3 + 4?": "7",
    "How many hours are there in a day?": "24",
    "What is the opposite of hot?": "cold"
}
s=1
c=0
for j,k in q.items():
    print("-" * 10)
    print(f"Question {s}")
    print("-"*10)
    s+=1
    print(j)
    b=input("Enter Your answer :")
    if k.isnumeric:
        if str(b) == k:
            print("Correct!!!")
            c+=1
        else:
            print("Incorrect!!!")
    else:
        if b.lower() == k:
            print("Correct!!!")
            c+=1
        else:
            print("Incorrect!!!")
print()
print("$"*20)
print()
print(f"Your score is {c}")
print(f"you got {(c/len(q))*100}")
print()
print("$"*20)
# print("--------------------------------")
# print("Welcome to my computer quiz!!")
# print("--------------------------------")
# playing = input("Do you want to play? : ")
#
# if playing.lower() != "yes":
#     quit()  #immediatly quit the program
# score = 0
# print("Okay! Let's Play :)")
#
# answer = input("what does CPU stand for ? ").lower()
# if answer == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("incorrect!")
#
# answer = input("What does GPU stand for? ").lower()
# if answer == "graphics processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("incorrect!")
#
# answer = input("What does RAM stand for? ").lower()
# if answer == "random access memory":
#     print("Correct!")
#     score += 1
# else:
#     print("incorrect!")
#
# answer = input("What does ROM stand for? ").lower()
# if answer == "read only memory":
#     print("Correct!")
#     score += 1
# else:
#     print("incorrect!")
# print("--------------------------------")
# print(f"Your score is {score}")
# print(f"you got {(score/4)*100}")
# print("--------------------------------")