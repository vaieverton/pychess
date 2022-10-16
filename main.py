import pygame
from pygame.locals import *
from pieces import Piece
from utils import isEven, read_piece

green = (0, 136, 71)
white = (240, 240, 240)

size = 600,600
width, height = size

square_size = width / 8

def draw_board(screen):
     for row in range(9):
        for column in range(9):
            left = (row-1) * square_size
            top = (column-1) * square_size

            color = white

            if (not isEven(row) and isEven(column)) or (isEven(row) and not isEven(column)):
                color = green

            pygame.draw.rect(screen, color, pygame.Rect((left, top, square_size, square_size)))

def read_initial_pieces(screen):
    with open('./initial_positions.txt') as f:
        lines = f.readlines()

        for line in lines:
            x, y, r, t = read_piece(line)
            piece = Piece(x, y, r, t)
            piece.image(screen, square_size)


def main():
    pygame.init()
    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        draw_board(screen)
        
        read_initial_pieces(screen)


        pygame.display.flip()



if __name__ == '__main__': main()