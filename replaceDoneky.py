# Reading the file which contains Donkey
with open("donkey.txt","r") as f:
    text = f.read()

# replacing Donkey with ######
text1  = text.replace("Donkey","######")

# writing the updated text to the file 
with open ("donkey.txt","w") as f:
    f.write(text1)

