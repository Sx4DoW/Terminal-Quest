"""Base class for all game objects."""
from typing import Union
from pygame import Rect
from pgzero.actor import Actor


class GameObject:
    """Base class for all game objects.

    Provides a common interface for drawable and updatable objects
    in the game. Subclasses should override draw() and optionally update().
    """

    def __init__(
            self,
            target: Union[Rect, Actor],
            hoverable: bool = False,
            draggable: bool = False,
            collidable: bool = False
    ):
        """Initialize the game object."""
        self.target = target
        self.hoverable = hoverable
        self.draggable = draggable
        self.collidable = collidable

    def draw(self, screen) -> None:
        """Draw the game object on screen.

        Args:
            screen: PgZero screen object

        Raises:
            NotImplementedError: Subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must implement draw()")

    def update(self, *args, **kwargs) -> None:
        """Update the game object state.

        This method is optional and can be overridden by subclasses
        that need to respond to input or other state changes.

        Args:
            *args: Positional arguments (e.g., mouse position)
            **kwargs: Keyword arguments
        """
        pass

    def isDrawable(self) -> bool:
        """Check if the object is drawable.

        Returns:
            True if the object has either a rect or an actor, False otherwise.
        """
        return self.hitbox is not None or self.image is not None