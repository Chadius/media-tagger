import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget


class TitleScreen(Widget):
    pass


class UISwitcherApp(App):
    def build(self):
        return TitleScreen()

if __name__ == '__main__':
    UISwitcherApp().run()

