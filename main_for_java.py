import argparse
import os.path
import sys

from javalang import tokenizer
from tabulate import tabulate


from get_operators_operands_count import get_operators_operands_count
from halstead import calculate_halstead


def print_table(data, headers=[], title=None):

    if title:
        print("\n", title, "\n")
    print(tabulate(data.items(), headers=headers, tablefmt='fancy_grid'))

def print_t(data):
    print(data)

def read_code():
    parser = argparse.ArgumentParser(
        description='outputs Halstead metrics and cyclomatic complexity for a given java file')
    parser.add_argument('java_file', metavar='JAVA_FILE', type=str,
                        help='path to the java file')

    args = parser.parse_args()

    if not os.path.isfile(args.java_file):
        print('Invalid Java File')
        sys.exit()

    with open(args.java_file, 'r', encoding='utf-8') as file:
        code = file.read()
        return code


def parsing():
    code=read_code()
    tokens = list(tokenizer.tokenize(code))

    print(tokens)

    operators, operands = get_operators_operands_count(tokens)

    n1 = len(operators)
    n2 = len(operands)
    N1 = sum(operators.values())
    N2 = sum(operands.values())

    # print_t({"Number of Distinct Operators": n1,
    #              "Number of Distinct Operands": n2,
    #              "Number of Operators": N1,
    #              "Number of Operands": N2,
    #              **calculate_halstead(
    #                  n1, N1, n2, N2)})

    print_table({"Number of Distinct Operators": n1,
                 "Number of Distinct Operands": n2,
                 "Number of Operators": N1,
                 "Number of Operands": N2,
                 **calculate_halstead(
                     n1, N1, n2, N2)}, ['Metric', 'Value'], 'Halstead Metrics:')

    print_table(operators, ['Operator', 'Count'], 'Operators:')

    print_table(operands, ['Operand', 'Count'], 'Operands:')

if __name__ == '__main__':
    parsing()