import kivy

# import pygame
# pygame.init()
# print(pygame.display.Info())

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from tryvars import b, h, Window_back_color

Builder.load_file("maingame.kv")
Builder.load_file("saari_goti.kv")
Builder.load_file("trybutton.kv")



class Cancan(FloatLayout):
    pass


class tryApp(App):
    def build(self):
        return Cancan()

if __name__ == "__main__":
    Window.size = (b, h)
    Window.clearcolor = get_color_from_hex(Window_back_color)
    tryApp().run()