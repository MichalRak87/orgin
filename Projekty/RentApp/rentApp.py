
from genericpath import exists
from tkinter import *
import datetime
import os



try:
    with open('rent_history.txt','r')as file:
        pass
except:
    with open('rent_history.txt','w')as file:
        file.write(str(datetime.date.today()))


root = Tk()
root.geometry('800x800')
root.title("Rent counter")
root.bind('<Escape>', lambda e: root.destroy())

class Rent:
    def __init__(self):
        self.today = datetime.date.today()
        self.date = ''
        self.get_data()
        self.rent= self.rent_amount()
        self.info = ''
        self.my_date=''
        self.hist()


    def rent_amount(self):
        self.days = self.date - self.today
        rent= int(self.days.days)
        rent_am = int((abs(rent)) / 7)*100
        return rent_am

    def add_data(self):
        with open('rent_history.txt','a+') as file:
            file.seek(0,0)
            if str(self.today) in file.read():
                return f'Date already exist {str(self.today)}'
            else: 
                file.write('\n'+str(self.today))
                return f'Add to history {str(self.today)}'
               

    def get_data(self):
        with open('rent_history.txt','r') as file:
            str_data = file.readlines()[-1]
            self.date = datetime.datetime.strptime(str_data, '%Y-%m-%d').date()

    def click_button1(self):
        label_info.config(text=c.add_data())
        self.get_data()
        self.rent=c.rent_amount()
        label3.config(text=f'Last paid was: {c.date}')
        label4.config(text=f'Rent amount: {self.rent}')
        label_hist2.config(text=c.hist())

    def back(self):
        with open('rent_history.txt','r') as file:
            rent= file.read()
            if len(rent) > 10:
                with open('rent_history.txt','w') as file:
                        rent =rent.replace(rent[-11::],'')
                        file.write(rent)
                        
                self.get_data()
                self.rent=c.rent_amount()
                label3.config(text=f'Last paid was: {c.date}')
                label4.config(text=f'Rent amount: {self.rent}') 
                label_info.config(text='Last payment removed')
                label_hist2.config(text=c.hist())
    def date_check(self):
        try:
            h=datetime.datetime.fromisoformat(date_edit.get()).date()-self.today
            if date_edit.get()[4] == '-' and date_edit.get()[7] == '-':
                if len(date_edit.get()) == 10:
                    if int(h.days)<=0:
                        return True
                    else:
                        label_info.config(text='Date is too hight')
                        return False
        except:
            label_info.config(text='Invalid date format')
            return False
    def edit_date(self):
        if self.date_check():
            with open('rent_history.txt','r') as file:
                rent= file.read()
                if len(rent) > 10:
                    with open('rent_history.txt','w') as file:
                        rent =rent.replace(rent[-11::],'\n'+date_edit.get())
                        file.write(rent)
                elif len(rent) == 10:
                    with open('rent_history.txt','w') as file:
                        rent =rent.replace(rent[-11::],date_edit.get())
                        file.write(rent)
                self.get_data()
                self.rent=c.rent_amount()
                label3.config(text=f'Last paid was: {c.date}')
                label4.config(text=f'Rent amount: {self.rent}') 
                label_info.config(text='Last date changed')
                label_hist2.config(text=c.hist())       
                
    def hist(self):
        with open('rent_history.txt','r') as file:
            h=file.read()
            return h
    def add_new_date(self):
        if self.date_check():
            with open('rent_history.txt','r+') as file:
                f = file.read()
                if str(datetime.datetime.fromisoformat(date_edit.get()).date()) in f:
                    label_info.config(text='Date already exist')
                else:
                    file.write('\n'+str(datetime.datetime.fromisoformat(date_edit.get()).date()))
                    label_info.config(text='New date added')
            self.get_data()
            self.rent=c.rent_amount()
            label3.config(text=f'Last paid was: {c.date}')
            label4.config(text=f'Rent amount: {self.rent}') 
            label_hist2.config(text=c.hist()) 
    def full_hist(self):
        
        nw = Toplevel(root)
        nw.title('Full History')
        nw.geometry('300x700')
        Label(nw,text=c.hist(),font=16).pack()
        # if nw.winfo_exists() == 1:
        #     print(nw.winfo_exists())
        #     message.config=DISABLED
        
 
            
        
        
c = Rent()


#App Widgets:
#=====================================
label1 = Label(root,text='Rent counter',font=('Comic Sans MS',42),border=20)
#=====================================
label2= Label(root,text=f'Today is: {c.today}',fg='Blue',font=('Comic Sans MS',22))
#=====================================
label3= Label(root,text=f'Last paid was: {c.date}',fg='Red',font=('Comic Sans MS',22))
#=====================================
label4= Label(root,text=f'Rent amount: {c.rent_amount()}',font=('Comic Sans MS',22))
#=====================================
button1 = Button(root,text='Pay rent',
padx=50,pady=20,command=c.click_button1,
border=5,
fg='blue',bg='grey',font=('Comic Sans MS',16))
#=====================================
button2 = Button(root,text='Delete last date',
padx=50,pady=20,command=c.back,
border=5,
fg='blue',bg='grey',font=('Comic Sans MS',16))
#=====================================
label_info =Label(root,wrap=150,text=c.info,font=('Comic Sans MS',16))
#=====================================
button3 = Button(root,text='Edit last date',
padx=50,pady=20,command=c.edit_date,
border=5,
fg='blue',bg='grey',font=('Comic Sans MS',16))
#=====================================
add_date = Button(root,text='Add new date',
padx=50,pady=20,command=c.add_new_date,
border=5,
fg='blue',bg='grey',font=('Comic Sans MS',16))
#=====================================
message = Button(root,text='Full history',
padx=50,pady=20,
border=5,
command=c.full_hist,
fg='blue',bg='grey',font=('Comic Sans MS',12))
#=====================================
date_edit = Entry(font=22,background='Light blue',
border=7,cursor='dot',width=10,
)
date_edit.insert(0,c.today)
#=====================================
label_hist1= Label(root,text='History:',font=('Comic Sans MS',22))
label_hist2= Label(root,text=c.hist(),font=('Comic Sans MS',22),anchor=S,width=10,height=2,relief=RIDGE)
#=====================================
label1.grid(row=0,columnspan=2)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
button1.grid(row=4,column=0)
label_info.grid(row=4,column=1)
button2.grid(row=5,column=0,pady=20)
button3.grid(rows=5,column=1,rowspan=4,columnspan=4)
date_edit.grid(row=5,column=1)
label_hist1.grid(row=1,column=1)
label_hist2.grid(row=1,column=1,rowspan=1,columnspan=1)
add_date.grid(rowspan=1,column=1)
message.grid(row=3,column=1)

root.mainloop()




