from tkinter import*
from tkinter import messagebox 
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")



count=0
correctAnswer=0
Answer=[]
Answer_dict={}

def btnClick(btn, number)
    global count, correctAnswer,Answer, Answer_dict
if btn["bg.jpg"]=="pyimage1" and count<2:
    btn["bg.jpg"]=ImageList[number]
    count+=1
    Answer.append(number)
    Answer_dict[btn]=ImageList(number)

if len(Answer)==2:
if ImageList(answer[0]==ImageList[Answer[1]])

for key in Answer_dict:
key["state"]=DISABLED
if correctAnswer==2
else:
    messagebox.showinfo("VIENADI")
    for key Answer_dict:
        key["image"]="pyimage6"
count=0
Answer=[]
Answer_dict={}
return 0

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


bgImg=ImageTk.PhotoImage(Image.open("bg.jpg"))



ImageList=[myimg0,myimg0,myimg1,myimg1,myimg2,myimg2,myimg3,myimg3,myimg4,myimg4,]
random.shuffle(ImageList)

btn0=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn1,0))
btn1=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn2,1))
btn2=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn3,2))
btn3=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn4,3))
btn4=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn5,4))
btn5=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn6,7))
btn6=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn8,9))
btn7=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn9,10))
btn8=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn9,0))
btn9=Button(width=5,height=4,image=bgImg command=lambda:btnClick(btn1,0))


btn0.grid(row=1,column=0)
btn1.grid(row=2,column=0)
btn2.grid(row=1,column=4)
btn3.grid(row=1,column=1)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=3)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=2)
btn8.grid(row=2,column=4)
btn9.grid(row=1,column=3)




#btn0=Button(width=200, height=300, image=bgImg)
#btn1=Button(width=200, height=300, image=bgImg)
#btn2=Button(width=200, height=300, image=bgImg)
#btn3=Button(width=200, height=300, image=bgImg)
#btn4=Button(width=200, height=300, image=bgImg)
#btn5=Button(width=200, height=300, image=bgImg)
#btn6=Button(width=200, height=300, image=bgImg)
#btn7=Button(width=200, height=300, image=bgImg)
#btn8=Button(width=200, height=300, image=bgImg)
#btn9=Button(width=200, height=300, image=bgImg)







gameWindow.mainloop()
