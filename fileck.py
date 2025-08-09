import os

# Create and close the file
new_file = open("new_file.txt", "w")
new_file.close()

print("checking file existence...")
if os.path.exists("new_file.txt"):
    print("File exists.")
else:
    print("File does not exist.")
print("File operations completed successfully.")

new_file = open("new_file.txt", "w")
new_file.write("This is a new file created for testing purposes.\n")
new_file.close()