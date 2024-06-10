# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

# This class defines a complete listener for a parse tree produced by MithonParser.
class MithonListener(ParseTreeListener):

    def __init__(self):
        self.function_declarations = {}

    # Enter a parse tree produced by MithonParser#program.
    def enterProgram(self, ctx:MithonParser.ProgramContext):
        pass

    # Exit a parse tree produced by MithonParser#program.
    def exitProgram(self, ctx:MithonParser.ProgramContext):
        pass


    # Enter a parse tree produced by MithonParser#statement.
    def enterStatement(self, ctx:MithonParser.StatementContext):
        pass

    # Exit a parse tree produced by MithonParser#statement.
    def exitStatement(self, ctx:MithonParser.StatementContext):
        pass


    # Enter a parse tree produced by MithonParser#statement_list.
    def enterStatement_list(self, ctx:MithonParser.Statement_listContext):
        pass

    # Exit a parse tree produced by MithonParser#statement_list.
    def exitStatement_list(self, ctx:MithonParser.Statement_listContext):
        pass


    # Enter a parse tree produced by MithonParser#printFunction.
    def enterPrintFunction(self, ctx:MithonParser.PrintFunctionContext):
        pass

    # Exit a parse tree produced by MithonParser#printFunction.
    def exitPrintFunction(self, ctx:MithonParser.PrintFunctionContext):
        pass


    # Enter a parse tree produced by MithonParser#type.
    def enterType(self, ctx:MithonParser.TypeContext):
        pass

    # Exit a parse tree produced by MithonParser#type.
    def exitType(self, ctx:MithonParser.TypeContext):
        pass


    # Enter a parse tree produced by MithonParser#complexType.
    def enterComplexType(self, ctx:MithonParser.ComplexTypeContext):
        pass

    # Exit a parse tree produced by MithonParser#complexType.
    def exitComplexType(self, ctx:MithonParser.ComplexTypeContext):
        pass


    # Enter a parse tree produced by MithonParser#func_return_type.
    def enterFunc_return_type(self, ctx:MithonParser.Func_return_typeContext):
        pass

    # Exit a parse tree produced by MithonParser#func_return_type.
    def exitFunc_return_type(self, ctx:MithonParser.Func_return_typeContext):
        pass


    # Enter a parse tree produced by MithonParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MithonParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MithonParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MithonParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MithonParser#constDeclaration.
    def enterConstDeclaration(self, ctx:MithonParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by MithonParser#constDeclaration.
    def exitConstDeclaration(self, ctx:MithonParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by MithonParser#forLoop.
    def enterForLoop(self, ctx:MithonParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MithonParser#forLoop.
    def exitForLoop(self, ctx:MithonParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MithonParser#whileLoop.
    def enterWhileLoop(self, ctx:MithonParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by MithonParser#whileLoop.
    def exitWhileLoop(self, ctx:MithonParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by MithonParser#ifStatement.
    def enterIfStatement(self, ctx:MithonParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MithonParser#ifStatement.
    def exitIfStatement(self, ctx:MithonParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MithonParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):

        function_name = ctx.IDENTIFIER().getText()
        return_type_ctx = ctx.func_return_type() if ctx.func_return_type() else None
        parameter_list_ctx = ctx.parameterList(0) if ctx.parameterList() else None

        parameter_list, parameters_count = [], []
        if parameter_list_ctx:
            for i in range(len(parameter_list_ctx.IDENTIFIER())):
                parameter_list.append((parameter_list_ctx.type_()[i].getText(), parameter_list_ctx.IDENTIFIER()[i].getText()))
                parameters_count.append(parameter_list_ctx.type_()[i].getText())

        if tuple([function_name, tuple(parameters_count)]) in self.function_declarations:
            raise SyntaxError(f"cannot declare 2 functions with identic names: {function_name}({','.join(tuple(parameters_count))}) in scope")

        function_body = ctx.statement_list()

        return_type = return_type_ctx.getText() if return_type_ctx else None

        self.function_declarations[tuple([function_name, tuple(parameters_count)])] = {
            'return_type': return_type,
            'parameters': parameter_list,
            'body': function_body
        }
        
        if return_type != 'None' and not self.doesFunctionReturn(function_body):
            raise SyntaxError(f"function '{function_name}' must return a value of type {return_type}")
        
    def doesFunctionReturn(self, ctx):
        for statement in ctx.statement():
            if 'return' in statement.getText():
                return True
        return False

    # Exit a parse tree produced by MithonParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by MithonParser#parameterList.
    def enterParameterList(self, ctx:MithonParser.ParameterListContext):
        pass

    # Exit a parse tree produced by MithonParser#parameterList.
    def exitParameterList(self, ctx:MithonParser.ParameterListContext):
        pass


    # Enter a parse tree produced by MithonParser#functionCall.
    def enterFunctionCall(self, ctx:MithonParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MithonParser#functionCall.
    def exitFunctionCall(self, ctx:MithonParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MithonParser#argumentList.
    def enterArgumentList(self, ctx:MithonParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MithonParser#argumentList.
    def exitArgumentList(self, ctx:MithonParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by MithonParser#expressionList.
    def enterExpressionList(self, ctx:MithonParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MithonParser#expressionList.
    def exitExpressionList(self, ctx:MithonParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by MithonParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MithonParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MithonParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MithonParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MithonParser#returnStatement.
    def enterReturnStatement(self, ctx:MithonParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MithonParser#returnStatement.
    def exitReturnStatement(self, ctx:MithonParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MithonParser#expression.
    def enterExpression(self, ctx:MithonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#expression.
    def exitExpression(self, ctx:MithonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:MithonParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:MithonParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:MithonParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:MithonParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MithonParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MithonParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MithonParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MithonParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MithonParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MithonParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MithonParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MithonParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MithonParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MithonParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:MithonParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:MithonParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by MithonParser#list.
    def enterList(self, ctx:MithonParser.ListContext):
        pass

    # Exit a parse tree produced by MithonParser#list.
    def exitList(self, ctx:MithonParser.ListContext):
        pass


    # Enter a parse tree produced by MithonParser#name.
    def enterName(self, ctx:MithonParser.NameContext):
        pass

    # Exit a parse tree produced by MithonParser#name.
    def exitName(self, ctx:MithonParser.NameContext):
        pass


    # Enter a parse tree produced by MithonParser#listIndexation.
    def enterListIndexation(self, ctx:MithonParser.ListIndexationContext):
        pass

    # Exit a parse tree produced by MithonParser#listIndexation.
    def exitListIndexation(self, ctx:MithonParser.ListIndexationContext):
        pass


    # Enter a parse tree produced by MithonParser#augAssignment.
    def enterAugAssignment(self, ctx:MithonParser.AugAssignmentContext):
        pass

    # Exit a parse tree produced by MithonParser#augAssignment.
    def exitAugAssignment(self, ctx:MithonParser.AugAssignmentContext):
        pass



del MithonParser