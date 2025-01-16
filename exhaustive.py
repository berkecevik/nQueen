def solveNQueensExhaustive(n):
    def dfs(row, state):
        if row == n:
            if is_valid(state):
                board = ["  ".join(row) for row in state]
                solutions.append(board)
            return

        for col in range(n):
            new_row = ["."] * n
            new_row[col] = "Q"
            state.append(new_row)
            dfs(row + 1, state)
            state.pop()

    def is_valid(state):
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i].index("Q") == state[j].index("Q") or \
                   abs(i - j) == abs(state[i].index("Q") - state[j].index("Q")):
                    return False
        return True

    solutions = []
    dfs(0, [])
    return solutions