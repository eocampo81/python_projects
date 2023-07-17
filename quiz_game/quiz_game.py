
print("Welcome to my Data Engineering quiz!")

playing = input("Do you want to play (yes or no)? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

correct = 0
incorrect = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    correct = correct + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    correct = correct + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    correct = correct + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct")
    correct = correct + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1

print("Thanks for playing!")
print("Number of correct answers: ", correct)
print("Number of incorrect answers: ", incorrect)
print("You got "+ str((correct / (correct+incorrect))*100) + "%.")
