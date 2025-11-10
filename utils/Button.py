from typing import Callable, Optional
from pygame import Rect

from utils.GameObject import GameObject


class Button(GameObject):
    """A clickable button with hover detection and an optional action.

    The action is a zero-argument callable that will be invoked when
    the button is clicked. Using a zero-arg action keeps the Button
    API simple and allows callers to provide closures capturing any
    needed context (for example, the button index).
    """

    def __init__(
        self,
        rect: Rect,
        text: str,
        text_color: str = "white",
        inactive_color=(50, 50, 50),
        active_color=(100, 100, 100),
        on_click: Optional[Callable[[], None]] = None,
    ):
        """Initialize a button.
        
        Args:
            rect: Pygame Rect defining button position and size
            text: Text displayed on the button
            text_color: Color of the button text
            inactive_color: Color when button is not hovered
            active_color: Color when button is hovered
            on_click: Callable action to invoke on click (optional)
        """
        self.rect = rect
        self.text = text
        self.is_hovered = False
        self.text_color = text_color
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.on_click = on_click

    def is_clicked(self, mouse_pos, button) -> bool:
        """Check if the button is clicked based on mouse position.
        
        Args:
            mouse_pos: Tuple of (x, y) mouse coordinates
        Returns:
            True if mouse_pos is within button rect and left mouse button is clicked, False otherwise
        """
        return self.rect.collidepoint(mouse_pos) and button == 1

    def update(self, mouse_pos, button=None) -> None:
        """Update button state based on mouse position.
        
        Args:
            mouse_pos: Tuple of (x, y) mouse coordinates
        """
        print(f"Updating button '{self.text}'")
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        if self.is_clicked(mouse_pos, button):
            self.click()
        #print(f"Button '{self.text}' hovered {self.is_hovered} clicked={self.is_clicked(mouse_pos, button)}")


    def click(self) -> None:
        """Invoke the button's click action, if any."""
        if self.on_click:
            self.on_click()
    
    def draw(self, screen) -> None:
        """Draw the button on screen.
        
        Args:
            screen: PgZero screen object
        """
        # Choose color based on hover state
        color = self.active_color if self.is_hovered else self.inactive_color
        
        # Draw button rectangle
        screen.draw.rect(self.rect, color)
        
        # Draw button text
        screen.draw.textbox(
            self.text,
            color=self.text_color,
            align="center",
            rect=self.rect
        )