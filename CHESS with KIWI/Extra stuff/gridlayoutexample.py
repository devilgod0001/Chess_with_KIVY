import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

#Different classes should be used for different Screens

class MainMenuScreen(GridLayout):
    def __init__(self, **kwargs): #NO NEED
        super(MainMenuScreen, self).__init__(**kwargs) #NO NEED
        pass




class ChessApp(App):

    def build(self):

        return MainMenuScreen()



if __name__ == "__main__":
    ChessApp().run()