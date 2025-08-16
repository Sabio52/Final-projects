import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        label_result.config(text=f"Generated Password: {password}")
    except ValueError:
        label_result.config(text="Please enter a valid length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")

label_length = tk.Label(window, text="Enter password length:")
label_length.pack(pady=10)

entry_length = tk.Entry(window)
entry_length.pack(pady=5)
button = tk.Button(window, text="generate", command=generate_password, bg="blue", fg="white")
button.pack(pady=10)
label_result = tk.Label(window, text="")
label_result.pack(pady=10)



window.mainloop()
