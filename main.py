import pygame
from pygame.locals import *
from pieces import Piece
from utils import convert_click_to_coordinates, isEven, read_piece, locate_piece_clicked

green = (0, 136, 71)
white = (240, 240, 240)

size = 600,600
width, height = size

square_size = width / 8

pieces = []

def draw_board(screen):
     for row in range(9):
        for column in range(9):
            left = (row-1) * square_size
            top = (column-1) * square_size

            color = white

            if (not isEven(row) and isEven(column)) or (isEven(row) and not isEven(column)):
                color = green

            pygame.draw.rect(screen, color, pygame.Rect((left, top, square_size, square_size)))

def read_initial_pieces():
    with open('./initial_positions.txt') as f:
        lines = f.readlines()

        for line in lines:
            x, y, r, t = read_piece(line)
            piece = Piece(x, y, r, t)

            pieces.append(piece)

def draw_pieces(_screen, _pieces):
    for piece in _pieces:
        piece.image(_screen, square_size)

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Chess')

    screen = pygame.display.set_mode(size)

    mousex, mousey = 0, 0

    pressed = False
    piece_selected = None

    read_initial_pieces()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # mouse clicked
        if pygame.mouse.get_pressed()[0] == True and not piece_selected:
            mousex, mousey = pygame.mouse.get_pos()
            x, y = convert_click_to_coordinates(mousex, mousey, square_size)
            piece_selected = locate_piece_clicked(x, y, pieces)
            pressed = True

        if pygame.mouse.get_pressed()[0] == True and pressed and piece_selected:
            mousex, mousey = pygame.mouse.get_pos()
            x, y = convert_click_to_coordinates(mousex, mousey, square_size)
            print(x, y)
            piece_selected.move(x, y)
            piece_selected = None
            pressed = False

        
        draw_board(screen)
            
        draw_pieces(screen, pieces)


        pygame.display.flip()



if __name__ == '__main__': main()