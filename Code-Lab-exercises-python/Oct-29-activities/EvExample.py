#import tkinter module and messagebox
from tkinter import *
import tkinter.messagebox
# Set the output window
root = Tk()
root.title('Display Name')
root.geometry('400x200')
root.config(bg='#234567')

root.mainloop() 


#Create a label 
l1 = Label(root, text = "Enter Name",
bg='#234567',fg="white",font=("tahoma",12))
l1.place(x=10, y=20)

#Create entry widget
e1 = Entry(root,font=("tahoma",12),textvariable = type)
e1.place(x=120, y=20)

#Create a button
b1 = Button(root, text = "Show Name", fg="yellow", bg="#001111"
,font=("tahoma",12),command = Button )
b1.place(x=140,y=60)

#Create a label to display name
l2 = Label(root, text = "Your Name is ",
bg='#234567',fg="white",font=("tahoma",12))
l2.place(x=10, y=100)
#create a variable to store user name from entry widget
user_name=StringVar()

# Create the Event handler function onClick()
def onClick():
	# get the value entered by user in the entry using get()
	name = user_name.get()

	# Append the name at the end of the Label2 text
	s = f' Your name is : {name}'
	l2.configure(text=s)  
