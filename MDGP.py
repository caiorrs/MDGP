import numpy
import random
import time
import math

def geneticAlgorithm(self, weights, numberOfCandidates, theSeed):
    print("Genetic Algorithm")
    state_current = weights
    initialPopulation = []
    print("Initial score")
    #print(self.run_episode(state_current))

    numpy.random.seed(theSeed)
    initialPopulation = numpy.random.uniform(-10,10,(numberOfCandidates,len(state_current)))
    for i in range(len(initialPopulation)):
        for j in range(len(initialPopulation[i])):
            initialPopulation[i][j]+=state_current[j]


    iterator = 10
    while(iterator > 0):
        finalDescendants = []
        fitness = []
        for i in initialPopulation:
            fitness.append(self.run_episode(i))

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
