import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, ai_game): # ai_game gives us access to the alien invasion object we created
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen # we want screen of ship to match up with screen of tha game
        self.screen_rect = ai_game.screen.get_rect() # get_rect method allows 

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # we'll get the images coordinates and save them to self.rect

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom # this is saying the images midbottom is the same as the screens midbottom, this is how we get our ship to always start in the middle of the screen

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
