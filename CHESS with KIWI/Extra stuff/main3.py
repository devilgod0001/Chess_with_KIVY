
'''
COORDINATE SYSTEM (0,0) --> BOTTOM LEFT!!!  [Like real cartesian plane!!!]
'''

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from datetime import datetime
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

now = datetime.now()




#print(now.strftime('[b]%H[/b]:%M:%S'))

class MainMenuScreen(FloatLayout):
    def changenameonpress(self):
        self.ids.btn2.background_color= .2,.3,.2,1

    def changenameonrelease(self):
        self.ids.btn2.background_color = 0.0625,0.0625,0.59765625,1


class Chess2App(App):
    def on_start(self):
        Clock.schedule_interval(self.update_timetime,0.1)
    def update_timetime(self,nap):
        self.root.ids.timetime.text = now.strftime('[b]%H[/b]:%M:%S')

    def build(self):

        return MainMenuScreen()

if __name__ == "__main__":
    Window.size = (9*40,16*40) #Since the ratio of most phone screens is 9:16 [width,height]
    Window.clearcolor = get_color_from_hex("#101010")
    Chess2App().run()