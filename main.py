import pgzrun

import assets
import classes
from utils.GameState import GameState
from utils.settings import SettingsManager
from utils import Menu
from pygame import Rect

# Game dimensions
WIDTH = GameState.width
HEIGHT = GameState.height

def draw():
    """Main draw function called by PgZero every frame."""
    if GameState.is_screen(GameState.SCREEN_MAIN_MENU):
        Menu.mainMenu.draw(screen) # type: ignore
    elif GameState.is_screen(GameState.SCREEN_SETTINGS):
        Menu.settingsMenu.draw(screen) # type: ignore
    elif GameState.is_screen(GameState.SCREEN_GAME):
        # Draw game screen (to be implemented)
        pass

def update():
    """Update function called by PgZero every frame."""
    if GameState.is_screen(GameState.SCREEN_QUIT):
        print("Exiting game...")
        #TODO close the game somehow

def update_mouse(pos, button=None):
    """Update function to handle mouse movement on main menu."""
    for gameobject in GameState.game_objects:
        gameobject.update(pos, button)

def on_mouse_move(pos):
    """Handle mouse movement events."""
    update_mouse(pos)

def on_mouse_down(pos, button):
    """Handle mouse button down events."""
    print(f"Mouse down at {pos} with button {button}")
    update_mouse(pos, button)

def main():
    # Initialize game and start PgZero
    settings_manager = SettingsManager("settings.txt")
    print("Loaded settings")
    # Loading Main Menu
    GameState.set_screen(GameState.SCREEN_MAIN_MENU)

    print("Game initialized")
    print("Game started")



main()