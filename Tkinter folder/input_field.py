from tkinter import *
root = Tk()

input_text = Entry(root,width=100 , fg="white", bg="black")
input_text.pack()
input_text.insert(0,"enter name or anything")

def click_me():
    mylabel = Label(root, text="your input: "+input_text.get())
    mylabel.pack()

first_button = Button(root, text="print that you entered", command=click_me, fg="blue", bg="yellow")
first_button.pack()
root.mainloop()