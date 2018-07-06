from functools import partial
import subprocess

import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

from settings.kivy import KivySettings
from event.command.scene import SceneChangeCommand
from event.command.scene import SceneChangeController

class MainWindow(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        # Create a consumer of SceneChangeCommands.
        self.scene_change_controller = SceneChangeController()

        # Periodically add an update call.
        Clock.schedule_interval(partial(self.update), 1/60.0)

    def change_scene(self, scene_name):
        """Queues an attempt to change the scene.
        """
        known_screens = (
            'title_screen',
            'game_screen',
        )
        # If it's not a known scene, ignore it
        if not scene_name in known_screens:
            return

        # Create a new SceneChangeCommand with the new scene.
        new_command = SceneChangeCommand(actor=self, scene=scene_name)

        # Add the new command to the contorller.
        self.scene_change_controller.add_command(new_command)

    def update(self, dt):
        """Tries to execute periodically.
        dt = The amount of time.
        """
        # Process all scene change commands.
        self.scene_change_controller.process_commands()

class ManageTagScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def play_video(self):
        """Ask MPlayer to play the video.
        """
        subprocess.run(["ls", "-l"])
        subprocess.run(
            [
                "mplayer",
                "/Users/Shared/Adobe/Premiere Pro/12.0/Tutorial/Going Home project/Footage/A001_C037_0921FG_001.mp4",
                "-idle",
                "-fixed-vo",
                "-osdlevel", "3",
                "-geometry", "10%:10%",
            ]
        )
        pass

class UISwitcherApp(App):
    def build(self):
        screen_manager = MainWindow(transition=FadeTransition())
        screen_manager.add_widget(ManageTagScreen(name="manage_tag"))
        screen_manager.current = 'manage_tag'
        return screen_manager

if __name__ == '__main__':
    # First set up graphics settings.
    settings = KivySettings(filename="user/settings.ini")

    UISwitcherApp().run()

