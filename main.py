import argparse
import ast
import os.path
import sys
import radon
from radon.metrics import *
from tabulate import tabulate
from halstead import calculate_halstead

def print_table(data, headers=[], title=None):

    if title:
        print("\n", title, "\n")
    print(tabulate(data.items(), headers=headers, tablefmt='fancy_grid'))

def print_halstead(hal):

    print_table({"Number of Distinct Operators": hal.h1,
                 "Number of Distinct Operands": hal.h2,
                 "Number of Operators": hal.N1,
                 "Number of Operands": hal.N2,
                 "Program vocabulary": hal.vocabulary,
                 "Program length": hal.calculated_length,
                 "Estimated length": hal.length,
                 "Purity ratio": hal.length / hal.calculated_length,
                 "Volume": hal.volume,
                 "Difficulty": hal.difficulty,
                 "Program effort": hal.effort,
                 "Time required to program": hal.time,
                 "Number of delivered bugs": hal.bugs}, ['Metric', 'Value'], 'Halstead Metrics:')

    # print("^^^^^^^^^Halstead^^^^^^^^\n\n\n")
    # print(" n1: the number of distinct operators = "+str(hal.h1))
    # print(" n2: the number of distinct operands = "+str(hal.h2))
    # print("N1: the total number of operators = "+str(hal.N1) )
    # print("N2: the total number of operands= " +str(hal.N2))
    # print("n: the vocabulary, i.e. n1 + n2= "+ str(hal.vocabulary))
    # print("N: the length, i.e. N1 + N2 = "+ str(hal.length))
    # print("calculated_length: n1 * log2(n1) + n2 * log2(n2) = "+ str(hal.calculated_length))
    # print("volume: V = N * log2(n)= "+ str(hal.volume))
    # print("difficulty: D = n1 / 2 * N2 / n2= "+ str(hal.difficulty))
    # print("effort: E = D * V ="+ str(hal.effort))
    # print("time: T = E / 18 seconds ="+ str(hal.time))
    # print("bugs: B = V / 3000 - an estimate of the errors in the implementation ="+ str(hal.bugs)+"\n\n\n")
    # print("^^^^^^^^^END Halstead^^^^^^^^\n\n\n")


class method_return(ast.NodeVisitor):
    def visit_FunctionDef(self,node):
      print(node)


def Halstead_for_python_file(code):

        hal=radon.metrics.h_visit(code)
        #print(hal)
        print_halstead(hal.total)

        #for n in hal.total.funtions:
        #print_halstead(hal.functions[0])




def Halstead_for_funtion(code):

    hal = radon.metrics.h_visit_ast(code)
    # print(hal)
    print_halstead(hal.total)

def print_loc(ret):

    print_table({"LOC: Total number of lines": ret.loc,
                 "LLOC_: Logical LOC. Excluding blank lines and comment lines": ret.lloc,
                 "SLOC_: Source LOC. Excluding blank lines": ret.sloc,
                 "Comments: Comment line": ret.comments,
                 "Multi: A multi-line string": ret.multi,
                 "Blank: blank line": ret.blank,
                 "Single Comments: single comments": ret.single_comments},['Metric', 'Value'], 'Halstead Metrics:')

def return_loc(code):
    ret = radon.raw.analyze(code)

    print("******LOC*******\n\n\n")
    print_loc(ret)
    # print("LOC: Total number of lines="+str(ret.loc))
    # print("LLOC_: Logical LOC. Excluding blank lines and comment lines =" + str(ret.lloc))
    # print("SLOC_: Source LOC. Excluding blank lines =" + str(ret.sloc))
    # print("Comments: Comment line =" + str(ret.comments))
    # print("Multi: A multi-line string =" + str(ret.multi))
    # print("Blank: blank line =" + str(ret.blank))
    # print("Single Comments: single comments =" + str(ret.single_comments)+"\n\n\n")
#   print(ret)

    print("******END LOC*******\n\n\n")


def read_code():
    parser = argparse.ArgumentParser(
        description='outputs Halstead metrics and cyclomatic complexity for a given python file')
    parser.add_argument('python_file', metavar='PYTHON_FILE', type=str,
                        help='path to the python file')

    args = parser.parse_args()

    if not os.path.isfile(args.python_file):
        print('Invalid python File')
        sys.exit()

    with open(args.python_file, 'r', encoding='utf-8') as file:
        code = file.read()
        return code


if __name__ == '__main__':
    code= read_code()

    methods=method_return()
    fun_nodes=methods.visit(ast.parse(code))

    # print(dir(fun_nodes))
    # nodes=[]
    # nodes=dir(fun_nodes)

  #  for node in nodes:
  #      Halstead_for_funtion(node)


    return_loc(code)
    Halstead_for_python_file(code)


