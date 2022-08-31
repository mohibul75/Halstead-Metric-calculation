code = """
j=6
if a > b :
    if a == 5 : 
        if b == 6 :
            print(a)
else :
    print(b)

for i in range(5):
    print(i)
"""

code2 = """
def func1():
    print(a)
"""



import ast

class node_visit(ast.NodeVisitor):

    #def visit(self, node) :
     #   nodes = []
    #    ast.NodeVisitor.generic_visit(self, node)

       # print(ast.dump(node))

    def visit_Compare(self, node):
        print('Node type: Compare\nFields:', len(node._fields))
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        print('Node type: Name\nFields:', len(node._fields))
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Constant(self, node):
        print('Node type: Constant\nFields:', len(node._fields))
        ast.NodeVisitor.generic_visit(self, node)

  #      print(nodes)


def return_halstead():
    parsed_code = ast.parse(code)


    node_v= node_visit()
    node_v.visit(parsed_code)

  #  print(ast.dump(parsed_code))

    f = open("demofile2.txt", "a")
    f.write(ast.dump(parsed_code))
    f.close()





if __name__ == '__main__':

    return_halstead()
