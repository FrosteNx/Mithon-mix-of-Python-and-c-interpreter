# Generated from Mithon.g4 by ANTLR 4.13.1
import collections
from antlr4 import ParseTreeListener
from collections import defaultdict

if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

# This class defines a complete listener for a parse tree produced by MithonParser.
class MithonListener(ParseTreeListener):

    # Enter a parse tree produced by MithonParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by MithonParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):
        pass

del MithonParser