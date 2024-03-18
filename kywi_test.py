
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint

Window.size = (300, 250)
Window.title = "Test"
Window.resizable = False


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Hello world', font_size=30)

    def btn_pressed(self, *args):
        self.label.color = (randint(0, 255)/255, randint(0,
                            255)/255, randint(0, 255)/255, 1)

    def build(self):

        box = BoxLayout()
        btn = Button(text="Click Me!")
        btn.bind(on_press=self.btn_pressed)
        box.add_widget(self.label)
        box.add_widget(btn)
        return box


if __name__ == '__main__':
    MyApp().run()