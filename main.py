import os
from antlr4 import *
from gen.trabalhoFinal_lucasLexer import trabalhoFinal_lucasLexer
from gen.trabalhoFinal_lucasParser import trabalhoFinal_lucasParser
from MyListener import trabalhoFinal_lucasListener

if __name__ == '__main__':
    file = FileStream("teste.txt")

    # parte lexica
    lexer = trabalhoFinal_lucasLexer(file)
    streams = CommonTokenStream(lexer)

    # parte analise sintatica
    parser = trabalhoFinal_lucasParser(streams)
    tree = parser.prog()

    # parte analise semantica
    filename = 'programa_final'
    l = trabalhoFinal_lucasListener(filename)
    walker = ParseTreeWalker()
    walker.walk(l, tree)

    # executar o programa .j
    # os.system('java -jar jasmin.jar {}'.format(filename + '.j'))
    # os.system('java {}'.format(filename))