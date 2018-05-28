from functools import partial

import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

class Command(object):
    """Encapsulate an request that acts upon an object.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self, args, kwargs)
        # Track the object that will act.
        self.actor = None
        # Did the actor finish executing?
        self.completed_acting = False

    def execute(self):
        """Perform the command on the actor.
        """
        pass

    def undo(self):
        """Reverse the effects of the execute command.
        """
        pass

class MainWindow(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def command(self, verb, **kwargs):
        """An API to send commands to the controller.
        """

        function_by_verb = {
            "add": self.add_new_screen,
            "close": self.close_screen,
            "switch": self.switch_screen,
        }

        if verb in function_by_verb:
            function_by_verb[verb](**kwargs)

    def switch_screen(self, **kwargs):
        """Switches to an already existing screen.
        """
        self.current = kwargs["screen_name"]
        pass

    def add_new_screen(self, **kwargs):
        """Creates and adds a new game screen.

        screen_name - String referring to the name of the screen.
        """
        screen_name = kwargs["screen_name"]

        screen_class_by_name = {
            "title": TitleScreen,
            "game": GameScreen,
        }

        if screen_name in screen_class_by_name:
            new_screen = screen_class_by_name[screen_name]()
            self.add_widget(new_screen)

    def close_screen(self, **kwargs):
        widget_to_close = kwargs["screen_widget"]
        self.remove_widget(widget_to_close)


    def update(self, dt):
        """Tries to execute periodically.
        dt = The amount of time.
        """
        pass

class TitleScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def switch_to_game_screen(self):
        """Close this widget and open the Game Screen.
        """

        # Ask the parent to switch to the Game screen
        self.parent.command("switch", screen_name="game_screen")

class GameScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def switch_to_title_screen(self):
        """Close this widget and open the Title Screen.
        """

        # Ask the parent to switch to the Game screen
        self.parent.command("switch", screen_name="title_screen")

class UISwitcherApp(App):
    def build(self):
        screen_manager = MainWindow(transition=FadeTransition())
        screen_manager.add_widget(TitleScreen(name="title_screen"))
        screen_manager.add_widget(GameScreen(name="game_screen"))
        screen_manager.current = 'title_screen'
        return screen_manager

if __name__ == '__main__':
    UISwitcherApp().run()

