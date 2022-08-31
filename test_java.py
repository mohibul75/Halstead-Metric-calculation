import argparse
import os.path
import sys


from javalang import tokenizer


def parse_python_file():
    parser = argparse.ArgumentParser(
        description='outputs Halstead metrics and cyclomatic complexity for a given python file')
    parser.add_argument('java_file', metavar='JAVA_FILE', type=str,
                        help='path to the python file')

    args = parser.parse_args()

    if not os.path.isfile(args.java_file):
        print('Invalid python File')
        sys.exit()

    with open(args.java_file, 'r', encoding='utf-8') as file:
        code = file.read()
        tokens = list(tokenizer.tokenize(code))

        print(tokens)


#        operators, operands = get_operators_operands_count(tokens)


if __name__ == '__main__':
    parse_python_file()


