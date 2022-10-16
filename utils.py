def isEven(num):
    return num % 2 == 0

def read_piece(piece_s):
    piece_s = piece_s.replace(' ', '').split()[0].split()

    x, y, role, team = piece_s[0]

    return x, y, role, team
    
