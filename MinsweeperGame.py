import array

array_dim = 3
mine_feild_string = "x,m"

def create_minefeild(dim, minfeild_input):
    minefeild = []
    game_view = []
    for row_string in minfeild_input.split(','):
        row = []
        game_view_row = []
        for cells in row_string:
            row.append(cells)
            game_view_row.append('x')
        minefeild.append(row)
        game_view.append(game_view_row)
    return minefeild, game_view

minefeild, game_view = create_minefeild(array_dim, mine_feild_string)

def O(row, col):
    if game_view[row][col] == 'O':
        return
    if(minefeild[row][col] == 'm'):
        raise Exception("Oops Game over")

    game_view[row][col] = 'O'

def F(row, col):
    if game_view[row][col] != 'x':
        return
    game_view[row][col] = 'F'

def is_mine_feild_clear():
    all_mines_flagged = True
    for i, row in enumerate(minefeild):
        for j, cell in enumerate(row):
            if cell == 'm' and game_view[i][j] != 'F':
                all_mines_flagged = False

    for row in game_view:
        for cell in row:
            if cell == 'x':
                all_mines_flagged = False

    if all_mines_flagged:
        print("You have cleared all")


O(0,0)
F(1,0)
print(minefeild, game_view)
is_mine_feild_clear()



#min_F[0,2] -> 'm' -> there is mine
#min_f[1,2] -> 'x' -> there is no mine




