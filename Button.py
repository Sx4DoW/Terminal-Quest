from pygame import Rect

class Button:
    """A clickable button with hover detection."""
    def __init__(self, rect: Rect, text: str, text_color="white", inactive_color=(50, 50, 50), active_color=(100, 100, 100)):
        """Initialize a button.
        
        Args:
            rect: Pygame Rect defining button position and size
            text: Text displayed on the button
        """
        self.rect = rect
        self.text = text
        self.is_hovered = False
        self.text_color = text_color
        self.inactive_color = inactive_color
        self.active_color = active_color
    
    def update(self, mouse_pos):
        """Update button state based on mouse position.
        
        Args:
            mouse_pos: Tuple of (x, y) mouse coordinates
        """
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    def is_clicked(self, mouse_pos):
        """Check if button was clicked at given position.
        
        Args:
            mouse_pos: Tuple of (x, y) mouse coordinates
            
        Returns:
            True if click is within button rect, False otherwise
        """
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen):
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