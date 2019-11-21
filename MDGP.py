import argparse
import sys
from pprint import pprint

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def main(args):
    filename = args.file[0].name
    seed = args.seed
    shouldMeasureTime = args.time

    kGraph = []

    with open(filename, 'r') as f:
        # M - number of elements - number of nodes
        # G - number of groups - edges
        # GT - group type "ss" or "ds"
        first_line = f.readline().split()
        M, G = first_line[:2]
        GT = first_line[2]
        limits = first_line[3:]
        for line in f:
            e1, e2, d = line.split()
            e1, e2, d = int(e1), int(e2), float(d)
            kGraph.append([[e1, e2], d])

    print("kGraph")
    pprint(kGraph)
    # valores minimos para cada grupo
    a = limits[::2]
    # valores maximos para cada grupo
    b = limits[1::2]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Uses Genetic Algorithm to find solution for MDGP.',
        usage='MGDP.py [-h] [--file myinstance.txt] [--seed 1234ABCD] [--time n]')

    parser.add_argument('-f', '--file', type=open, nargs=1,
                        help='a file containing the instance',
                        required=True)

    parser.add_argument(
        '-s', '--seed', type=str, nargs=1, help='Seed to generate random numbers')

    parser.add_argument(
        '-t', '--time', action='store_true', help='Measure and print mean execution time')
    # argumento é o numero de vezes que o algoritmo deve ser rodado

    args = parser.parse_args()
    print(args.file[0].name)
    print(args.seed)
    print(args.time)

    main(args)
