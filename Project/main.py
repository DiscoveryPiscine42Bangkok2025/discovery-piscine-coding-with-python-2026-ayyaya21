from checkmate import checkmate

def main():
    board = """\
....
..K.
....
B...\
""" 

# def main():
#     board = """\
# ..
# .K\
# """

# def main():
#     board = """\
# .R..
# .K..
# ....
# ....\
# """ 

    board = board.strip().splitlines()
    checkmate(board)

main()
#test with python3 main.py | cat -e