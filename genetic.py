import random

class GeneticAlgorithms:

    def __init__(self, sizeOfBlock):  # Fixed constructor
        self.blockSize = sizeOfBlock

    def DisplayBoard(self, board):
        for row in board:
            print(" ".join("Q" if i == row else "x " for i in range(self.blockSize)))
        print()

    def Fitness(self, board):
        n = len(board)
        maxPairs = n * (n - 1) // 2
        attackingPairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(board[i] - board[j]) == abs(i - j):
                    attackingPairs += 1

        return maxPairs - attackingPairs

    def GeneratePopulation(self, populationSize):
        population = []
        for _ in range(populationSize):
            board = list(range(self.blockSize))
            random.shuffle(board)
            population.append(board)
        return population

    def Crossover(self, parent1, parent2):
        point1 = random.randint(0, self.blockSize - 2)
        point2 = random.randint(point1 + 1, self.blockSize - 1)
        child = [-1] * self.blockSize

        for i in range(point1, point2 + 1):
            child[i] = parent1[i]

        current_index = 0
        for value in parent2:
            if value not in child:
                while child[current_index] != -1:
                    current_index += 1
                child[current_index] = value

        return child

    def Mutate(self, board, mutationRate):
        if random.random() < mutationRate:
            i, j = random.sample(range(len(board)), 2)
            board[i], board[j] = board[j], board[i]
        return board

    def CreateNewGeneration(self, population, fitnessScores, populationSize, eliteSize, mutationRate):
        sorted_population = [board for _, board in sorted(zip(fitnessScores, population), reverse=True)]
        elites = sorted_population[:eliteSize]
        nextGeneration = elites[:]

        while len(nextGeneration) < populationSize:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = self.Crossover(parent1, parent2)
            child = self.Mutate(child, mutationRate)
            nextGeneration.append(child)

        return nextGeneration

    def Solve(self,POPULATION_SIZE,GENERATIONS,MUTATION_RATE,ELITE_SIZE = 20):
        population = self.GeneratePopulation(POPULATION_SIZE)

        for generation in range(GENERATIONS):
            fitnessScores = [self.Fitness(board) for board in population]
            maxFitness = max(fitnessScores)

            if maxFitness == self.blockSize * (self.blockSize - 1) // 2:
                print(f"Solution found in generation {generation}\n")
                self.DisplayBoard(population[fitnessScores.index(maxFitness)])
                return True

            population = self.CreateNewGeneration(population, fitnessScores, POPULATION_SIZE, ELITE_SIZE, MUTATION_RATE)

        print("No solution found.")
        return False