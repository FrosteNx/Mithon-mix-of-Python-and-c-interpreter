from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from MithonLexer import MithonLexer
from MithonParser import MithonParser
from MithonVisitor import MithonVisitor, MithonError

    
class MyErrorListener(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "extraneous input" in msg:
            raise SyntaxError(f"Error at line: {line}. Unexpected symbol {offendingSymbol.text}")
        elif "mismatched input" in msg:
            raise SyntaxError(f"Error at line: {line}. Incorrect symbol {offendingSymbol.text}")
        else:
            raise SyntaxError(f"Error at line: {line}. Error message: {msg}")


def main():

    with open("test.mithon", "r") as file:
        lines = file.readlines()

    input_stream = FileStream("test.mithon")
    lexer = MithonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MithonParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    try:
        tree = parser.program()
    except Exception as e:
        print(e)
        exit(1)

    visitor = MithonVisitor(lines)

    try:
        visitor.visit(tree)
    except MithonError as me:
        print(me)
        exit(1)

if __name__ == '__main__':
    main()