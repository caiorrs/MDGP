import argparse
import sys
from pprint import pprint
import numpy
import random
import time
import math



def getFitness(vertexes,weights):
    fitness = 0
    for i in range(len(vertexes)):
        for j in range(i + 1, len(vertexes)):
            for k in weights:
                if((vertexes[i] == k[0] and vertexes[j] == k[1]) or (vertexes[i] == k[1] and vertexes[j] == k[0])):
                    fitness+=k[2]
    return fitness

def getExcludedValues(vertexes,chosenValues):
    excludedValues = []
    for i in vertexes:
        count = 0
        for j in chosenValues:
            for k in j:
                if(i == k):
                    count+=1
        if(count == 0):
            excludedValues.append(i)
    return excludedValues


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def geneticAlgorithm( weights,vertexes, numberOfCandidates,numberOfGroups, theSeed, theIterationNumber):
    print("Genetic Algorithm")
    state_current = weights
    vertexList = list(range(0, vertexes))
    initialPopulation = []

    #numpy.random.seed(int(time.time()))
    numpy.random.seed(theSeed)
    numpy.random.shuffle(vertexList)
    initialPopulation = list(chunks(vertexList, numberOfCandidates))
    print("POP INICIAL")
    print(initialPopulation)


    iterator = theIterationNumber
    while(iterator > 0):
        finalDescendants = []
        fitness = []
        excludedValues = []

        chosenPopulation = theChoice(initialPopulation, numberOfCandidates)
        excludedValues = getExcludedValues(vertexList,chosenPopulation)
        fitness = numpy.zeros(len(chosenPopulation))
        for i in range(len(chosenPopulation)):
                fitness[i] += (getFitness(chosenPopulation[i],state_current))

        descendants = matching(chosenPopulation)
        descendants = numpy.array_split(descendants,numberOfGroups)
        #print("DESC")
        #print(descendants)
        if(excludedValues):
            finalDescendants, excludedValues = mutateGenesWithExcluded(descendants, excludedValues)
        else:
            finalDescendants = descendants
            #finalDescendants = mutateGenes(descendants)

        groupFit = numpy.zeros(len(finalDescendants))
        for i in range(len(finalDescendants)):
            for j in range(len(finalDescendants[i])):
                groupFit[i] += (getFitness(finalDescendants[i][j],state_current))
        maxIndex = numpy.argpartition(groupFit, -1)[-1:]
        #if(groupFit[maxIndex[0]] > sum(fitness)):
        #    finalDescendants = finalDescendants[maxIndex[0]]
        #else:
        #    finalDescendants = chosenPopulation
        finalDescendants = finalDescendants[maxIndex[0]]
        fitness = []
        for i in finalDescendants:
            fitness.append(getFitness(i,state_current))
        print("Mid pop")
        print(finalDescendants)
        print("Mid score")
        print(sum(fitness))
        initialPopulation = finalDescendants
        initialPopulation = numpy.append(initialPopulation,excludedValues)
        initialPopulation = list(chunks(initialPopulation, numberOfCandidates))
        iterator-=1

    print("POP FINAL")
    print(finalDescendants)
    fitness = []
    for i in finalDescendants:
        fitness.append(getFitness(i,state_current))
    print("ESSE E O FITNESS FINAL")
    print(fitness)
    maxValue = max(fitness)
    for i in range(len(fitness)):
        if(maxValue == fitness[i]):
            bestChoice = i
    print("Final score")
    print(sum(fitness))
    #return finalDescendants[bestChoice]


def mutateGenesWithExcluded(candidates, excluded):
    if(numpy.random.randint(10) == 1):
        indSon = numpy.random.randint(0,len(candidates))
        indGroup = numpy.random.randint(0,len(candidates[indSon]))
        indValue = numpy.random.randint(0,len(candidates[indSon][indGroup]))
        indExc = numpy.random.randint(0,len(excluded))
        candidates[indSon][indGroup][indValue],excluded[indExc] = excluded[indExc],candidates[indSon][indGroup][indValue]

    return candidates, excluded

def mutateGenes(candidates):
    if(numpy.random.randint(10) == 1):
        indCand1 = numpy.random.randint(0,len(candidates[0]))
        indCand2 = numpy.random.randint(0,len(candidates[1]))
        candidates[0][indCand1],candidates[1][indCand2] = candidates[1][indCand2] ,candidates[0][indCand1]

    return candidates

def matching( chosen):
    descendants = []
    for i in range(len(chosen)):
        if(i+1 < len(chosen)):
            descendants.extend( crossover(chosen[i],chosen[i+1]))
    return descendants

def crossover( candidate1, candidate2):
    numpy.random.shuffle(candidate1)
    numpy.random.shuffle(candidate2)
    #can1 = candidate1
    #can2 = candidate2
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
    #finalArray.append(can1)
    #finalArray.append(can2)

    return finalArray

def theChoice( candidates, limit):
    chosenOnes=[]
    for i in candidates:
        if (len(i) == limit):
            chosenOnes.append(i)
    return chosenOnes

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def main(args):
    filename = (args.file[0].name)
    popSize = (args.population)
    groups = (args.groups)
    seed = (args.seed)
    shouldMeasureTime = (args.time)

    forest = []

    with open(filename, 'r') as f:
        # M - number of elements - number of nodes
        # G - number of groups - edges
        # GT - group type "ss" or "ds"
        # LL - lower limit
        # UL - upper limit
        first_line = f.readline().split()
        M ,G = first_line[:2]
        GT = first_line[3]
        limits = first_line[3:]
        for line in f:
            e1, e2, d = line.split()
            e1, e2, d = int(e1), int(e2), float(d)
            forest.append([e1, e2, d])

    #print("forest")
    #pprint(forest)
    if(popSize * groups > int(M)):
        print("Valor de indivíduos maior que o permitido")
        quit()

    geneticAlgorithm(forest,int(M),popSize,groups,seed,shouldMeasureTime)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Uses Genetic Algorithm to find solution for MDGP.',
        usage='MGDP.py [-h] [--file myinstance.txt] [--population n] [--groups n] [--seed 1234ABCD] [--time n]')

    parser.add_argument('-f', '--file', type=open, nargs=1,
                        help='a file containing the instance',
                        required=True)
    parser.add_argument(
        '-p', '--population',type=int, help='Population Size')
    parser.add_argument(
        '-g', '--groups',type=int, help='Group Size')

    parser.add_argument(
        '-s', '--seed', type=int, help='Seed to generate random numbers')

    parser.add_argument(
        '-t', '--time',type=int, help='Measure and print mean execution time')
    # argumento é o numero de vezes que o algoritmo deve ser rodado


    args = parser.parse_args()
    print(args.file[0].name)
    print(args.population)
    print(args.groups)
    print(args.seed)
    print(args.time)

    main(args)
