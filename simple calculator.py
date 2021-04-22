from _ast import Lambda
from tkinter import*
#creating the main window
root=Tk()
#defining title of the project
root.title("simple calculator")
e=Entry(root,bg="black",fg="white", width=40,borderwidth=15,justify="center",font=("Times",15,"bold"))
e.grid(row=0,column=0,columnspan=4,padx=15,pady=5,ipadx=15,ipady=5)
root.iconbitmap('a.ico')


def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0,END)

#function to add numbers
def button_add():
    first_number=e.get()
    global f_num
    global result
    result='add'
    f_num=int(first_number)
    e.delete(0,END)

#function to subtract numbers
def button_sub():
    first_number=e.get()
    global f_num
    global result
    result='sub'
    f_num= int(first_number)
    e.delete(0,END)

#function to multiply numbers
def button_mul():
    first_number=e.get()
    global f_num
    global result
    result='mul'
    f_num= int(first_number)
    e.delete(0,END)

#function to divide numbers
def button_div():
    first_number=e.get()
    global f_num
    global result
    result='div'
    f_num= int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if result=='add':
        e.insert(0, f_num + int(second_number))
    if result=='sub':
        e.insert(0, f_num - int(second_number))
    if result=='mul':
        e.insert(0, f_num * int(second_number))
    if result=='div':
        e.insert(0, f_num / int(second_number))





# defining the buttons
button_1=Button(root,bg="violet",fg="red", text='1', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(1)).grid(row=3, column=0)
button_2=Button(root,bg="violet",fg="red", text='2', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(2)).grid(row=3, column=1)
button_3=Button(root,bg="violet",fg="red", text='3', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(3)).grid(row=3, column=2)
button_4=Button(root,bg="violet",fg="red", text='4', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(4)).grid(row=2, column=0)
button_5=Button(root,bg="violet",fg="red", text='5', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(5)).grid(row=2, column=1)
button_6=Button(root,bg="violet",fg="red", text='6', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(6)).grid(row=2, column=2)
button_7=Button(root,bg="violet",fg="red", text='7', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(7)).grid(row=1, column=0)
button_8=Button(root,bg="violet",fg="red", text='8', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(8)).grid(row=1, column=1)
button_9=Button(root,bg="violet",fg="red", text='9', padx=40,pady=20,font=("times",10,"bold") , command=lambda : button_click(9)).grid(row=1, column=2)
button_0=Button(root,bg="violet",fg="red", text='0', padx=100,pady=20,font=("times",10,"bold") , command=lambda : button_click(0)).grid(row=4, column=0,columnspan=2)
button_add=Button(root,bg="cyan",fg="red",text='+',padx=60,pady=10,font=("times",15,"bold") ,command=button_add).grid(row=1, column=3)
button_sub=Button(root,bg="cyan",fg="red",text='-',padx=60,pady=10,font=("times",15,"bold") ,command=button_sub).grid(row=2, column=3)
button_mul=Button(root,bg="cyan",fg="red",text='*',padx=60,pady=10,font=("times",15,"bold") ,command=button_mul).grid(row=3, column=3)
button_div=Button(root,bg="cyan",fg="red",text='/',padx=120,pady=20,font=("times",10,"bold") ,command=button_div).grid(row=4, column=2,columnspan=2)
button_equal=Button(root,bg="pink",fg="black",text='=',padx=100,pady=20,font=("times",10,"bold") ,command=button_equal).grid(row=5, column=0,columnspan=2)
button_clear=Button(root,bg="pink",fg="black",text='clear',padx=110,pady=20,font=("times",10,"bold") ,command=button_clear).grid(row=5, column=2,columnspan=2)

root.mainloop()