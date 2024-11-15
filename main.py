from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Programming")
window.config(background="#333")

# win_text = Text(window, text="Hello World!")World

# label = Label(window, text="Hello World!", font=("Arial", 30, "bold"))
# label.pack()
# label.place(x=0, y=100)

button = Button(window, text="Click Me!!!", padx=10, pady=10)
button.pack()

window.mainloop()
