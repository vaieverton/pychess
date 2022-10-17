import string

def isEven(num):
    return num % 2 == 0

def read_piece(piece_s):
    piece_s = piece_s.replace(' ', '').split()[0].split()

    x, y, role, team = piece_s[0]

    return string.ascii_lowercase.index(x.lower()), int(y), role, team

def convert_click_to_coordinates(x, y, square_size):
    x = int(x / square_size)
    y = 8 - int(y / square_size)

    return x, y

def locate_piece_clicked(click_x, click_y, pieces):
    for piece in pieces:
        if piece.x == click_x and piece.y == click_y:
            print(piece.type_formated())
            return piece
    
    return None
