"""Config: This object tracks user settings (resolution, keybindings, audio, etc.)
"""

class BaseSettingsModel(object):
    """This stores per-OS settings.
    """

    def __init__(self, *args, **kwargs):
        # A dict that tracks all fullscreen changes. This should be serializable.
        self.pending_changes = { }

        # All of the values, stored in a serializable dict.
        self.all_values = { }

        # Set to default.
        self.initialize_settings()

    def initialize_settings(self):
        """Resets settings.
        """
        self._fullscreen('initialize')

    def reset_settings(self):
        """Resets settings.
        """
        self._fullscreen('reset')

    def set(self, name, value):
        """Tries to mark a settings change as penidng.
        Use apply_pending_changes() to permanently set it.
        """
        function_by_name = {
            'fullscreen': self._fullscreen
        }

        try:
            function_by_name[name]('set_pending_value', value)
        except KeyError:
            print ("Unknown setting: {setting_name}".format(setting_name=name))

    def apply_pending_changes(self):
        """Applies all penidng changes.
        """
        self._fullscreen("apply_penidng_value")

    def get(self, name):
        """Returns the value of the given setting, or None if it's not set/ name isn't found.
        """
        function_by_name = {
            'fullscreen': self._fullscreen
        }

        try:
            return function_by_name[name]('get')
        except KeyError:
            print ("Unknown setting: {setting_name}".format(setting_name=name))
            return None

    def get_pending_changes(self):
        """Returns a dict containing all pending changes.
        """
        return {
            'fullscreen': self._fullscreen('get_pending_value'),
        }

    def _fullscreen(self, action, value=None):
        """Modify fullscreen.
        Override this function when it's time to apply the changes.
        """

        if action == "initialize":
            self.all_values["fullscreen"] = False
            self.pending_changes["fullscreen"] = False

        if action == "reset":
            self.all_values["fullscreen"] = False

        if action == "get_current_value":
            return self.all_values["fullscreen"]

        if action == "get_pending_value":
            return self.pending_changes["fullscreen"]

        if action == "set_pending_value":
            if value:
                self.pending_changes["fullscreen"] = True
            else:
                self.pending_changes["fullscreen"] = False
            return

        if action == "apply_penidng_value":
            # Copy the pending changes over.
            self.all_values["fullscreen"] = self.pending_changes["fullscreen"]
            self.pending_changes["fullscreen"] = None
