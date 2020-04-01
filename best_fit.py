from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Chương Trình Mô Tả Thuật Toán Best Fit")
a=[]
c=[] 
def show():
   messagebox.showinfo("Thông Tin Nhóm ","""1.Trương Hữu Phúc
2.Nguyễn Hoàng Duy
3.Phan Duy Khang
""") 
def them1():
    ten="Size: "+e1.get()
    l1.insert(END,ten)
    a.append(int(e1.get()))
def them2():
    ten2="Size: "+e2.get()
    l2.insert(END,ten2)
    c.append(int(e2.get()))
def xuli():
    all=[-1]*len(a)
    for i in range(len(a)):
        vt=-1
        for j in range(len(c)):
            if c[j]>=a[i]:
                if vt==-1:
                    vt=j
                elif c[vt]>c[j]:
                    vt=j
        if vt!=-1:
            all[i]=vt
            c[vt]-=a[i]
           
    l3.insert(END,"---------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(a)):
        if (all[i]!=-1):
            var ="Bộ nhớ: "+str(all[i]+1)+" cung cấp"+" cho process size: "+str(a[i])
            l3.insert(END,var)
        else:
            var ="Không đủ bộ nhớ cung cấp"+" cho process size: "+str(a[i])
            l3.insert(END,var)
    l3.insert(END,"---------------------------------------------------------------------------------------------------------------------------------------")
            


label1=Label(root,text="Input Process Size",font=("cambria",10),bd=2)
label1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=1,column=0)
b1=Button(root,text="Add",width=17,command=them1)
b1.grid(row=2,column=0)
l1=Listbox(root,height=20,bd=2,bg="black",fg="green")
l1.grid(row=3,column=0)

label2=Label(root,text="Input Block Size",font=("cambria",10),bd=2)
label2.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
b2=Button(root,text="Add",width=17,command=them2)
b2.grid(row=2,column=1)
l2=Listbox(root,height=20,bd=2,bg="black",fg="green")
l2.grid(row=3,column=1)

b=Button(root,text="About",width=60,command=show,font=("cambria",10))
b.grid(row=0,column=2)
b4=Button(root,text="Exit",width=60,command=root.quit,font=("cambria",10))
b4.grid(row=1,column=2)
b3=Button(root,text="Xử Lí",width=60,command=xuli,font=("cambria",10))
b3.grid(row=2,column=2)
l3=Listbox(root,width=60,height=20,bd=2,bg="black",fg="green")
l3.grid(row=3,column=2)


root.mainloop()
