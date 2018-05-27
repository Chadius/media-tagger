from functools import partial

import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class MainWindow(FloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        # Add a callback to switch to the title screen when the system finishes initializing
        Clock.schedule_once(partial(MainWindow.init_go_to_title_screen, self), 0.0)

    def init_go_to_title_screen(self, dt):
        """Switch to the title screen once the system has initialized.
        """
        # Add a TitleScreen.
        title_screen = TitleScreen()
        self.add_widget(title_screen)

    def callback_switch_to_title(self, dt):
        self.switch_to_title()

    def command(self, verb, **kwargs):
        """An API to send commands to the controller.
        """

        function_by_verb = {
            "add": self.add_new_screen,
            "close": self.close_screen,
        }

        if verb in function_by_verb:
            function_by_verb[verb](**kwargs)
        pass

    def add_new_screen(self, **kwargs):
        """Creates and adds a new game screen.

        screen_name - String referring to the name of the screen.
        """
        screen_name = kwargs["screen_name"]

        print ("Add new game screen " + screen_name)

        screen_class_by_name = {
            "title": TitleScreen,
            "game": GameScreen,
        }

        if screen_name in screen_class_by_name:
            new_screen = screen_class_by_name[screen_name]()
            self.add_widget(new_screen)

    def close_screen(self, screen_name, **kwargs):
        print ("Close game screen " + screen_name)

        screen_class_by_name = {
            "title": TitleScreen,
            "game": GameScreen,
        }

        pass

class TitleScreen(FloatLayout):
    def switch_to_game_screen(self):
        """Close this widget and open the Game Screen.
        """

        # Ask the parent to open the GameScreen.
        self.parent.command("add", screen_name="game")
        # Ask the parent to close this widget.
        # self.parent.command("close", "title")
        pass

class GameScreen(FloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        print ("I'm a Game Screen!")
        pass

class UISwitcherApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    UISwitcherApp().run()

