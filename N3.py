def quene_move(first_column, first_row, second_column, second_row):
    moves = [first_column, first_row, second_column, second_row]

    if value_check(moves):
        if (first_row == second_row) and (first_column != second_column):
            return True # verticall move, pass!!

        elif (first_row != second_row) and (first_column == second_column):
            return True # horizontal move, pass!!

        if abs(first_row - second_row) == abs(first_column - second_column):
            return True
 
    # Opponent is safe
    return False
def value_check(moves_list):
    values = list(map(lambda x: (x > 0) and (x < 9), moves_list))
    return True if values else False


if __name__ == '__main__':
    fr, fc = 1, 4
    sr, sc = 5, 8
    if quene_move(fc, fr, sc, sr):
        print("Yes")
    else:
        print("No")
