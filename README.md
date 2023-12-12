# Spele-2
from tkinter import*
from tkinter import messagebox 
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")


myimg0=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg1=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg7=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg8=ImageTk.PhotoImage(Image.open("cat1.jpg"))
myimg9=ImageTk.PhotoImage(Image.open("cat1.jpg"))


bgImg=ImageTk.PhotoImage(Image.open("cat1.jpg"))

btn0=Button(width=5,height=4)
btn1=Button(width=5,height=4)
btn2=Button(width=5,height=4)
btn3=Button(width=5,height=4)
btn4=Button(width=5,height=4)
btn5=Button(width=5,height=4)
btn6=Button(width=5,height=4)
btn7=Button(width=5,height=4)
btn8=Button(width=5,height=4)
btn9=Button(width=5,height=4)


btn0.grid(row=1,column=0)
btn1.grid(row=2,column=0)
btn2.grid(row=3,column=0)
btn3.grid(row=1,column=1)
btn4.grid(row=2,column=1)
btn5.grid(row=3,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=2)
btn8.grid(row=3,column=2)
btn9.grid(row=1,column=3)




btn0=Button(width=200, height=300, image=bgImg)
btn1=Button(width=200, height=300, image=bgImg)
btn2=Button(width=200, height=300, image=bgImg)
btn3=Button(width=200, height=300, image=bgImg)
btn4=Button(width=200, height=300, image=bgImg)
btn5=Button(width=200, height=300, image=bgImg)
btn6=Button(width=200, height=300, image=bgImg)
btn7=Button(width=200, height=300, image=bgImg)
btn8=Button(width=200, height=300, image=bgImg)
btn9=Button(width=200, height=300, image=bgImg)



gameWindow.mainloop()
