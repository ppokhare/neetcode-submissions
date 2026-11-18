class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # use hashmp of sets for O(1) lookup and duplicate
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue # pass just skips to next line, continue goes to new loop

                # tuple are hashable
                if (
                    board[i][j] in rowSet[i]
                    or board[i][j] in colSet[j]
                    or board[i][j] in boxSet[(i // 3, j // 3)]
                ):
                    return False

                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                boxSet[(i // 3, j // 3)].add(board[i][j])

        return True
