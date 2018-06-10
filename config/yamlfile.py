import yaml

# TODO Import Kivy stuff.

class YamlFileSettings(BaseSettingsModel):
    """Handles YAML and saving to and from files.
    """

    def save_settings(self, filename):
        """Save the settings to external storage.
        """
        # Collect all current settings.
        current_values = self.get_current_values()

        # Open the file for saving purposes:
        try:
            settings_file = open(filename, 'w')
        except OSError as e:
            raise

        # Convert to YAML.
        try:
            current_yaml = yaml.dump(current_values, settings_file)
        except yaml.YAMLError as e:
            raise

        settings_file.close()

    def load_settings(self, filename):
        """Load the settings from a file.
        """
        # Load the file.
        try:
            file_yaml = open(filename, 'r')
        except OSError as e:
            raise

        # Convert from YAML to a dict.
        try:
            settings_dict = yaml.load(file_yaml)
        except yaml.YAMLError as e:
            raise

        # Call the base class's load_settings.
        self.load_settings(settings_dict)

    def _get_name_to_function_mapping(self):
        """ This stores a dict of setting names to the function that manages them.
        Subclass this function to add or remove entries.
        """
        return {
            'fullscreen': self._fullscreen
            'resolution': self._resolution
        }

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

    def _resolution(self, action, value=None):
        """Modify resolution.
        Override this function when it's time to apply the changes.
        """

        if action == "initialize":
            self.all_values["resolution"] = {
                "width": 800,
                "height": 600,
            }
            self.pending_changes["resolution"] = {
                "width": None,
                "height": None,
            }

        if action == "reset":
            self.all_values["resolution"] = {
                "width": 800,
                "height": 600,
            }

        if action == "get_current_value":
            return self.all_values["resolution"]

        if action == "get_pending_value":
            return self.pending_changes["resolution"]

        if action == "set_pending_value":
            self.pending_changes["resolution"] = value
            return

        if action == "apply_penidng_value":
            self.apply_changes_hook('resolution', self.all_values["resolution"], self.pending_changes["resolution"])
            # Copy the pending changes over.
            self.all_values["resolution"] = self.pending_changes["resolution"]
            self.pending_changes["resolution"] = {
                "width": None,
                "height": None,
            }

