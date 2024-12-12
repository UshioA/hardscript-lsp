import sys
from antlr4 import *
from HardScriptLexer import HardScriptLexer
from HardScriptParser import HardScriptParser


def main(argv):
  pass
  input_stream = FileStream(argv[1])
  lexer = HardScriptLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = HardScriptParser(stream)
  tree = parser.design()
  print(tree.toStringTree(recog=parser))
