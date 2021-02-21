from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ExampleApp>:
    orientation: "vertical"
    ColoredButton:
        text: ""
        on_press: gif.anim_delay = 0.01
        on_press: gif._coreimage.anim_reset(True)

        Image:
            id: gif
            source: 'beaming_face_with_smiling_eyes.gif'
            center: self.parent.center
            size: 50, 50
            allow_stretch: True
            anim_delay: -1
            anim_loop: 1
""")

class ExampleApp(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    ExampleApp().run() 
