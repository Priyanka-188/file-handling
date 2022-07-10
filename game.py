import random 
 
# function to get random value of score using random module
def game():
    score =random.randint(1,1000)
    return score

# reading the highscore from the file 
with open("hiscore.txt", "r") as f:
    hiscore = f.read()

print("The current high score is ", hiscore)
scores = game()     # taking the score by calling the game function

# updating the hiscore if the score is greater than the current highscore
if scores > int(hiscore):
    with open("hiscore.txt", "w") as f:
        f.write(str(scores))
elif hiscore == "":
    with open("hiscore.txt", "w") as f:
        f.write(str(scores))

# Printing the current high score in the hiscore.txt file 
with open("hiscore.txt", "r") as f:
    value = f.read()
print("The new hishscore is :", value)
