from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/ARYAN PATEL/Desktop/Tkinter folder/docs/index.png"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/ARYAN PATEL/Desktop/Tkinter folder/docs/index1.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/ARYAN PATEL/Desktop/Tkinter folder/docs/index3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/ARYAN PATEL/Desktop/Tkinter folder/docs/index4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/ARYAN PATEL/Desktop/Tkinter folder/docs/index5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=5)

count=0

def forward():
	global my_label
	global count
	my_label.grid_forget()
	if count<4:
		count = count + 1
	elif count==4:
		count=0
	my_label = Label(image=image_list[count])
	my_label.grid(row=0, column=0, columnspan=3)

def back():
	global my_label
	global count
	my_label.grid_forget()
	if count>=1:
		count=count-1
	elif count==0:
		count=4
	my_label = Label(image=image_list[count])
	my_label.grid(row=0, column=0, columnspan=3)

backButton = Button(root, text="<<", command=back).grid(row=1, column=0)
exitButton = Button(root, text="Exit", command=root.quit).grid(row=1, column=1)
forwardButton = Button(root, text=">>", command=forward).grid(row=1,column=2)

root.mainloop()