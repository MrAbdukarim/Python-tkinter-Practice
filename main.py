from tkinter import *

window = Tk()
window.title("Created by MrAbdukarim")
window.geometry('420x420')

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

text = Label(text="MrAbdukarim", font=152)
text.pack()

window.config(background='#333')

window.mainloop()