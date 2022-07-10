f = open("poems.txt","r")
t = f.read()
if 'Twinkle' in t:
    print("twinkle is present ")
else:
    print("twinkle is not present in the file")
f.close()