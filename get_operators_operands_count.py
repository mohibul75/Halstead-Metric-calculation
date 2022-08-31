
#import json


#with open('operands.json', 'r', encoding='utf-8') as operandsJson:
 #   OPERANDS = set(json.load(operandsJson))



def get_operators_operands_count(tokens):
    OPERANDS= [
  "Literal",
  "Integer",
  "DecimalInteger",
  "OctalInteger",
  "BinaryInteger",
  "HexInteger",
  "FloatingPoint",
  "DecimalFloatingPoint",
  "HexFloatingPoint",
  "Boolean",
  "Character",
  "String",
  "Null",
  "Annotation",
  "Identifier"
]

#https://www.geeksforgeeks.org/java-tokens/
#https://www.edureka.co/blog/tokens-in-java/
#https://docs.oracle.com/javase/specs/jls/se8/html/jls-3.html#jls-3.5

#    Keywords
#    Identifiers
#    Literals

    # Integer
    # Floating Point
    #  Character
    #   String
    #    Boolean

#    Operators
#    Special Symbols




    operands = {}
    operators = {}

    for token in tokens:
        value = token.value

        if token.__class__.__name__ in OPERANDS:
            operands[value] = operands.get(value, 0) + 1
        else:
            operators[value] = operators.get(value, 0) + 1

    return operators, operands