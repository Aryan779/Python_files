from tkinter import *
import math
root=Tk()
root.title("Simple Calculator")
input_num = Entry(root,width=35)
input_num.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

#for putting number on screen
def put_num(number):
	#input_num.delete(0, END)
	current=input_num.get()
	input_num.delete(0, END)
	input_num.insert(0,str(current)+str(number))
	

num1Button = Button(root,text='1', padx=35, pady=15, command= lambda: put_num(1)).grid(row=1, column=0)
num2Button = Button(root,text='2', padx=35, pady=15, command= lambda: put_num(2)).grid(row=1, column=1)
num3Button = Button(root,text='3', padx=35, pady=15, command= lambda: put_num(3)).grid(row=1, column=2)

num4Button = Button(root,text='4', padx=35, pady=15, command= lambda: put_num(4)).grid(row=2, column=0)
num5Button = Button(root,text='5', padx=35, pady=15, command= lambda: put_num(5)).grid(row=2, column=1)
num6Button = Button(root,text='6', padx=35, pady=15, command= lambda: put_num(6)).grid(row=2, column=2)

num7Button = Button(root,text='7', padx=35, pady=15, command= lambda: put_num(7)).grid(row=3, column=0)
num8Button = Button(root,text='8', padx=35, pady=15, command= lambda: put_num(8)).grid(row=3, column=1)
num9Button = Button(root,text='9', padx=35, pady=15, command= lambda: put_num(9)).grid(row=3, column=2)

num0_Button = Button(root,text='0', padx=35, pady=15, command= lambda: put_num(0)).grid(row=4, column=1)

#clear screen
def clear_screen():
	input_num.delete(0, END)

def add_button():
	num1 = float(input_num.get())
	global first_num
	first_num = num1
	input_num.delete(0, END)
	input_num.insert(0,'+')

def sub_button():
	num1 = float(input_num.get())
	global first_num
	first_num = num1
	input_num.delete(0, END)
	input_num.insert(0,'-')

def mul_button():
	num1 = float(input_num.get())
	global first_num
	first_num = num1
	input_num.delete(0, END)
	input_num.insert(0,'*')

def div_button():
	num1 = float(input_num.get())
	global first_num
	first_num = num1
	input_num.delete(0, END)
	input_num.insert(0,'/')

def sin_button():
	num1 = float(input_num.get())
	input_num.delete(0, END)
	num2 = (num1*math.pi)/180
	answer = math.sin(num2)
	input_num.insert(0, str(answer))

def cos_button():
	num1 = float(input_num.get())
	input_num.delete(0, END)
	num2 = (num1*math.pi)/180
	answer = math.cos(num2)
	input_num.insert(0, str(answer))

def log_button():
	num1 = float(input_num.get())
	input_num.delete(0, END)
	answer = math.log(10,num1)
	input_num.insert(0, str(answer))

def ln_button():
	num1 = float(input_num.get())
	input_num.delete(0, END)
	a=math.e
	answer = math.log(a,num1)
	input_num.insert(0, str(answer))

def equal():
	second_num = str(input_num.get())
	
	if second_num[0]=='+':
		input_num.delete(0, END)
		b=second_num.replace('+','')
		answer = str(first_num + float(b))
	elif second_num[0]=='-':
		input_num.delete(0, END)
		b=second_num.replace('-','')
		answer = str(first_num - float(b))
	elif second_num[0]=='*':
		input_num.delete(0, END)
		b=second_num.replace('*','')
		answer = str(first_num * float(b))
	elif second_num[0]=='/':
		input_num.delete(0, END)
		b=second_num.replace('/','')
		answer =  first_num / float(b)
	else :
		return 

	input_num.insert(0, answer)

	


addButton = Button(root, text="+", padx=35, pady=15, command=add_button).grid(row=1, column=3)
subButton = Button(root, text="-", padx=35, pady=15, command=sub_button).grid(row=2, column=3)
mulButton = Button(root, text="*", padx=35, pady=15, command=mul_button).grid(row=3, column=3)
divButton = Button(root, text="/", padx=35, pady=15, command=div_button).grid(row=4, column=3)
sinButton = Button(root, text="sin", padx=35, pady=15, command=sin_button).grid(row=1, column=4)
cosButton = Button(root, text="cos", padx=35, pady=15, command=cos_button).grid(row=2, column=4)
logButton = Button(root, text="log", padx=35, pady=15, command=log_button).grid(row=3, column=4)
lnButton = Button(root, text="ln", padx=39, pady=15, command=ln_button).grid(row=4, column=4)
equalButton = Button(root, text="=", padx=35, pady=15, command=equal).grid(row=4, column=2)
clsButton = Button(root, text="C", padx=35, pady=15, command=clear_screen).grid(row=4, column=0)


root.mainloop()
