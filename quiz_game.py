
Print("This is the quiz game, play now!")

print("Welcome to my computer quiz!")
playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :) ")  

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU Stand for? ")
if answer.lower() == "graphic processing unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM Stand for? ")
if answer.lower() == "random access memory" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU Stand for? ")
if answer.lower() == "power supply unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Congratulations! You got " + str(score) + " correct answers!")
print("You got " + str((score/4) * 100 ) + "%")