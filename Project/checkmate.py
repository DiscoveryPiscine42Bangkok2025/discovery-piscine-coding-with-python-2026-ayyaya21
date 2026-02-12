def find_king(board):
    """
    หาและคืนค่าตำแหน่งของ King (K)
    - ถ้ามี King แค่ตัวเดียว → คืน (row, col)
    - ถ้าไม่มี หรือมีมากกว่า 1 ตัว → คืน None
    """
    king_positions = []

    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == 'K':
                king_positions.append((r, c))

    return king_positions[0] if len(king_positions) == 1 else None


def is_valid_board(board):
    """
    ตรวจสอบว่ากระดานถูกต้องหรือไม่
    - ต้องไม่ว่าง
    - ต้องเป็นสี่เหลี่ยมจัตุรัส (NxN)
    """
    if not board:
        return False

    size = len(board)
    for row in board:
        if len(row) != size:
            return False

    return True


def is_path_clear(board, start, end, step):
    """
    ตรวจว่าทางเดินจาก start ไป end มีหมากขวางหรือไม่
    ใช้กับ Rook / Bishop / Queen
    """
    r, c = start
    dr, dc = step

    # เดินทีละช่องไปหาคิง
    r += dr
    c += dc

    while (r, c) != end:
        if board[r][c] != '.':  # มีหมากขวางทาง
            return False
        r += dr
        c += dc

    return True


def threatens_king(board, piece, pos, king_pos):
    """
    ตรวจว่าหมากตัวนี้สามารถรุก King ได้หรือไม่
    """
    r, c = pos
    kr, kc = king_pos

    # Pawn รุกแนวทแยง 1 ช่อง
    if piece == 'P':
        return abs(r - kr) == 1 and abs(c - kc) == 1

    # Rook และ Queen (แนวนอน / แนวตั้ง)
    if piece in 'RQ':
        # แนวนอน
        if r == kr:
            step = (0, 1 if kc > c else -1)
            return is_path_clear(board, (r, c), (kr, kc), step)

        # แนวตั้ง
        if c == kc:
            step = (1 if kr > r else -1, 0)
            return is_path_clear(board, (r, c), (kr, kc), step)

    # Bishop และ Queen (แนวทแยง)
    if piece in 'BQ':
        if abs(r - kr) == abs(c - kc):
            step = (
                1 if kr > r else -1,
                1 if kc > c else -1
            )
            return is_path_clear(board, (r, c), (kr, kc), step)

    return False


def checkmate(board):
    """
    ตรวจสอบว่ามีหมากใดรุก King อยู่หรือไม่
    """
    # ตรวจความถูกต้องของกระดาน
    if not is_valid_board(board):
        print("Fail")
        return

    # หาตำแหน่ง King
    king_pos = find_king(board)
    if not king_pos:
        print("Fail")
        return

    # วนตรวจหมากทุกตัวบนกระดาน
    for r, row in enumerate(board):
        for c, piece in enumerate(row):
            if piece == '.':  # ช่องว่าง ข้าม
                continue

            # ถ้าหมากตัวนี้รุก King ได้
            if threatens_king(board, piece, (r, c), king_pos):
                print("Success")
                return

    # ไม่มีหมากใดรุก King
    print("Fail")
