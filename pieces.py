import pygame
from pygame.locals import *
import string

class Piece():
    def __init__(self, x, y, role, team) -> None:
        self.x = x
        self.y = y
        self.role = role
        self.team = team

    def position(self):
        return self.x, self.y

    def role(self):
        return self.role

    def team(self):
        return self.team
    
    def move(self, x, y):
        self.x = x
        self.y = y

        print(x, y)

    def image(self, screen, square_size):
        width, _ = pygame.display.get_surface().get_size()

        left = self.x * square_size
        top = width - self.y * square_size

        img_size = (square_size * 0.95, square_size * 0.95)

        picture = pygame.image.load(self.handle_image_url())
        picture = pygame.transform.scale(picture, img_size)

        screen.blit(picture, (left, top))

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
        
    def position_formated(self):
        return f'{self.type_formated()} {string.ascii_lowercase[self.x].upper()}{self.y}'

    def type_formated(self):
        team = ''
        role = ''
        if self.team == 'P':
            team = 'Pretas'
        if self.team == 'B':
            team = 'Brancas'

        if self.role == 'T':
            role = 'Torre'
        if self.role == 'B':
            role = 'Bispo'
        if self.role == 'C':
            role = 'Cavalo'
        if self.role == 'D':
            role = 'Dama'
        if self.role == 'R':
            role = 'Rei'
        if self.role == 'P':
            role = 'Peão'

        return f'{role} {string.ascii_lowercase[self.x].upper()}{self.y} {team}'
