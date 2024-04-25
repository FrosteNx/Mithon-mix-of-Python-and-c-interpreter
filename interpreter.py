from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from MithonLexer import MithonLexer
from MithonParser import MithonParser
from MithonVisitor import MithonVisitor
from MithonListener import MithonListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Błąd w linii: {line}. Treść błędu: {msg}")

def main():
    input_stream = FileStream("test.mithon")
    lexer = MithonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MithonParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    try:
        tree = parser.program()
    except SyntaxError as e:
        print(e)
        exit(1)

    variable_listener = MithonListener()
    walker = ParseTreeWalker()
    walker.walk(variable_listener, tree)
    
    variables = variable_listener.variables

    visitor = MithonVisitor(variables)
    visitor.visit(tree)

if __name__ == '__main__':
    main()