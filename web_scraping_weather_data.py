
from bs4 import BeautifulSoup as bs
import requests as rq
from tkinter import *
def get():
    url='https://weather.com/vi-VN/weather/today/l/e4f3028ded4eaa85aa504baa51acd7b6df7932ebc68c9d7aff1c838d1178f42c'
    a=rq.get(url)
    soup=bs(a.text,"html.parser")
    vt=soup.find('h1',{'class':'h4 today_nowcard-location'})
    label1=Label(labelframe,text="Vị Trí: "+vt.text,font="Helvetica",width=41,bg='#4c4cff')
    label1.pack()
    temp1=soup.find('div',{'class':'today_nowcard-temp'})
    label2=Label(labelframe,text="Nhiệt độ hiện tại: "+temp1.text,font="Helvetica",width=41,bg='#00bfff')
    label2.pack()
    temp=soup.find('p',{'class':'today_nowcard-timestamp'})
    label3=Label(labelframe,text=temp.text,font="Helvetica",width=41,bg='#005b96')
    label3.pack()
    mt=soup.find('div',{'class':'today_nowcard-phrase'})
    label4=Label(labelframe,text=mt.text,font="Helvetica",width=41,bg='#6497b1')
    label4.pack()
    mt2=soup.find('div',{'class':'today_nowcard-feels'})
    label5=Label(labelframe,text=mt2.text,font="Helvetica",width=41,bg='#b3cde0')
    label5.pack()
    mt3=soup.find('div',{'class':'today_nowcard-hilo'})
    label6=Label(labelframe,text=mt3.text,font="Helvetica",width=41,bg='#63ace5')
    label6.pack()
root=Tk()
labelframe=LabelFrame(root,text="Dự Báo Thời Tiết Hôm Nay",bg='#4f95b9',font="Helvetica")
labelframe.pack(fill="both", expand="yes")
button=Button(labelframe,text='Cập Nhật',font="Helvetica",command=get,relief=RAISED,)
button.pack()
root.geometry('700x200')
root.iconbitmap('C:/Users/84908/Desktop/weather_icon3.ico')
root.title('web scraping weather data')
root.mainloop()


