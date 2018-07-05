from functools import partial

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color
from kivy.graphics import Rectangle

class GameScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(
            partial(
                GameScreen.update,
                self
            ),
            1.0 / 30.0
        )

    def switch_to_title_screen(self):
        """Close this widget and open the Title Screen.
        """

        # Ask the parent to switch to the Game screen
        self.parent.change_scene("title_screen")

    def update(self, dt):
        # Stop if this window isn't active.
        if not self.parent:
            return

        self.draw_tiles(dt)

    def draw_tiles(self, dt):
        """
        """

        # Stop if this window isn't active.
        if not self.parent:
            return

        # Draw a box
        with self.canvas:
            Color(1.0, 0.0, 0.0)
            Rectangle(pos=(740,20), size=(70, 220))
