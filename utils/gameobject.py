"""Base class for all game objects."""


class GameObject:
    """Base class for all game objects.

    Provides a common interface for drawable and updatable objects
    in the game. Subclasses should override draw() and optionally update().
    """

    def __init__(self, hoverable: bool = False, draggable: bool = False) -> None:
        """Initialize the game object."""
        self.hoverable = hoverable
        self.draggable = draggable

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