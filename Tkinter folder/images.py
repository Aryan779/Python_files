from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Facebook")
root.iconbitmap('C:/Users/ARYAN PATEL/Downloads/favicon.ico')

my_img = ImageTk.PhotoImage(Image.open("3.png"))
myLabel = Label(image=my_img)
myLabel.pack()

exitButton = Button(root, text="Program exit", padx=35, pady=15, command=root.quit)
exitButton.pack()

root.mainloop()

# remember to use .ico format for images, to convert it into .ico check online converter
