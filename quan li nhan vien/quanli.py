from tkinter import *
import tkinter.font as tkf
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import mysql.connector as mq
from tkinter import messagebox
#connect database
db=mq.connect(host='localhost',user='demo',password='123',database='nhanvien')
#####################
root=Tk()
root.geometry('900x900')
root.title("Quan li nhan vien")
root.iconbitmap("bg.ico")
root.configure(background="#FAEBD7")

fontstyle=tkf.Font(family="Times New Roman",size=20)
fontframe=tkf.Font(family="Times New Roman",size=12)

a=Image.open('nv.jpg')
a=a.resize((90,90))
a=ImageTk.PhotoImage(a)
tieude=Label(root,text="Phần mềm quản lí nhân viên",compound=RIGHT,image=a,font=fontstyle,bg="#FAEBD7")
tieude.pack()

frame1=LabelFrame(root,text="Thêm nhân viên",font=fontframe,takefocus=True)
frame1.pack()
frame2=LabelFrame(root,text="Cập nhật nhân viên",font=fontframe,takefocus=True)
frame2.pack()
frame3=LabelFrame(root,text="Xóa nhân viên",font=fontframe,takefocus=True)
frame3.pack()
frame4=LabelFrame(root,text="Tìm kiếm nhân viên",font=fontframe,takefocus=True)
frame4.pack()
frame5=LabelFrame(root,text="Danh sách nhân viên",font=fontframe,takefocus=True)
frame5.pack()
#bien
vargt = StringVar()
varngay=IntVar()
varthang=IntVar()
#ham xu li
def add():
    ngaysinh=str(namentry.get())+"-"+str(varthang.get())+"-"+str(varngay.get())
    sql="insert into tnhanvien values (%s,%s,%s,%s,%s)"
    val=(msentry.get(),htentry.get(),ngaysinh,phongbanentry.get(),vargt.get())
    run=db.cursor()
    run.execute(sql,val)
    db.commit()
    messagebox.showinfo("Thêm nhân viên","Thành Công")
def update():
    sql="update tnhanvien set phongban= '{0}' where ms= '{1}'".format(uppbentry.get(),upmsentry.get())
    run=db.cursor()
    run.execute(sql)
    db.commit()
    messagebox.showinfo("Cập nhật nhân viên","Thành Công")
def delete():
    sql="delete from tnhanvien where ms='{0}'".format(delmsentry.get())
    run=db.cursor()
    run.execute(sql)
    db.commit()
    messagebox.showinfo("Xóa nhân viên","Thành Công")
def search():
    xoahet()
    sql="select * from tnhanvien where ms ='{0}'".format(tkmsentry.get())
    dem="select count(*) from tnhanvien where ms ='{0}'".format(tkmsentry.get())
    rdem=db.cursor()
    rdem.execute(dem)
    kq=rdem.fetchall()
    if(kq[0][0]!=0):
        run=db.cursor()
        run.execute(sql)
        row=run.fetchall()
        k=row[0][0].ljust(60)+row[0][1].ljust(47)+str(row[0][2]).ljust(60)+row[0][3].ljust(50)+row[0][4]
        lb.insert(END,k)
    else:
        messagebox.showwarning("Thông báo","Không tìm thấy nhân viên")
def show():
    xoahet()
    sql="select * from tnhanvien"
    run=db.cursor()
    run.execute(sql)
    row=run.fetchall()
    for i in row:
        s=i[0].ljust(60)+i[1].ljust(47)+str(i[2]).ljust(60)+i[3].ljust(50)+i[4]
        lb.insert(END,s)

def xoahet():
    lb.delete(0,END)
