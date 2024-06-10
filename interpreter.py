from antlr4 import FileStream, CommonTokenStream
from antlr4 import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from MithonLexer import MithonLexer
from MithonParser import MithonParser
from MithonListener import MithonListener
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

    input_file = "test.mithon"

    input_stream = FileStream(input_file)
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

    listener = MithonListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    visitor = MithonVisitor(lines, listener.declaration_tree)

    try:
        visitor.visit(tree)
    except Exception as e:
        print(f"Traceback (most recent call last):")
        for e in visitor.errors[::-1]:
            print(f"  File \"{input_file}\", line {e.line_number}, in <module>")
            print(f"    {e.line_content.lstrip()}")
            print(f"  {' ' * (e.column_number+1)}^")
        
        e = visitor.errors[0]
        print(f"{e.error_type}: {e.message}")

if __name__ == '__main__':
    main()