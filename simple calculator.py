from _ast import Lambda
from tkinter import*
#creating the main window
root=Tk()
#defining title of the project
root.title("simple calculator")
text=StringVar()
e=Entry(root,bg="black",fg="white",textvariable=text, width=40,borderwidth=15,justify="center",font=("Times",15,"bold"))
e.grid(row=0,column=0,columnspan=4,padx=15,pady=5,ipadx=15,ipady=5)
root.iconbitmap('a.ico')
#defining button function
operator=""


def button_click(number):
   global operator
   operator=operator+str(number)
   text.set(operator)
def button_clear():
    global operator
    operator=""
    text.set("")

def button_equal():
    global operator
    result=str(eval(operator))
    text.set(result)
    operator=""





# defining the buttons
# buttons for row 3
button_1=Button(root,bg="violet",fg="red", text='1', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(1)).grid(row=3, column=0)
button_2=Button(root,bg="violet",fg="red", text='2', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(2)).grid(row=3, column=1)
button_3=Button(root,bg="violet",fg="red", text='3', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(3)).grid(row=3, column=2)
# buttons for row 2
button_4=Button(root,bg="violet",fg="red", text='4', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(4)).grid(row=2, column=0)
button_5=Button(root,bg="violet",fg="red", text='5', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(5)).grid(row=2, column=1)
button_6=Button(root,bg="violet",fg="red", text='6', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(6)).grid(row=2, column=2)
# buttons for row 1
button_7=Button(root,bg="violet",fg="red", text='7', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(7)).grid(row=1, column=0)
button_8=Button(root,bg="violet",fg="red", text='8', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(8)).grid(row=1, column=1)
button_9=Button(root,bg="violet",fg="red", text='9', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(9)).grid(row=1, column=2)
#buttons for operators
button_add=Button(root,bg="cyan",fg="red",text='+',padx=60,pady=10,font=("times",15,"bold") ,command=lambda : button_click("+")).grid(row=1, column=3)
button_sub=Button(root,bg="cyan",fg="red",text='-',padx=60,pady=10,font=("times",15,"bold") ,command=lambda : button_click("-")).grid(row=2, column=3)
button_mul=Button(root,bg="cyan",fg="red",text='*',padx=60,pady=10,font=("times",15,"bold") ,command=lambda : button_click("*")).grid(row=3, column=3)
button_div=Button(root,bg="cyan",fg="red",text='/',padx=120,pady=20,font=("times",10,"bold") ,command=lambda : button_click("/")).grid(row=4, column=2,columnspan=2)
#remaining button
button_0=Button(root,bg="violet",fg="red", text='0', padx=100,pady=20,font=("times",10,"bold") , command=lambda : button_click(0)).grid(row=4, column=0,columnspan=2)
button_equal=Button(root,bg="pink",fg="black",text='=',padx=100,pady=20,font=("times",10,"bold") ,command=button_equal).grid(row=5, column=0,columnspan=2)
button_clear=Button(root,bg="pink",fg="black",text='clear',padx=110,pady=20,font=("times",10,"bold") ,command=button_clear).grid(row=5, column=2,columnspan=2)

root.mainloop()