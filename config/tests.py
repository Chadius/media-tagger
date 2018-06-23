from unittest import TestCase
from unittest.mock import MagicMock

from config.models import KivyGraphicsSettings

class KivyGraphicsSettings(TestCase):
    def test_default_settings(self):
        """Create activity settings config. Do not apply settings.
        Make sure defaults are set.
        """
        #settings = KivyGraphicsSettings(apply_settings = False)

        #fullscreen = settings.get_value('fullscreen')
        #self.assertTrue(fullscreen)
        pass

    def test_load_settings(self):
        """Create graphics settings object. Passing a file -like object.
        Make sure the settings are read from this device.
        """
        pass

    def test_change_settings(self):
        """Create a graphing setting object.
        Change one of the settings
        make sure the setting has been changed.
        """
        pass

    def test_save_settings(self):
        """Create a graphic settings object.
        Change one of the settings and save.
        Make sure the settings file has new settings.
        """
        pass
