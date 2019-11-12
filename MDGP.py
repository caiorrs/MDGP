import argparse
import sys
from pprint import pprint

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def main(args):
    filename = (args.file[0].name)
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