#frame1
mslabel=Label(frame1,text="Nhập mã số nhân viên:  ",font=fontframe)
mslabel.grid(row=0,column=0)
msentry=Entry(frame1,bd=2,width=30)
msentry.grid(row=0,column=2)
htlabel=Label(frame1,text="Nhập họ và tên:             ",font=fontframe)
htlabel.grid(row=1,column=0)
htentry=Entry(frame1,bd=2,width=30)
htentry.grid(row=1,column=2)
giotinhlabel=Label(frame1,text="Giới Tính:                      ",font=fontframe)
giotinhlabel.grid(row=2,column=0)
namradio=Radiobutton(frame1,text="Nam",variable=vargt,value="Nam",font=fontframe)
namradio.deselect()
namradio.grid(row=2,column=1)
nuradio=Radiobutton(frame1,text="Nữ",variable=vargt,value="Nữ",font=fontframe)
nuradio.grid(row=2,column=2)
ngaylabel=Label(frame1,text="   Ngày:                              ",font=fontframe)
ngaylabel.grid(row=3,column=0)
ngayCombobox=ttk.Combobox(frame1,width=2,textvariable=varngay,values=tuple(range(1,32)))
ngayCombobox.grid(row=3,column=1)
thanglabel=Label(frame1,text=" Tháng: ",font=fontframe)
thanglabel.grid(row=3,column=2)
thangCombobox=ttk.Combobox(frame1,width=2,textvariable=varthang,values=tuple(range(1,13)))
thangCombobox.grid(row=3,column=3)
namlabel=Label(frame1,text="       Năm: ",font=fontframe)
namlabel.grid(row=3,column=4)
namentry=Entry(frame1,bd=2,width=10)
namentry.grid(row=3,column=5)
phongbanlabel=Label(frame1,text="Phòng làm việc:             ",font=fontframe)
phongbanlabel.grid(row=4,column=0)
phongbanentry=Entry(frame1,bd=2,width=30)
phongbanentry.grid(row=4,column=2)
b=Button(frame1,text="Thêm nhân viên",command=add,font=fontframe,width=15)
b.grid(row=7,column=2)
#frame 2
updatems=Label(frame2,text="Nhập mã số nhân viên: ",font=fontframe)
updatems.grid(row=0,column=0)
upmsentry=Entry(frame2,bd=2,width=73)
upmsentry.grid(row=0,column=3)
updatepb=Label(frame2,text="Nhập phòng làm việc:  ",font=fontframe)
updatepb.grid(row=1,column=0)
uppbentry=Entry(frame2,bd=2,width=73)
uppbentry.grid(row=1,column=3)
capnhat=Button(frame2,text="Cập nhật",font=fontframe,width=25,command=update)
capnhat.grid(row=2,column=3)
#frame3
delms=Label(frame3,text="Nhập mã số nhân viên: ",font=fontframe)
delms.grid(row=0,column=0)
delmsentry=Entry(frame3,bd=2,width=60)
delmsentry.grid(row=0,column=1)
delxoa=Button(frame3,text="Xóa nhân viên",font=fontframe,width=48,command=delete)
delxoa.grid(row=1,column=1)
#frame4
tkmslabel=Label(frame4,text="Nhập mã số nhân viên",font=fontframe)
tkmslabel.grid(row=0,column=0)
tkmsentry=Entry(frame4,bd=2,width=63)
tkmsentry.grid(row=0,column=1)
tkms=Button(frame4,text="Tìm kiếm nhân viên",font=fontframe,command=search)
tkms.grid(row=1,column=0)
showall=Button(frame4,text="Tất cả nhân viên",font=fontframe,command=show)
showall.grid(row=1,column=1)
xuatfile=Button(frame4,text="Xóa hết",font=fontframe,command=xoahet)
xuatfile.grid(row=1,column=2)
#frame5
scrollbar=Scrollbar(frame5)
scrollbar.grid(row=1,column=1)
lb=Listbox(frame5,width=161,height=20,yscrollcommand=scrollbar.set)
lb.grid(row=1,column=0)
scrollbar.configure(command=lb.yview)
tieude1=Text(frame5,height=1,width=120,font=fontframe)
tieude1.insert(INSERT,"Mã số nhân viên\t\t\tHọ Tên\t\t\tNgày Sinh\t\t\tPhòng Ban\t\t\tGiới Tính")
tieude1.grid(row=0,column=0)
messagebox.showinfo("Thông Tin","Tác giả:Trương Hữu Phúc\nFB:fb.com/DdosFulzac")
root.mainloop()

