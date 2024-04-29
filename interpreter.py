from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from freshLexer import freshLexer
from freshParser import freshParser
from freshVisitor import freshVisitor

class freshErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Błąd w linii: {line}. Treść błędu: {msg}")

def main():
    input_stream = FileStream("test.fresh")
    lexer = freshLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = freshParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(freshErrorListener())

    try:
        tree = parser.program()
    except SyntaxError as e:
        print(e)
        exit(1)

    visitor = freshVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()