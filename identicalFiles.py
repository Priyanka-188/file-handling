file1 = "log.txt"
file2 = "listwords.txt"

with open("log.txt") as f1:
    text1 = f1.read()
with open("listwords.txt") as f2:
    text2 = f2.read()

if text1 == text2:
    print("Files are identical ")
else:
    print("Files are different")