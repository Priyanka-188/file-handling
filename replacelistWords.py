words = ["Donkey","kaddu","fattu"]

with open("listwords.txt") as f:
    content = f.read()

for word in words :
    content = content.replace(word,"#$@%^#$@&")
    with open("listwords.txt","w") as f:
        f.write(content)
