with open("listlines.txt", "w") as file:
    file.write("This is a new line.\n")
    file.close()

with open("listlines.txt", "r") as file:
    lines = file.readlines()
    print("Lines in the file:")
    for line in lines:
        print(line.split())
        print(lines)
