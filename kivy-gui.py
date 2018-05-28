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
        # Did the actor start executing?
        self.is_started_execution = False
        # Did the actor finish executing?
        self.is_finished_execution = False

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

        # A list of Command objects
        self.command_queue = []
        # The last completed queue

    def add_command(self, new_command):
        """Adds a Command to the queue.
        """
        self.command_queue.append(new_command)

    def process_commands(self):
        """Tries to process commands.
        """
        # If the queue is empty, return
        if len(self.command_queue) == 0:
            return

        # If the first Command is still executing, return later.
        current_command = self.command_queue[0]

        if current_command.is_started_execution and not current_command.is_finished_execution:
            return

        # If the first Command has finished executing, remove it from the queue now.
        if current_command.is_started_execution and not current_command.is_finished_execution:
            self.command_queue.pop(0)
        # Process through the commands.
        commands_to_remove = []
        for command in self.command_queue:
            # Process known Commands.
            # TODO

            # If a Command is still executing, stop processing commands and return.
            if not command.is_finished_execution:
                break

            # If the process completed, remove it from the queue.
            if command.is_finished_execution:
                commands_to_remove.append(command)

            # If the command wasn't started, then we don't recognize this command. Raise an Error.
            # TODO
        # Remove all commands marked for removal.
        for command in commands_to_remove:
            self.command_queue.remove(command)

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

