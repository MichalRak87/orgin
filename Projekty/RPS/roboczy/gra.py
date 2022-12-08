import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import SwapTransition
import os,sys
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from random import choice
import time
from kivy.core.window import Window

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


kv = Builder.load_file(resource_path('gra.kv'))

class MenuScreen(Screen):
    #Function animate Play button
    def animate_it(self,widget,*args):  
        animate1=Animation(duration=0.1,disabled=False)
        animate1+=Animation(duration=.5,opacity=1)
        #Function checking input is != ''
        if self.name_box_dis() != '' and self.name_box_dis() != ' ' :
            animate1.start(widget=self.ids.play_button)
    #Function starting animate Play button
    def animate_it2(self,widget,*args):
        self.ids.name_input.text
        animate2 = Animation(duration=.5,opacity=0)
        animate2 += Animation(duration=0.1,disabled=True)
        animate2.start(widget=self.ids.play_button)
    #Function checking input is != '' or ' '
    def on_press_submit(self,name):
            name=self.ids.name_input.text
            if self.name_box_dis() != '' and self.name_box_dis() != ' ':
                self.ids.submit_button.text = f'Hello {name.title()}'
    #Function checking input is != '' or ' '
    def name_box_dis(self):
        return self.ids.name_input.text


class GameScreen(Screen):
    player_scores=0
    computer_scores=0
    player_wins = 0
    computer_wins = 0
    def plr_scores(self):
        self.player_scores+=1
        return self.player_scores

    def com_scores(self):
        self.computer_scores+=1
        return self.computer_scores
    #Player move animations:
    #Kamien Animation
    def animate_kamien(self,widget,*args):
        kamien = Animation(duration=.3,pos_hint={'x':.5,'y':.4},)
        kamien.start(widget)
        kamien = Animation(duration=.3,pos_hint={'x':.6,'y':.01})
        kamien.start(widget=self.ids.nozyce)
        kamien = Animation(duration=.3,pos_hint={'x':.8,'y':.01})
        kamien.start(widget=self.ids.papier)
        

    #Nozyce Animation
    def animate_nozyce(self,widget,*args):
        nozyce = Animation(duration=.3,pos_hint={'x':.5,'y':.4},)
        nozyce.start(widget)
        nozyce = Animation(duration=.3,pos_hint={'x':.4,'y':.01})
        nozyce.start(widget=self.ids.kamien)
        nozyce = Animation(duration=.3,pos_hint={'x':.8,'y':.01})
        nozyce.start(widget=self.ids.papier) 

    #Papier Animation
    def animate_papier(self,widget,*args):
        papier = Animation(duration=.3,pos_hint={'x':.5,'y':.4},)
        papier.start(widget)
        papier = Animation(duration=.3,pos_hint={'x':.4,'y':.01})
        papier.start(widget=self.ids.kamien)
        papier = Animation(duration=.3,pos_hint={'x':.6,'y':.01})
        papier.start(widget=self.ids.nozyce)

    #Menu Button Animation
    def menu_button(self,widget,*args):
        menu= Animation(duration=.1,pos_hint={'x':.4,'y':.01})
        menu.start(widget=self.ids.kamien)
        menu= Animation(duration=.1,pos_hint={'x':.8,'y':.01})
        menu.start(widget=self.ids.papier)
        menu= Animation(duration=.1,pos_hint={'x':.6,'y':.01})
        menu.start(widget=self.ids.nozyce)
        menu= Animation(duration=.1,pos_hint={'x':.4,'y':.79})
        menu.start(widget=self.ids.com_label3)
        menu= Animation(duration=.1,pos_hint={'x':.6,'y':.79})
        menu.start(widget=self.ids.com_label2)
        menu= Animation(duration=.1,pos_hint={'x':.8,'y':.79})
        menu.start(widget=self.ids.com_label1)
        self.player_scores=0
        self.player_wins=0
        self.computer_scores=0
        self.computer_wins=0
        self.ids.plr_scores.text = 'Player: ' + str(self.player_scores)
        self.ids.com_scores.text = 'Computer: ' + str(self.computer_scores)
        self.ids.plr_win.text = 'Player wins: ' + str(self.player_wins)
        self.ids.com_win.text = 'Computer wins: ' + str(self.computer_wins)       
        self.ids.winner_label.text = 'Good Luck!!!'
        self.ids.winner_label.color = '3CCF4E'

    def result(self,plr):
        #Game logic
        global lab
        lab=choice(['kamien','papier','nozyce'])
        print(f'lab = {lab} plr= {plr}')
        if plr == lab:
            self.ids.winner_label.text = 'Its a Tie'
            self.ids.winner_label.color = (1,1,0)
            print('Tie')
        elif plr == 'papier' and lab == "kamien":
            self.ids.winner_label.color = (0,1,0)
            self.ids.winner_label.text = 'You Won!!!'
            print('Player wins')
            self.plr_scores()
        elif plr == 'kamien' and lab == "nozyce":
            self.ids.winner_label.color = (0,1,0)
            self.ids.winner_label.text = 'You Won!!!'
            print('Player wins')
            self.plr_scores()
        elif plr == 'nozyce' and lab == "papier":
            self.ids.winner_label.color = (0,1,0)
            self.ids.winner_label.text = 'You Won!!!'
            print('Player wins')
            self.plr_scores()
        else:
            self.ids.winner_label.color = (1,0,0)
            self.ids.winner_label.text = 'You Lost!!!'
            print('Computer wins')
            self.com_scores()
        self.ids.plr_scores.text = 'Player: ' + str(self.player_scores)
        self.ids.com_scores.text = 'Computer: ' + str(self.computer_scores)

        if self.player_scores ==3:  
            self.player_wins +=1
        elif self.computer_scores == 3:
            self.computer_wins+=1
        
        self.ids.plr_win.text = 'Player wins: ' + str(self.player_wins)
        self.ids.com_win.text = 'Computer wins: ' + str(self.computer_wins)

        if self.player_scores ==3 or self.computer_scores ==3:
            self.player_scores=0
            self.computer_scores=0
            self.ids.plr_scores.text = 'Player: ' + str(self.player_scores)
            self.ids.com_scores.text = 'Computer: ' + str(self.computer_scores)
        
            
            
        

    def comp_move(self,widget,*args):
        #Computer move animation
        if lab == 'papier':
            comp= Animation(duration=.3,pos_hint={'x':.8,'y':.79}) 
            comp.start(widget=self.ids.com_label1)
            comp= Animation(duration=.3,pos_hint={'x':.7,'y':.4})
            comp.start(widget=self.ids.com_label2)
            comp1 = Animation(duration=.3,pos_hint={'x':.4,'y':.79})
            comp1.start(widget=self.ids.com_label3)
        elif lab == 'nozyce':
            comp= Animation(duration=.3,pos_hint={'x':.7,'y':.4}) 
            comp.start(widget=self.ids.com_label1)
            comp= Animation(duration=.3,pos_hint={'x':.6,'y':.79})
            comp.start(widget=self.ids.com_label2)
            comp1 = Animation(duration=.3,pos_hint={'x':.4,'y':.79})
            comp1.start(widget=self.ids.com_label3)
        elif lab =='kamien':
            comp= Animation(duration=.3,pos_hint={'x':.8,'y':.79}) 
            comp.start(widget=self.ids.com_label1)
            comp= Animation(duration=.3,pos_hint={'x':.6,'y':.79})
            comp.start(widget=self.ids.com_label2)
            comp1 = Animation(duration=.3,pos_hint={'x':.7,'y':.4})
            comp1.start(widget=self.ids.com_label3)
        



    
sm = ScreenManager(transition=SwapTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='game'))

class GraApp(App):
    def build(self):
        self.title = 'Rock,Paper,Scissors Game'       
        return sm

        





if __name__ == '__main__':
    GraApp().run()