from GameState import GameState
from utils.settings import SettingsManager
from utils.Background import Background

# Game dimensions
WIDTH = GameState.width
HEIGHT = GameState.height

def draw():
    """Main draw function called by PgZero every frame."""
    for gameobject in GameState.game_objects:
        gameobject.draw(screen) #type: ignore


def update():
    """Update function called by PgZero every frame."""
    if GameState.is_screen(GameState.SCREEN_QUIT):
        #print("Exiting game...")
        #TODO close the game somehow
        pass

def update_mouse(pos, button=None):
    """Update function to handle mouse movement on main menu."""
    for gameobject in GameState.game_objects:
        gameobject.update(pos, button)

def on_mouse_move(pos):
    """Handle mouse movement events."""
    update_mouse(pos)

def on_mouse_down(pos, button):
    """Handle mouse button down events."""
    #print(f"Mouse down at {pos} with button {button}")
    update_mouse(pos, button)

def main():
    # Initialize game and start PgZero
    settings_manager = SettingsManager("settings.txt")
    #print("Loaded settings")
    #print("Initializing game...")
    GameState.add_gameObject(Background("background"))  # Background actor
    #print("Game initialized")
    #print("Loading Main Menu")
    GameState.set_screen(GameState.SCREEN_MAIN_MENU)
    #print("Game started")

main()