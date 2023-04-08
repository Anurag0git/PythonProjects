# Treasure Map 2.0
row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = (
  input("Where do you want to put the treasure?(ex: 13 i.e row-1; column-3\n"))

row_to_be_marked_x = int(position[0])
col_to_be_mark_x = int(position[1])

map[row_to_be_marked_x - 1][col_to_be_mark_x - 1] = " x"
print(f"{row1}\n{row2}\n{row3}")
