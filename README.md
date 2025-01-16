# nQueen Solver

This repository contains implementations of two approaches to solve the N-Queens problem: an **Exhaustive Search Algorithm** and a **Genetic Algorithm**. The N-Queens problem is a classic combinatorial problem where the goal is to place N queens on an N×N chessboard so that no two queens attack each other.

## Project Structure

- **`exhaustive.py`**: Contains the implementation of the exhaustive search algorithm to solve the N-Queens problem.
- **`genetic.py`**: Implements a genetic algorithm for solving the N-Queens problem.
- **`run_exhaustive.py`**: A script to execute the exhaustive algorithm for a specific board size and measure its performance.
- **`run_genetic.py`**: A script to run the genetic algorithm on multiple board sizes and configurations, showcasing its performance and flexibility.

## How It Works

### Exhaustive Search
The exhaustive algorithm recursively explores all possible configurations of queens on the board. It validates each configuration to ensure no two queens attack each other. While accurate, this method becomes computationally expensive as the board size increases.

### Genetic Algorithm
The genetic algorithm uses evolutionary principles to find solutions:
1. **Population Generation**: Creates an initial set of random board configurations.
2. **Fitness Evaluation**: Measures how close each configuration is to a valid solution.
3. **Selection, Crossover, Mutation**: Iteratively improves the population to converge toward valid solutions.
4. **Stopping Condition**: Ends once a valid solution is found or after a specified number of generations.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nqueens-solver.git
   cd nqueens-solver
