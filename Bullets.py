import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the bullet's position.
        self.y -= self.ai_settings.bullet_speed_factor

        # Ensure the bullet's position is valid.
        if self.y < 0:
            self.y = 0  # Reset to a valid position if necessary

        # Update the rect position.
        self.rect.y = self.y

        # Debugging print statement for bullet position
        print(f"Bullet position: {self.y}")
