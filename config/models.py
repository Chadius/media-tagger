from kivy.config import Config

class KivyGraphicsSettings:
     """This class handles all of the graphics config settings.
     """

     def __init__(self, *args, **kwargs):
         self.load_settings(**kwargs)
         self.apply_settings()

     def load_settings(self, **kwargs):
         """Load graphics configuration settings. Does not actually apply settings.
         filename - optional string argument. This will try to open the file with that filename instead.
         file - optional file-like object argument. This will try to use the file-like object as the configuration file.

         If neither argument is used, the function will use the built-in Kivy configuration (or default values if it can't be found.)
         """
         # TODO: need research config
         #self.temp_fullscreen = something.load(graphics, fullscreen)
         pass

     def save_settings(self, **kwargs):
         """Saves the current graphics configuration settings.
         filename - optional string argument. This will try to open the file with that filename instead.
         file - optional file-like object argument. This will try to use the file-like object as the configuration file.

         If neither argument is used, the function will use the built-in Kivy configuration.
         """

         #TODO: research Kivy configuration to figure out how this works.

         #something.save(graphics, fullscreen, self.temporary_fullscreen)
         pass

     def apply_settings(self):
         """After loading the settings, this will actually apply the changes.
         This will affect settings.
         """
         #from kivy.core.window import Window
         #TODO: research to these graphics settings and then apply them here.
         pass

     def change_settings(self, setting_name, value):
         """Changes the giving setting name to the given value.
         """
         pass

     def get_setting(self, setting_name):
         """Returns the value for the given setting.
         """
         pass
