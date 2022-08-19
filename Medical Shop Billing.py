from distutils.cmd import Command
from tkinter import *
from tkcalendar import DateEntry
medic=Tk()
medic.geometry('600x800')
#medic.config(bg='#dbd3c5')
medic.title('BILL')





def total():
    total_amount=int(e16.get())+int(e17.get())+int(e18.get())+int(e19.get())+int(e20.get())
    k.set(total_amount)









def reset():
    a1.delete(0,END)
    a2.delete(0,END)
    a3.delete(0,END)
    a4.delete(0,END)
    a5.delete(0,END)
    a6.delete(0,END)
    a7.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    e14.delete(0,END)
    e15.delete(0,END)
    e16.delete(0,END)
    e17.delete(0,END)
    e18.delete(0,END)
    e19.delete(0,END)
    e20.delete(0,END)
    e21.delete(0,END)
    












def submit():
    
        name=a.get()
        b.set(name)
        bill=a1.get()
        b1.set(bill)
        date=date1.get()
        b2.set(date)
        medicine1=list1.get()
        z1.set(medicine1)
        medicine2=list2.get()
        z2.set(medicine2)
        medicine3=list3.get()
        z3.set(medicine3)
        medicine4=list4.get()
        z4.set(medicine4)
        medicine5=list5.get()
        z5.set(medicine5)
        qty1=e1.get()
        x1.set(qty1)
        qty2=e2.get()
        x2.set(qty2)
        qty3=e3.get()
        x3.set(qty3)
        qty4=e4.get()
        x4.set(qty4)
        qty5=e5.get()
        x5.set(qty5)


        if medicine1=='Acetaminophen':
            price1=60
        elif medicine1=='Adderall':
            price1=30
        elif medicine1=='No Medicine':
            price1=0
        elif medicine1=='Amitriptyline':
            price1=20
        elif medicine1=='Amlodipine':
            price1=40
        elif medicine1=='Ativan':
            price1=70
        elif medicine1=='Atorvastatin':
            price1=13
        elif medicine1=='Azithromycin':
            price1=90
        elif medicine1=='Benzonatate':
            price1=100
        elif medicine1=='Brilinta':
            price1=18
        


        if medicine2=='Acetaminophen':
            price2=60
        elif medicine2=='Adderall':
            price2=30
        elif medicine2=='Amitriptyline':
            price2=20
        elif medicine2=='Amlodipine':
            price2=40
        elif medicine2=='No Medicine':
            price2=0
        elif medicine2=='Ativan':
            price2=70
        elif medicine2=='Atorvastatin':
            price2=13
        elif medicine2=='Azithromycin':
            price2=90
        elif medicine2=='Benzonatate':
            price2=100
        elif medicine2=='Brilinta':
            price2=18


        
        if medicine3=='Acetaminophen':
            price3=60
        elif medicine3=='Adderall':
            price3=30
        elif medicine3=='Amitriptyline':
            price3=20
        elif medicine3=='No Medicine':
            price3=0
        elif medicine3=='Amlodipine':
            price3=40
        elif medicine3=='Ativan':
            price3=70
        elif medicine3=='Atorvastatin':
            price3=13
        elif medicine3=='Azithromycin':
            price3=90
        elif medicine3=='Benzonatate':
            price3=100
        elif medicine3=='Brilinta':
            price3=18





        
        if medicine4=='Acetaminophen':
            price4=60
        elif medicine4=='Adderall':
            price4=30
        elif medicine4=='Amitriptyline':
            price4=20
        elif medicine4=='Amlodipine':
            price4=40
        elif medicine4=='Ativan':
            price4=70
        elif medicine4=='No Medicine':
            price4=0
        elif medicine4=='Atorvastatin':
            price4=13
        elif medicine4=='Azithromycin':
            price4=90
        elif medicine4=='Benzonatate':
            price4=100
        elif medicine4=='Brilinta':
            price4=18


        
        if medicine5=='Acetaminophen':
            price5=60
        elif medicine5=='Adderall':
            price5=30
        elif medicine5=='Amitriptyline':
            price5=20
        elif medicine5=='No Medicine':
            price5=0
        elif medicine5=='Amlodipine':
            price5=40
        elif medicine5=='Ativan':
            price5=70
        elif medicine5=='Atorvastatin':
            price5=13
        elif medicine5=='Azithromycin':
            price5=90
        elif medicine5=='Benzonatate':
            price5=100
        elif medicine5=='Brilinta':
            price5=18


        amount1=int(price1)*int(e1.get())
        y1.set(amount1)
        amount2=int(price2)*int(e2.get())
        y2.set(amount2)
        amount3=int(price3)*int(e3.get())
        y3.set(amount3)
        amount4=int(price4)*int(e4.get())
        y4.set(amount4)
        amount5=int(price5)*int(e5.get())
        y5.set(amount5)


options=['No Medicine','Acetaminophen','Adderall','Amitriptyline','Amlodipine','Ativan','Atorvastatin','Azithromycin','Benzonatate','Brilinta']







list1=StringVar()
list2=StringVar()
list3=StringVar()
list4=StringVar()
list5=StringVar()
a=StringVar()
b=StringVar()
b1=StringVar()
a1=StringVar()
b2=StringVar()
z1=StringVar()
z2=StringVar()
z3=StringVar()
z4=StringVar()
z5=StringVar()
x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
y1=StringVar()
y2=StringVar()
y3=StringVar()
y4=StringVar()
y5=StringVar()
k=StringVar()


list1.set('No Medicine')
list2.set('No Medicine')
list3.set('No Medicine')
list4.set('No Medicine')
list5.set('No Medicine')

