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
    def setUp(self):
        self.settings = TestSettingsModel()

    def test_update_settings(self):
        """Confirm you can update settings using the generic set call.
        """
        # Change the fullscreen setting
        self.settings.set("fullscreen", True)

        # Confirm the pending field was updated
        self.assertFalse(self.settings.get("fullscreen"))
        self.assertTrue(self.settings.get_pending_changes()["fullscreen"])

        # Change a setting that doesn't exist, you shouldn't see anything
        self.settings.set("bogus", "800")

        # Now apply the settings changes
        self.settings.apply_pending_changes()

        # The fullscreen should be set.
        self.assertFalse(self.settings.get("fullscreen"))
        self.assertIsNone(self.settings.get_pending_changes()["fullscreen"])

    def test_reset_to_defaults(self):
        """Confirm you can reset settings.
        """
        pass

    def test_save_settings(self):
        """Confirm you can save settings to a permanent storage.
        """
        pass

    def test_load_settings(self):
        """Confirm you can load settings from a permanent storage.
        """
        pass
