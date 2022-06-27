# https://leetcode.com/problems/valid-sudoku/
# Best submission time: 98ms

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col, box = {}, {}
        for i in range(9):
            row = set()
            line = board[i]
            for j in range(9):
                el = line[j]
                if el.isdigit():
                    # check row
                    if el in row: 
                        return False
                    
                    # Check col
                    if j not in col:
                        col[j] = set()
                    elif el in col[j]: 
                        return False
                    
                    # Check box
                    box_index = f'{i//3}{j//3}'
                    if box_index not in box: 
                        box[box_index] = set()
                    elif el in box[box_index]:
                        return False
                    
                    row.add(el)
                    col[j].add(el)
                    box[box_index].add(el)
                
        return True