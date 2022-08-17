

print("Welcome to my general knowledge quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! Let's Play!")

score = 0 

# lower() added so all answers are in lowercase. after each question if the answer is correct. 1 will be added to score.

answer = input("How many bones does an adult human have? ")
if answer.lower() == "206":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Who is the worlds fastest man? ")
if answer.lower() == "usain bolt":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many weeks n a year? ")
if answer.lower() == "52":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Spain? ")
if answer.lower() == "madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many birthdays are there? ")
if answer.lower() == "366":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
#i have now added a string to the end of the quiz. the string with print out how many quesions you got correct.

print("You got " + str(score) + " questions correct!")
print("Thank you for takng part in my terminal game! I hope you had fun!")

