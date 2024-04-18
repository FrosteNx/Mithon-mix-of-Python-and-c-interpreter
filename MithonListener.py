# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

# This class defines a complete listener for a parse tree produced by MithonParser.
class MithonListener(ParseTreeListener):

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


    # Enter a parse tree produced by MithonParser#tempDeclaration.
    def enterTempDeclaration(self, ctx:MithonParser.TempDeclarationContext):
        pass

    # Exit a parse tree produced by MithonParser#tempDeclaration.
    def exitTempDeclaration(self, ctx:MithonParser.TempDeclarationContext):
        pass


    # Enter a parse tree produced by MithonParser#type.
    def enterType(self, ctx:MithonParser.TypeContext):
        pass

    # Exit a parse tree produced by MithonParser#type.
    def exitType(self, ctx:MithonParser.TypeContext):
        pass


    # Enter a parse tree produced by MithonParser#forLoop.
    def enterForLoop(self, ctx:MithonParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MithonParser#forLoop.
    def exitForLoop(self, ctx:MithonParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MithonParser#ifStatement.
    def enterIfStatement(self, ctx:MithonParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MithonParser#ifStatement.
    def exitIfStatement(self, ctx:MithonParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MithonParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):
        pass

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



del MithonParser