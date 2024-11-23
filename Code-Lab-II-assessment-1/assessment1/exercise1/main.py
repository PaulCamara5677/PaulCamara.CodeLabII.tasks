#Main python file for exercise 1 - Algorithmitic Math Quiz's window
#code by Paul Yram Bartolome Camara
from tkinter import *
from random import randint

root = Tk()
root.geometry("800x500")
root.title("Algorithmetic Math Quiz")

headingLabel = Label(root , text="Algorithmitic Math Quiz",  font= ('arial' , 20) )
headingLabel.grid(row=0 , column=0 )

number1 = randint(1 , 10)
print(number1)

root.mainloop