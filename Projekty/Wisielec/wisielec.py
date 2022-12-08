import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import turtle
from random import randint

answer=0
random_num=0
max_l = 100
# Creating Main menu window
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.config(background='light yellow')
        self.geometry('250x200')
        self.title('Wisielec')
        self.eval('tk::PlaceWindow . Center')
        self.main_label = ttk.Label(text='Witaj w grze wisielec', font=60,background='light yellow')
        self.main_label.pack(pady=10,side='top')
        self.r_label = tkinter.Label(wraplength=200,text='Zmien max liczbe do zgadywanie (domyslnie jest 100)', background='light yellow')
        self.r_label.pack()
        self.button_new_game = ttk.Button(text='Nowa gra', width=20, padding=10, command=lambda: self.new_game_button())
        self.ent = tkinter.Entry(self,width=5)
        self.ent.pack()
        self.bind_enter_m()
        self.button_exit = ttk.Button(text='Wyjscie', width=20, padding=10, command=lambda: self.exit_button())
        self.button_new_game.pack(pady=5)
        self.button_exit.pack(pady=5)

    def bind_enter_m(self):
        self.bind('<Return>', self.onclick_m)
        self.grid()

    def onclick_m(self,event):
        global max_l
        max_l = self.ent.get()
        print(max_l)
        try:
            if max_l.isdigit():
                pass
            else:
                raise Exception
        except Exception:
            self.r_label.config(text='Zmien max liczbe do zgadywanie (domyslnie jest 100)')
            max_l = 100
        else:
            self.r_label.config(text=f'Wybrales liczbe {max_l}')

    # Creating new game button:
    def new_game_button(self):
        self.nw = Message(self)
        self.nw.grab_set()
        global random_num
        random_num = randint(1, int(max_l))
        print(random_num)


    # Creating exit button:
    @staticmethod
    def exit_button():
        main_menu.quit()

# Creating game window:
class Message(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.resizable(False,False)
        self.title('Gra Wisielec')
        self.geometry("300x70+650+600")
        self.config(background='light yellow')
        self.lab = tkinter.Label(self, text='Podaj liczbe',background='light yellow')
        self.lab.pack()  # you can place it wherever you want
        self.e = tkinter.Entry(self,width=10) # customize all you want
        self.e.pack()
        self.bind_enter()
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.BOTTOM,pady=40)
        self.canvas.config(width=400, height=300)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("light grey")
        self.geometry('500x500+550+200')
        self.title('Gra Wisielec')
        self.label = tk.Label(self, text=f'Podaj liczbe od 1 do {max_l}', font=50, border=30,background='light yellow')
        self.label.pack(side=tk.TOP, )
        self.paint = turtle.RawTurtle(self.screen)
        self.paint.hideturtle()
        self.answers = []
        self.step = 1
        self.btn_ext = tkinter.Button(self, text='Wyjscie', font=12)
        self.btn_ext.pack()


    def bind_enter(self):
        self.bind('<Return>',self.onclick)
        self.grid()

    def onclick(self,event):
        global answer
        answer = self.e.get()
        try:
            if answer.isdigit():
                pass
            else:
                raise Exception
        except Exception:
            print('Lipa')
        else:
            answer = int(answer)
            if answer == random_num and self.step < 7:
                tkinter.messagebox.showinfo('Wygrales', f'Gratulacje udalo ci sie za {self.step} razem')
                self.label.config(text=f'Wygrales za {self.step} razem. Brawo!!!')
            else:
                if answer != '' and answer <= int(max_l) and answer > 0 and answer not in self.answers:
                    self.painting()
                    self.step +=1
                    self.answers.append(answer)
                    if random_num > answer:
                        self.label.config(text=f'Liczba jest wieksza od {answer}\nPodales juz liczby: {self.answers}')
                    else:
                        self.label.config(text=f'Liczba jest mniejsza od {answer}\nPodales juz liczby: {self.answers}')

    def painting(self):
        # Step 1
        if self.step == 1:
            self.paint.speed(0)
            self.paint.penup()
            self.paint.setposition(0, -100)
            self.paint.pendown()
            self.paint.begin_fill()
            for i in range(3):
                self.paint.forward(50)
                self.paint.left(120)
            self.paint.end_fill()

            # Step 2
        elif self.step == 2:
            self.paint.forward(50)
            self.paint.left(120)
            self.paint.forward(50)
            self.paint.right(30)
            self.paint.pendown()
            self.paint.pensize(4)
            self.paint.forward(100)
            self.paint.left(90)

            # Step 3
        elif self.step == 3:
            pass
            self.paint.fd(50.0)
            self.paint.left(90)
            self.paint.fd(20)

            # Step 4
        elif self.step == 4:
            self.paint.penup()
            self.paint.setx(-35.0)
            self.paint.begin_fill()
            self.paint.color('brown')
            self.paint.circle(10)
            self.paint.end_fill()
            self.paint.setposition(-25.0,30)
            self.paint.pendown()

            # Step 5
        elif self.step == 5:
            self.paint.forward(50)
            self.paint.penup()
            self.paint.setposition(-25.0, 10)
            self.paint.left(30)
            self.paint.pendown()
            self.paint.forward(30)
            self.paint.penup()
            self.paint.setposition(-25.0, 10)
            self.paint.right(60)
            self.paint.pendown()
            self.paint.forward(30)

            # Step 6
        elif self.step == 6:
            self.paint.penup()
            self.paint.setposition(-25.0, 10)
            self.paint.left(30)
            self.paint.forward(30)
            self.paint.left(30)
            self.paint.pendown()
            self.paint.forward(30)
            self.paint.penup()
            self.paint.setposition(-25.0, -20.0)
            self.paint.pendown()
            self.paint.right(60)
            self.paint.forward(30)
            tkinter.messagebox.showinfo('Przegrales', f'Powodzenia nastepnym razem! Chodzilo o liczbe {random_num}')


        if self.step == 7:
            Message.destroy(self)





if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.mainloop()
