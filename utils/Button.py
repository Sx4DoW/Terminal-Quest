from typing import Callable, Optional, Union
import pygame
from pgzero.actor import Actor

from utils.GameObject import GameObject


class Button(GameObject):
    """Button class for interactive clickable buttons.
    Supports either a Rect or an Actor for rendering and hit detection.
    """

    def __init__(
        self,
        target: Union[pygame.Rect, Actor],
        text: str = "",
        text_color: str = "white",
        inactive_color=(50, 50, 50),
        active_color=(100, 100, 100),
        on_click: Optional[Callable[[], None]] = None,
    ):
        """Initialize a button.

        Args:
            target: Either a pygame.Rect or pgzero.Actor defining the button's clickable area.
            text: Text displayed on the button.
            text_color: Color of the button text.
            inactive_color: Color when button is not hovered.
            active_color: Color when button is hovered.
            on_click: Callable action to invoke on click (optional).
        """
        self.text = text
        self.text_color = text_color
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.on_click = on_click

        # Accept either a rect or an actor
        if isinstance(target, Actor):
            self.actor = target
            self.hitbox = target._rect if hasattr(target, "_rect") else target.rect
            self.image = target
        elif isinstance(target, pygame.Rect):
            self.actor = None
            self.hitbox = target
            self.image = None
        else:
            raise TypeError(f"Button target must be a pygame.Rect or Actor, got {type(target)}")

    # ----------------------------
    # Interaction logic
    # ----------------------------
    def is_hovered(self, mouse_pos) -> bool:
        """Check if mouse is over the button."""
        return self.hitbox.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, button) -> bool:
        """Check if button is clicked with left mouse button."""
        return self.is_hovered(mouse_pos) and button == 1

    def update(self, mouse_pos, button=None) -> None:
        """Update the button (handle click events)."""
        if button is not None and self.is_clicked(mouse_pos, button):
            self.click()

    def click(self) -> None:
        """Invoke click action if provided."""
        if self.on_click:
            self.on_click()
    
    def draw(self, screen) -> None:
        """Draw the button on screen."""
        if self.actor:
            # Let the Actor handle its own drawing
            self.actor.draw()
        else:
            color = self.active_color if self.is_hovered(pygame.mouse.get_pos()) else self.inactive_color
            screen.draw.filled_rect(self.hitbox, color)
            screen.draw.textbox(
                self.text,
                color=self.text_color,
                align="center",
                rect=self.hitbox
            )
