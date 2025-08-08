file = open("line2.txt", "r")
for line in file:
    if not line.startswith("In"):
        print(line)
