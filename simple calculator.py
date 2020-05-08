from  tkinter import *
from math import *
root=Tk()
#function for calculating the mathematical calculation
def calculation(event):
    text=event.widget.cget("text")
    print(text)
    if(text=='='):
        x=screen.get()
        result=eval(x)
        screen.delete(0,END)
        screen.insert(END,result)
    elif(text=='+' or text=='-' or text=='*' or text=='/'):
        screen.insert(END,text)
    elif(text=='C'):
        x=screen.delete(0,END)
    elif (text=='sqrt' or text=='cube'):
        screen.insert(END,'NOT BUILT IN')
    else:

        screen.insert(END,text)



root.title('CALCULATOR')
root.geometry('400x550')
root.resizable(0,0)

#first create the entry widget
screen=Entry(root ,font=("Times", 25, "bold"),bd=10,foreground='springgreen4')
screen.pack(fill=X,ipady=10)

frame=Frame(root,height=120,width=400)
b=Button(frame,text='9',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='8',font=('lucid',20),padx=10,pady=5,border=5,width=5,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='7',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=RIGHT,padx=5,pady=5)

frame.pack()

frame=Frame(root,height=120,width=400)
b=Button(frame,text='6',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='5',font=('lucid',20),padx=10,pady=5,border=5,width=5,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='4',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=RIGHT,padx=5,pady=5)

frame.pack()



frame=Frame(root,height=120,width=400)
b=Button(frame,text='3',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='2',font=('lucid',20),padx=10,pady=5,border=5,width=5,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='1',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=RIGHT,padx=5,pady=5)

frame.pack()


frame=Frame(root,height=120,width=400)
b=Button(frame,text='+',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='-',font=('lucid',20),padx=10,pady=5,border=5,width=5,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='*',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=RIGHT,padx=5,pady=5)

frame.pack()


frame=Frame(root,height=120,width=400)
b=Button(frame,text='/',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='0',font=('lucid',20),padx=10,pady=5,border=5,width=5,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='C',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=RIGHT,padx=5,pady=5)

frame.pack()


frame=Frame(root,height=120,width=400)
b=Button(frame,text='sqrt',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='cube',font=('lucid',20),padx=10,pady=5,border=5,width=5,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(frame,text='=',font=('lucid',20),padx=10,pady=5,border=5,width=6,background='gray57')
b.bind("<Button-1>",calculation)
b.pack(side=RIGHT,padx=5,pady=5)

frame.pack()
root.mainloop()
