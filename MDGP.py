import argparse
import sys
from pprint import pprint
import numpy
import random
import time
import math

def geneticAlgorithm(self, weights, numberOfCandidates, theSeed, theIterationNumber):
    print("Genetic Algorithm")
    state_current = weights
    initialPopulation = []
    print("Initial score")
    #print(self.run_episode(state_current))
    #USAR DISTANCIA EUCLIDIANA PARA CALCULAR fitness
    #dist = numpy.linalg.norm(a-b)

    numpy.random.seed(theSeed)
    initialPopulation = numpy.random.uniform(-10,10,(numberOfCandidates,len(state_current)))
    for i in range(len(initialPopulation)):
        for j in range(len(initialPopulation[i])):
            initialPopulation[i][j]+=state_current[j]


    iterator = theIterationNumber
    while(iterator > 0):
        finalDescendants = []
        fitness = []
        for i in initialPopulation:
            fitness.append(i[2])

        chosenPopulation = self.tournamentChoice(initialPopulation, fitness, numberOfCandidates/2)
        descendants = self.matching(chosenPopulation,numberOfCandidates/2)

        finalDescendants = self.mutateGenes(descendants)
        initialPopulation = finalDescendants
        maxValue = max(fitness)
        for i in range(len(fitness)):
            if(maxValue == fitness[i]):
                bestChoice = i

        print("Mid score")
        #print(self.run_episode(finalDescendants[bestChoice]))
        iterator-=1

    fitness = []
    for i in finalDescendants:
        fitness.append(self.run_episode(i))
    maxValue = max(fitness)
    for i in range(len(fitness)):
        if(maxValue == fitness[i]):
            bestChoice = i
    print("Final score")
    #print(self.run_episode(finalDescendants[bestChoice]))
    return finalDescendants[bestChoice]


def mutateGenes(self, candidates):
    for i in range(len(candidates)):
        for j in range(len(candidates[i])):
            if(numpy.random.randint(100) == 1):
                candidates[i][j] += numpy.random.uniform(-0.5,0.5)

    return candidates

def matching(self, chosen, numberOfParts):
    parts = []
    dividedParts = []
    parts = numpy.array_split(chosen,numberOfParts)
    limit = int(numberOfParts)
    indexes = list(range(0,limit))
    for i in range(limit):
        value = numpy.random.choice(indexes)
        dividedParts.append(parts[value])
        indexes.remove(value)

    dplimit = len(dividedParts)
    descendants = []
    for i in range(0,limit,2):
        if ((dplimit - i) == 1):
            descendants.extend( self.crossover(dividedParts[i],dividedParts[i]))
        else:
            descendants.extend( self.crossover(dividedParts[i],dividedParts[i+1]))
    return descendants

def crossover(self, candidate1, candidate2):
    c1 = numpy.array_split(candidate1,2)
    c2 = numpy.array_split(candidate2,2)
    c3 = numpy.array_split(candidate1,4)
    c4 = numpy.array_split(candidate2,4)
    child1=[]
    child2=[]
    child3 = []
    child4 = []
    finalArray = []
    child1.extend(c1[0])
    child1.extend(c2[1])
    child2.extend(c2[0])
    child2.extend(c1[1])
    child3.extend(c3[0])
    child3.extend(c4[1])
    child3.extend(c3[2])
    child3.extend(c4[3])
    child4.extend(c4[0])
    child4.extend(c3[1])
    child4.extend(c4[2])
    child4.extend(c3[3])
    finalArray.append(child1)
    finalArray.append(child2)
    finalArray.append(child3)
    finalArray.append(child4)

    return finalArray

def tournamentChoice(self, candidates, fitness, limit):
    localFitness = fitness
    chosenOnes=[]
    round=0
    while(round<limit):

        combatant0 = numpy.random.randint(0,len(fitness))
        fitness0 = fitness[combatant0]
        combatant1 = numpy.random.randint(0,len(fitness))
        fitness1 = fitness[combatant1]
        combatant2 = numpy.random.randint(0,len(fitness))
        fitness2 = fitness[combatant2]
        combatant3 = numpy.random.randint(0,len(fitness))
        fitness3 = fitness[combatant3]
        chosenFitness = max(fitness0,fitness1,fitness2,fitness3)


        if (chosenFitness == fitness0):
            chosenOnes.extend(candidates[combatant0])
        elif (chosenFitness == fitness1):
            chosenOnes.extend( candidates[combatant1])
        elif (chosenFitness == fitness2):
            chosenOnes.extend(candidates[combatant2])
        elif (chosenFitness == fitness3):
            chosenOnes.extend(candidates[combatant3])
        round+=1

    return chosenOnes

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def main(args):
    filename = (args.file[0].name)
    popSize = (args.population)
    seed = (args.seed)
    shouldMeasureTime = (args.time)

    forest = []

    with open(filename, 'r') as f:
        # M - number of elements - number of nodes
        # G - number of groups - edges
        # GT - group type "ss" or "ds"
        # LL - lower limit
        # UL - upper limit
        first_line = f.readline().strip()
        M, G = first_line[:2]
        GT = first_line[3]
        limits = first_line[3:]
        for line in f:
            e1, e2, d = line.split()
            e1, e2, d = int(e1), int(e2), float(d)
            forest.append([e1, e2, d])

    print("forest")
    pprint(forest)
    self.geneticAlgorithm(forest,popSize,seed,shouldMeasureTime)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Uses Genetic Algorithm to find solution for MDGP.',
        usage='MGDP.py [-h] [--file myinstance.txt] [--population n] [--seed 1234ABCD] [--time n]')

    parser.add_argument('-f', '--file', type=open, nargs=1,
                        help='a file containing the instance',
                        required=True)
    parser.add_argument(
        '-p', '--population',type=int, help='Population Size')

    parser.add_argument(
        '-s', '--seed', type=int, help='Seed to generate random numbers')

    parser.add_argument(
        '-t', '--time',type=int, help='Measure and print mean execution time')
    # argumento é o numero de vezes que o algoritmo deve ser rodado


    args = parser.parse_args()
    print(args.file[0].name)
    print(args.population)
    print(args.seed)
    print(args.time)

    main(args)
