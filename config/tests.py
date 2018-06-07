from unittest import TestCase
from unittest.mock import MagicMock

from config.base import BaseSettingsModel

class TestSettingsModel(BaseSettingsModel):
    """This will use text to save to and from.
    """
    pass

class SettingsModelTest(TestCase):
    """Checks that you can load and save settings.
    """
    def setup(self):
        pass

    def test_update_settings(self):
        pass

    def test_save_settings(self):
        pass

    def test_load_settings(self):
        pass
