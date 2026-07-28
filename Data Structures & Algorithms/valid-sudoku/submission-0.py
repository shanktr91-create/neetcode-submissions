class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        column = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        sub_box = {}
        

        for i in range(9):
            row = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            for j in range(9):

                if board[i][j] in list(row.keys()):
                    row[board[i][j]]+=1
            for x in row.values():
                if (x>1):
                    return False

        
        for i in range(9):
            column = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            for j in range(9):

                if board[j][i] in list(column.keys()):
                    column[board[j][i]]+=1
            for x in column.values():
                if (x>1):
                    return False

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):

                sub_box = {
                    "1":0,"2":0,"3":0,"4":0,"5":0,
                    "6":0,"7":0,"8":0,"9":0
                }

                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if board[i][j] in sub_box:
                            sub_box[board[i][j]] += 1
                            if sub_box[board[i][j]] > 1:
                                return False
        return True