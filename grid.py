import tkinter as tk

window = tk.Tk()
window.title("Grid Layout Example")
window.geometry("600x400")

for i in range(8):
    for j in range(8):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()