from tkinter import *
root = Tk()
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Aryan")
myLabel3 = Label(root, text="               ").grid(row=1, column=0)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=10, column=0)


# you can also write as
# myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
# myLabel2 = Label(root, text="My name is Aryan").grid()


root.mainloop()
