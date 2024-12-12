import sys
from antlr4 import *
from .HardScriptLexer import HardScriptLexer
from .HardScriptParser import HardScriptParser
from .server import server
from pygls.server import *


def main():
  server.start_tcp('127.0.0.1', 8080)


if __name__ == '__main__':
  main()
