import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """ Initialize button attributes. """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimensions and properties of button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button's message prepping (one only)
        self.prep_msg(msg)
