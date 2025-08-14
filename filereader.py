with open('test.txt', 'r') as file:
    for line in file:
        print(line.strip())

print("File operations completed successfully.")

with open('test.txt', 'r') as file:
    content = file.read()
    print(f"File content: {content}")