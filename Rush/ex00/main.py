from checkmate import checkmate

def main():
### 1 ###
#     board = """\
# ....
# ..K.
# ....
# B...\
# """ 

### 2 ###
#     board = """\
# ..
# .K\
# """

## 3 ###
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