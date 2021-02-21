import kivy
kivy.require("1.1.1")
from kivy.app import App
from kivy.uix.label import Label

adding = "\n[size=25]You may know this![/size]\n(a+b)[sup]2[/sup]=a[sup]2[/sup]+b[sup]2[/sup]+2ab"
humming = "\nCO[sub]2[/sub]->C+O[sub]2[/sub]\n[font=Roboto-Light]Greetings![/font]\n...........if you know these!"
class TestApp(App):
    def build(self):
        mylabels = Label(text="[color=#332233]Hello [b]Gourav[/b][/color]\n[i]What [s]is[/s] [u]are[/u] your Plan[b]s?[/b][/i]"+adding+humming,
         font_size='40',markup=True)
        return mylabels

TestApp().run()
