import pygame
from pygame.locals import *
import string

class Piece():
    def __init__(self, x, y, role, team) -> None:
        self.x = string.ascii_lowercase.index(x.lower())
        self.y = int(y)
        self.role = role
        self.team = team

    def position(self):
        return self.x, self.y

    def role(self):
        return self.role

    def team(self):
        return self.team
    
    def image(self, screen, square_size):
        width, _ = pygame.display.get_surface().get_size()

        left = self.x * square_size
        top = width - self.y * square_size

        img_size = (square_size * 0.95, square_size * 0.95)

        picture = pygame.image.load(self.handle_image_url())
        # picture = 
        picture = pygame.transform.scale(picture, img_size)
        screen.blit(picture, (left, top))

        return picture

    def handle_image_url(self):
        team = ''
        if self.team == 'P':
            team = 'black'
        if self.team == 'B':
            team = 'white'

        piece = ''
        if self.role == 'T':
            piece = 'torre'
        
        if self.role == 'B':
            piece = 'bispo'

        if self.role == 'C':
            piece = 'cavalo'

        if self.role == 'P':
            piece = 'peao'

        if self.role == 'D':
            piece = 'dama'

        if self.role == 'R':
            piece = 'rei'

        return f'./imgs/{piece}_{team}.png'
        