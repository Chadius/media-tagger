from unittest import TestCase
from unittest.mock import MagicMock

from config.base import BaseSettingsModel
from config.base import UnknownSettingException

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
        self.settings.set_pending("fullscreen", True)

        # Confirm the pending field was updated
        self.assertFalse(self.settings.get("fullscreen"))
        self.assertTrue(self.settings.get_pending_changes()["fullscreen"])

        # Change a setting that doesn't exist, it should raise an error
        with self.assertRaises(UnknownSettingException):
            self.settings.set_pending("bogus", "800")

        # Now apply the settings changes
        self.settings.apply_pending_changes()

        # The fullscreen should be set.
        self.assertTrue(self.settings.get("fullscreen"))
        self.assertIsNone(self.settings.get_pending_changes()["fullscreen"])

    def test_reset_to_defaults(self):
        """Confirm you can reset settings.
        """
        # Get the initial setting
        initial_fullscreen = self.settings.get("fullscreen")

        # Change and apply the fullscreen setting.
        if initial_fullscreen:
            self.settings.set_pending("fullscreen", False)
        else:
            self.settings.set_pending("fullscreen", True)
        self.settings.apply_pending_changes()

        self.assertNotEqual(self.settings.get("fullscreen"), initial_fullscreen)

        # Reset settings.
        self.settings.reset_settings()

        # Settings should match the initial setting.
        self.assertEqual(self.settings.get("fullscreen"), initial_fullscreen)
        pass

    def test_save_settings(self):
        """Confirm you can save settings to a permanent storage.
        """
        pass

    def test_load_settings(self):
        """Confirm you can load settings from a permanent storage.
        """
        pass