Label(medic,text='Date',font=8,fg='red').place(x=1600,y=50)
date1=DateEntry(medic)
date1.place(x=1650,y=53)
Label(medic,text='Bill No',font='8',fg='red').place(x=1600,y=80)
a1=Entry(medic,textvariable=a1)
a1.place(x=1650,y=83)
Label(medic,text='NICE MEDICALS', font='times 25 bold').place(x=800,y=50)
Label(medic,text='Iyyattil Junction,Chittur Road,Kochi',font='times 10 ').place(x=830,y=100)
Label(medic,text='Phone:8592809392|nicemedic@gmail.com',font='times 10 ').place(x=820,y=120)
Label(medic,text='Name of patient',font=10).place(x=100,y=200)
a2=Entry(medic,textvariable=a)
a2.place(x=230,y=204)
Label(medic,text='Phone',font=10).place(x=100,y=250)
a3=Entry(medic)
a3.place(x=230,y=254)
Label(medic,text='Name of Doctor',font=10).place(x=100,y=300)
a4=Entry(medic)
a4.place(x=230,y=304)
Label(medic,text='Medicine1',font=10).place(x=100,y=350)
OptionMenu(medic,list1,*options).place(x=230,y=350)
Label(medic,text='Medicine2',font=10).place(x=430,y=350)
OptionMenu(medic,list2,*options).place(x=560,y=350)
Label(medic,text='Medicine3',font=10).place(x=760,y=350)
OptionMenu(medic,list3,*options).place(x=890,y=350)
Label(medic,text='Medicine4',font=10).place(x=1090,y=350)
OptionMenu(medic,list4,*options).place(x=1220,y=350)
Label(medic,text='Medicine5',font=10).place(x=1420,y=350)
OptionMenu(medic,list5,*options).place(x=1550,y=350)
Label(medic,text='Quantity',font=10).place(x=100,y=400)
e1=Entry(medic,width=7)
e1.place(x=230,y=400)
e1.insert(0,0)
e2=Entry(medic,width=7)
e2.place(x=560,y=400)
e2.insert(0,0)
e3=Entry(medic,width=7)
e3.insert(0,0)
e3.place(x=890,y=400)
e4=Entry(medic,width=7)
e4.place(x=1220,y=400)
e4.insert(0,0)
e5=Entry(medic,width=7)
e5.place(x=1550,y=400)
e5.insert(0,0)
# Label(medic,text='Quantity',font=10).place(x=100,y=400)
# Entry(medic,width=5).place(x=230,y=404)
submit_btn=Button(medic,text='Submit',fg='white',command=submit,width=8,bg='black').place(x=1700,y=520)
reset_btn=Button(medic,text='Reset',fg='white',command=reset,width=8,bg='black').place(x=1770,y=520)


f=Frame(medic,bg='light green',width=2000,height=470).place(x=0,y=550)

Label(f,text='Name:',bg='lightgreen',font=10).place(x=180,y=650)
a5=Entry(f,textvariable=b,bg='lightgreen',bd=0)
a5.place(x=330,y=653)
Label(f,text='Date:',bg='lightgreen').place(x=1600,y=560)
a6=Entry(f,textvariable=b2,bg='lightgreen',bd=0)
a6.place(x=1650,y=560)
Label(f,text='Bill No:',bg='lightgreen').place(x=1600,y=600)
a7=Entry(f,textvariable=b1,bg='lightgreen',bd=0)
a7.place(x=1650,y=600)
Label(f,text='BILL',font='times 20 bold underline',bg='lightgreen').place(x=900,y=555)
Label(medic,text='Medicines:',font=10,bg='lightgreen').place(x=180,y=700)
e6=Entry(f,textvariable=z1,bg='lightgreen',bd=0)
e6.place(x=330,y=700)
e7=Entry(f,textvariable=z2,bg='lightgreen',bd=0)
e7.place(x=580,y=700)
e8=Entry(f,textvariable=z3,bg='lightgreen',bd=0)
e8.place(x=830,y=700)
e9=Entry(f,textvariable=z4,bg='lightgreen',bd=0)
e9.place(x=1080,y=700)
e10=Entry(f,textvariable=z5,bg='lightgreen',bd=0)
e10.place(x=1330,y=700)
Label(f,text='Quantity:',font=10,bg='lightgreen').place(x=180,y=750)
e11=Entry(f,width=7,textvariable=x1,bg='lightgreen',bd=0)
e11.place(x=330,y=750)
e12=Entry(f,width=7,textvariable=x2,bg='lightgreen',bd=0)
e12.place(x=580,y=750)
e13=Entry(f,width=7,textvariable=x3,bg='lightgreen',bd=0)
e13.place(x=830,y=750)
e14=Entry(f,width=7,textvariable=x4,bg='lightgreen',bd=0)
e14.place(x=1080,y=750)
e15=Entry(f,width=7,textvariable=x5,bg='lightgreen',bd=0)
e15.place(x=1330,y=750)
Label(f,text='Amount:',font=10,bg='lightgreen').place(x=180,y=800)
e16=Entry(f,width=7,textvariable=y1,bg='lightgreen',bd=0)
e16.place(x=330,y=800)
e17=Entry(f,width=7,textvariable=y2,bg='lightgreen',bd=0)
e17.place(x=580,y=800)
e18=Entry(f,width=7,textvariable=y3,bg='lightgreen',bd=0)
e18.place(x=830,y=800)
e19=Entry(f,width=7,textvariable=y4,bg='lightgreen',bd=0)
e19.place(x=1080,y=800)
e20=Entry(f,width=7,textvariable=y5,bg='lightgreen',bd=0)
e20.place(x=1330,y=800)
btn_total=Button(f,text='Total:',command=total).place(x=1500,y=850)
e21=Entry(f,bg='lightgreen',bd=0,textvariable=k,width=50)
e21.place(x=1570,y=853)



mainloop()