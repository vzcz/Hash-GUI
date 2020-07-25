from tkinter import *
from hashlib import*
#---------------------------
wnd=Tk()
wnd.title('Hash')
wnd.geometry('400x550')
wnd.resizable(0,0)
wnd.configure(bg='#026889')
#---------------------------
varent=StringVar()
varinfo=StringVar()
text=varinfo.get()
varinfo.set(text)

def ch1():
    varinfo.set(md5(varent.get().encode()).hexdigest())
def ch2():
    varinfo.set(sha1(varent.get().encode()).hexdigest())
def ch3():
    varinfo.set(sha224(varent.get().encode()).hexdigest())
def ch4():
    varinfo.set(sha256(varent.get().encode()).hexdigest())
def ch5():
    varinfo.set(sha384(varent.get().encode()).hexdigest())
def ch6():
    varinfo.set(sha512(varent.get().encode()).hexdigest())

         #Enter#
#---------------------------
en=Entry(wnd,textvariable=varent,justify='left')
en.place(x=95,y=195)
#---------------------------
Bu1=Button(wnd,text='md5',bg='#026889',command=ch1,width=6,bd=3,fg='white',font=('arial',11,'bold'))
Bu1.place(x=180,y=225)
Bu2=Button(wnd,text='sha1',bg='#026889',command=ch2,width=6,bd=3,fg='white',font=('arial',11,'bold'))
Bu2.place(x=100,y=225)
Bu3=Button(wnd,text='sha224',bg='#026889',command=ch3,width=6,bd=3,fg='white',font=('arial',11,'bold'))
Bu3.place(x=20,y=225)
Bu4=Button(wnd,text='sha256',bg='#026889',command=ch4,width=6,bd=3,fg='white',font=('arial',11,'bold'))
Bu4.place(x=260,y=225)
Bu5=Button(wnd,text='sha384',bg='#026889',command=ch5,width=6,bd=3,fg='white',font=('arial',11,'bold'))
Bu5.place(x=180,y=260)
Bu6=Button(wnd,text='sha512',bg='#026889',command=ch6,width=6,bd=3,fg='white',font=('arial',11,'bold'))
Bu6.place(x=100,y=260)



         #logo#
#---------------------------
logo=PhotoImage(file='hash.png')
logo=logo.subsample(4,4)
lp=Label(wnd,
         image=logo,
         bg='#026889')
lp.place(x=125,y=30)

#---------------------------


#---------------------------

                #label#
#----------------------------------------------#
lp=Label(wnd,
         textvariable=varinfo,
         bg='#026889',
         fg='black',
         wraplength=280,
         justify='left',
        )
lp.place(x=35,y=320)
#lp.grid(row=2,column=1,padx=30,pady=20,ipady=8,ipadx=20)


lp=Label(wnd,
         text='Name:',
         bg='#026889',
         fg='white')

lp.place(x=45,y=195)

#----------------------------------------------#

wnd.mainloop()

