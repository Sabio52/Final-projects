from tkinter import *

window = Tk()
window.title("My Tkinter Window")   
window.geometry("400x300")

label = Label(master=window, text="Hello, Tkinter!", fg="blue", bg="lightgray")
button = Button(master=window, text="Click Me", bg="lightblue", fg="black")
box = Entry(master=window, width=20, bg="white", fg="black")

label.pack()
button.pack()
box.pack()

frame = Frame(master=window, bg="lightgreen", relief="raised", bd=2)
frame.pack()
label2 = Label(master=frame, text="This is a frame", bg="lightgreen")
label2.pack()

textbox = Text(master=window, bg="white", fg="black")
textbox.pack()

window.mainloop()