"""Config: This object tracks user settings (resolution, keybindings, audio, etc.)
"""
class UnknownSettingException(Exception):
    pass

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

    def _get_name_to_function_mapping(self):
        """ This stores a dict of setting names to the function that manages them.
        Subclass this function to add or remove entries.
        """
        return {
            'fullscreen': self._fullscreen
        }

    def initialize_settings(self):
        """Resets settings.
        """
        function_by_name = self._get_name_to_function_mapping()
        for setting_name, setting_function in function_by_name.items():
            setting_function('initialize')

    def reset_settings(self):
        """Resets settings.
        """
        function_by_name = self._get_name_to_function_mapping()
        for setting_name, setting_function in function_by_name.items():
            setting_function('reset')

    def set_pending(self, name, value):
        """Tries to mark a settings change as penidng.
        Use apply_pending_changes() to permanently set it.
        """
        function_by_name = self._get_name_to_function_mapping()
        try:
            function_by_name[name]('set_pending_value', value)
        except KeyError:
            raise UnknownSettingException("Unknown setting: {setting_name}".format(setting_name=name))

    def apply_pending_changes(self):
        """Applies all penidng changes.
        """
        function_by_name = self._get_name_to_function_mapping()
        for setting_name, setting_function in function_by_name.items():
            setting_function("apply_penidng_value")

    def get(self, name):
        """Returns the value of the given setting, or None if it's not set/ name isn't found.
        """
        function_by_name = self._get_name_to_function_mapping()

        try:
            return function_by_name[name]('get_current_value')
        except KeyError:
            raise UnknownSettingException("Unknown setting: {setting_name}".format(setting_name=name))

    def get_current_values(self):
        """Returns a dict containing all current values.
        """
        function_by_name = self._get_name_to_function_mapping()

        current_values = {}

        for setting_name, setting_function in function_by_name.items():
            current_values[setting_name] = setting_function('get_current_value')

        return current_values

    def get_pending_changes(self):
        """Returns a dict containing all pending changes.
        """
        function_by_name = self._get_name_to_function_mapping()

        pending_values = {}

        for setting_name, setting_function in function_by_name.items():
            pending_values[setting_name] = setting_function('get_pending_value')

        return pending_values

    def apply_changes_hook(self, setting_name, current_value, pending_value):
        """Perform any behavior before settings changes are applied.
        For example, a graphics card would actually change the resolution based on the pending change.
        """
        pass

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
            self.apply_changes_hook('fullscreen', self.all_values["fullscreen"], self.pending_changes["fullscreen"])
            # Copy the pending changes over.
            self.all_values["fullscreen"] = self.pending_changes["fullscreen"]
            self.pending_changes["fullscreen"] = None

    def save_settings(self):
        """Save the settings to external storage.
        Override this function to implement some kind of saving mechanism.
        """
        pass

    def load_settings(self, new_settings_dict):
        """Given a dictionary, set and apply all of the settings in the dictionary.
        Override this function if you need to open a file-like object or interpret data differently.
        """
        function_by_name = self._get_name_to_function_mapping()

        for setting_name, new_value in new_settings_dict.items():
            # If the setting name is in the function by name
            if setting_name in function_by_name:
                # Set the pending value
                self.set_pending(setting_name, new_value)

        # Apply the pending value
        self.apply_pending_changes()

