from tkinter import *

root = Tk()


# first_button = Button(root, text="click here")
# first_button = Button(root, text="click here", state=DISABLED)
# first_button = Button(root, text="click here", padx=10, pady=10)

def click_me():
    mylabel = Label(root, text="Hey you clicked me")
    mylabel.pack()

# first_button = Button(root, text="click here", command=click_me)
first_button = Button(root, text="click here", command=click_me, fg="blue", bg="yellow")
first_button.pack()
root.mainloop()

# we can change size of button with padx, pady
# fg--> text colour in button
# bg--> background clour of button