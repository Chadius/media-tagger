class YamlFileSettings(BaseSettingsModel):
    """Handles YAML and saving to and from files.
    """

    def save_settings(self, filename):
        """Save the settings to external storage.
        """
        # TODO
        # Collect all current settings.
        # Convert to YAML.
        # Save to a file.
        pass

    def load_settings(self, filename):
        """Load the settings from a file.
        """
        # TODO
        # Load the file from YAML.
        # Convert from YAML to a dict.
        # Call the bast class's load_settings
        pass

    def _get_name_to_function_mapping(self):
        """ This stores a dict of setting names to the function that manages them.
        Subclass this function to add or remove entries.
        """
        return {
            'fullscreen': self._fullscreen
        }

