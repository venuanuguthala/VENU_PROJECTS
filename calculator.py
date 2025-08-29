import tkinter as tk
t= ''
def field1(th):
    global t
    t+=str(th)
    field.delete("1.0","end")
    field.insert("1.0",t)
def calculate():
    global t
    res=str(eval(t))
    field.delete("1.0","end")
    field.insert("1.0",res)
def clear():
    global t
    t=""
    field.delete("1.0","end")
def C():
    global t
    field.delete("end-2c", "end-1c")
    t=""

    
root=tk.Tk()
root.title("Simple calculator")
root.geometry("350x420")
root.configure(bg="light blue")
field=tk.Text(height=5,width=42)
field.grid(row=1,column=1,columnspan=10)
b9=tk.Button(root,text="9",command=lambda:field1(9),width=5,font=("Times new roman",20))
b9.grid(row=2,column=3)
b8=tk.Button(root,text="8",command=lambda:field1(8),width=5,font=("Times new roman",20))
b8.grid(row=2,column=2)
b7=tk.Button(root,text="7",command=lambda:field1(7),width=5,font=("Times new roman",20))
b7.grid(row=2,column=1)
b6=tk.Button(root,text="6",command=lambda:field1(6),width=5,font=("Times new roman",20))
b6.grid(row=3,column=3)
b5=tk.Button(root,text="5",command=lambda:field1(5),width=5,font=("Times new roman",20))
b5.grid(row=3,column=2)
b4=tk.Button(root,text="4",command=lambda:field1(4),width=5,font=("Times new roman",20))
b4.grid(row=3,column=1)
b1=tk.Button(root,text="1",command=lambda:field1(1),width=5,font=("Times new roman",20))
b1.grid(row=4,column=1)
b2=tk.Button(root,text="2",command=lambda:field1(2),width=5,font=("Times new roman",20))
b2.grid(row=4,column=2)
b3=tk.Button(root,text="3",command=lambda:field1(3),width=5,font=("Times new roman",20))
b3.grid(row=4,column=3)
b0=tk.Button(root,text="0",command=lambda:field1(0),width=5,font=("Times new roman",20))
b0.grid(row=5,column=1)
b=tk.Button(root,text=".",command=lambda:field1("."),width=5,font=("Times new roman",20))
b.grid(row=5,column=2)
bc=tk.Button(root,text="AC",command=lambda:clear(),width=5,font=("Times new roman",20))
bc.grid(row=5,column=3)
bt=tk.Button(root,text="/",command=lambda:field1("/"),width=5,font=("Times new roman",20))
bt.grid(row=5,column=4)
b22=tk.Button(root,text="+",command=lambda:field1("+"),width=5,font=("Times new roman",20))
b22.grid(row=4,column=4)
b33=tk.Button(root,text="-",command=lambda:field1("-"),width=5,font=("Times new roman",20))
b33.grid(row=3,column=4)
b44=tk.Button(root,text="*",command=lambda:field1("*"),width=5,font=("Times new roman",20))
b44.grid(row=2,column=4)
b85=tk.Button(root,text="(",command=lambda:field1("("),width=5,font=("Times new roman",20))
b85.grid(row=6,column=1)
b86=tk.Button(root,text=")",command=lambda:field1(")"),width=5,font=("Times new roman",20))
b86.grid(row=6,column=2)
b87=tk.Button(root,text="%",command=lambda:field1("%"),width=5,font=("Times new roman",20))
b87.grid(row=6,column=3)
b89=tk.Button(root,text="=",command=lambda:calculate(),width=5,font=("Times new roman",20))
b89.grid(row=6,column=4)
b10=tk.Button(root,text="C",command=lambda:C(),width=5,font=("Times new roman",20))
b10.grid(row=7,column=1)
root.mainloop()