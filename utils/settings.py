"""Utility functions for reading, writing, and editing settings in a settings.txt file.
Each setting is expected to be in the format: KEY = VALUE"""

class SettingsManager:
    def __init__(self, filename = "settings.txt", settings_dict=None) -> None:
        """Initializes the settings manager.
        Args:
            filename (str): The name of the settings file. Defaults to "settings.txt".
            settings_dict (dict, optional): Initial settings dictionary. Defaults to None."""
        
        # Store the filename
        self.settings_filename = filename

        # Trying to open or create the settings file
        try:
            open(self.settings_filename, 'r', encoding='utf-8').close()
        except FileNotFoundError:
            print(f"Settings file '{self.settings_filename}' not found. Creating a new one.")
            try:
                open(self.settings_filename, 'w', encoding='utf-8').close()
            except Exception as e:
                print(f"Error creating settings file: {e}")
            

        # Initialize settings dictionary
        if settings_dict is None:
            self.settings = {}
        else:
            self.settings = settings_dict

    def get_settings(self) -> dict:
        """Returns the current settings dictionary."""
        return self.settings_dict
    
    def set_settings(self, settings_dict: dict) -> None:
        """Sets the settings dictionary to the provided one.
        Args:
            settings_dict (dict): The new settings dictionary."""
        self.settings_dict = settings_dict
        self.save_settings()

    def save_settings(self) -> None:
        """Saves the current settings dictionary to the settings file."""
        with open(self.settings_filename, 'w', encoding='utf-8') as file:
            for key, val in self.settings.items():
                file.write(f"{key} = {val}\n")

    def restore_settings(self) -> None:
        """Restores settings from the settings file into the settings dictionary."""
        settings = {}
        with open(self.settings_filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    line = line.strip()
                    if '=' in line:
                        key, val = line.split('=', 1)
                        settings[key.strip()] = val.strip()
                except ValueError:
                    print(f"Error: Could not parse line: {line}")
        self.settings = settings

    def edit_setting(self, key: str, value: str) -> None:
        """Edits a specific setting in the settings dictionary and saves it to the file.
        Args:
            key (str): The setting key to edit.
            value (str): The new value for the setting."""
        try:
            self.settings[key]
            self.save_settings()
        except KeyError:
            print(f"Error: Setting '{key}' not found.")
            return
        