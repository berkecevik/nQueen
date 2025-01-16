from genetic import GeneticAlgorithms
import time

POPULATIONSIZE = 100
GENERATIONS = 5000
MUTATIONRATE = 0.2

print("Genetic Algorithm\n")

print("Genetic Algorithm For 10x10 Board\n")
geneticAlgorithm = GeneticAlgorithms(10)
startTime = time.time()
geneticAlgorithm.Solve(POPULATIONSIZE, GENERATIONS, MUTATIONRATE)
endTime = time.time()
print(f"Function execution time: {endTime-startTime:.6f} seconds\n")


print("Genetic Algorithm For 50x50 Board\n")
geneticAlgorithm = GeneticAlgorithms(50)
startTime = time.time()
geneticAlgorithm.Solve(POPULATIONSIZE, GENERATIONS, MUTATIONRATE)
endTime = time.time()
print(f"Function execution time: {endTime-startTime:.6f} seconds\n")


print("Genetic Algorithm For 100x100 Board\n")
geneticAlgorithm = GeneticAlgorithms(100)
startTime = time.time()
geneticAlgorithm.Solve(POPULATIONSIZE, GENERATIONS, MUTATIONRATE)
endTime = time.time()
print(f"Function execution time: {endTime-startTime:.6f} seconds\n")
