from checkmate import checkmate

def run_test_scenario(test_name, board_str):
    print(f"Testing: {test_name}")
    print("Board Preview:")
    print(board_str)
    
    # แปลง String เป็น List ตามรูปแบบที่ checkmate ต้องการ
    board = board_str.strip().splitlines()
    
    print("Result: ", end="")
    checkmate(board)
    print("-" * 30 + "\n")

def main():
    # --- SCENARIO 1: SUCCESS cases (King โดนรุก) ---
    
    # 1.1 Rook Attack (ทางสะดวก)
    board_rook_attack = """\
R...
.K..
....
....\
"""
    run_test_scenario("Rook Attacks King", board_rook_attack)

    # 1.2 Bishop Attack (แนวทแยง)
    board_bishop_attack = """\
B...
....
..K.
....\
"""
    run_test_scenario("Bishop Attacks King", board_bishop_attack)

    # --- SCENARIO 2: BLOCKED cases (มีตัวกัน = รอด) ---
    
    # 2.1 Rook Blocked by Pawn (มี P บัง R อยู่)
    board_rook_blocked = """\
R...
P...
K...
....\
"""
    run_test_scenario("Rook Blocked by Pawn", board_rook_blocked)

    # --- SCENARIO 3: ERROR Handling (ดักจับ Error) ---
    
    # 3.1 No King (ลืมใส่ King)
    board_no_king = """\
R...
....
....
....\
"""
    run_test_scenario("Error: No King", board_no_king)

    # 3.2 Bad Board Shape (กระดานเบี้ยว ไม่ใช่จัตุรัส)
    board_bad_shape = """\
..K.
....
..\
"""
    run_test_scenario("Error: Bad Board Shape", board_bad_shape)

    # 3.3 Multiple Kings (มี King 2 ตัว)
    board_two_kings = """\
K...
..K.
....
....\
"""
    run_test_scenario("Error: Multiple Kings", board_two_kings)

if __name__ == "__main__":
    main()