import time
from exhaustive import solveNQueensExhaustive

n = 10

start_time = time.time()
solutions = solveNQueensExhaustive(n)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for idx, solution in enumerate(solutions, start=1):
    print(f"Solution {idx}:")
    for row in solution:
        print(row)
    print("\n" + "-" * (2 * n - 1) + "\n")
print(f"Elapsed time: {elapsed_time:.6f} seconds\n")
