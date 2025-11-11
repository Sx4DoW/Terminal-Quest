"""Game state module for Terminal Quest.

This module exposes a class-based (static) GameState. The class uses
class attributes to store application-wide state so it behaves like a
static container.
"""

from typing import List

from utils.GameObject import GameObject
from utils.SparseSet import SparseSet

class GameState:
    """Static-like container for global game state.

    All attributes are class attributes and therefore shared across the
    application. Use the provided classmethods for controlled updates
    when side-effects or validation are required.
    """

    # Valid screen identifiers
    SCREEN_MAIN_MENU: str = "Main Menu"
    SCREEN_SETTINGS: str = "Settings"
    SCREEN_GAME: str = "Game"
    SCREEN_QUIT: str = "Quit"

    # Display dimensions
    width: int = 1280
    height: int = 720

    # Current screen identifier
    current_screen: str = SCREEN_MAIN_MENU

    # List of game objects
    game_objects: List[GameObject] = SparseSet()

    # General volume
    general_volume: bool = True
    # Music volume
    music_volume: bool = True

    @classmethod
    def set_screen(cls, name: str) -> None:
        """Change the current screen with validation.

        Args:
            name: Screen identifier (use SCREEN_* class constants)

        Raises:
            ValueError: If screen name is not valid
        """
        from utils.Menu import mainMenu, settingsMenu
        menu_objs = {
            cls.SCREEN_MAIN_MENU: mainMenu,
            cls.SCREEN_SETTINGS: settingsMenu,
            cls.SCREEN_GAME: None,
            cls.SCREEN_QUIT: None,
        }
        valid_screens = (cls.SCREEN_MAIN_MENU, cls.SCREEN_SETTINGS, cls.SCREEN_GAME, cls.SCREEN_QUIT)
        
        if name not in valid_screens:
            raise ValueError(f"Invalid screen: {name}. Must be one of {valid_screens}")
        
        GameState.remove_gameObject(menu_objs.get(cls.current_screen))
        GameState.add_gameObject(menu_objs.get(name))

        cls.current_screen = name

    @classmethod
    def is_screen(cls, name: str) -> bool:
        """Check if the current screen matches the given name.

        Args:
            name: Screen identifier to check

        Returns:
            True if current_screen matches name, False otherwise
        """
        return cls.current_screen == name
    
    @classmethod
    def add_gameObject(cls, obj: GameObject) -> None:
        """Add a game object to the global list.

        Args:
            obj: Game object instance to add
        """
        cls.game_objects.add(obj)

    @classmethod
    def remove_gameObject(cls, obj: GameObject) -> None:
        """Remove a game object from the global list.

        Args:
            obj: Game object instance to remove
        """
        cls.game_objects.remove(obj)

    @classmethod
    def general_volume_status(cls) -> str:
        """Get the current general volume status as a string.

        Returns:
            "On" if general volume is enabled, "Off" otherwise
        """
        return "On" if cls.general_volume else "Off"
    
    @classmethod
    def music_volume_status(cls) -> str:
        """Get the current music volume status as a string.

        Returns:
            "On" if music volume is enabled, "Off" otherwise
        """
        return "On" if cls.music_volume else "Off"
    
    @classmethod
    def toggle_general_volume(cls) -> None:
        """Toggle the general volume setting."""
        cls.general_volume = not cls.general_volume
    
    @classmethod
    def toggle_music_volume(cls) -> None:
        """Toggle the music volume setting."""
        cls.music_volume = not cls.music_volume