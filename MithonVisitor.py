# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

# This class defines a complete generic visitor for a parse tree produced by MithonParser.

class MithonVisitor(ParseTreeVisitor):

    # self.visit(obiekt) -> self.visit[typ obiektu](context)

    # Visit a parse tree produced by MithonParser#program.
    def visitProgram(self, ctx:MithonParser.ProgramContext):
        
        for statment in ctx.statement():
            self.visitStatement(statment)


    # Visit a parse tree produced by MithonParser#statement.
    def visitStatement(self, ctx:MithonParser.StatementContext):
        
        if ctx.printFunction():
            self.visit(ctx.printFunction())

    # Visit a parse tree produced by MithonParser#statement_list.
    def visitStatement_list(self, ctx:MithonParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#printFunction.
    def visitPrintFunction(self, ctx:MithonParser.PrintFunctionContext):
        text = self.visitExpression(ctx.expression())
        print(text)


    # Visit a parse tree produced by MithonParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MithonParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#constDeclaration.
    def visitConstDeclaration(self, ctx:MithonParser.ConstDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#tempDeclaration.
    def visitTempDeclaration(self, ctx:MithonParser.TempDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#type.
    def visitType(self, ctx:MithonParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#forLoop.
    def visitForLoop(self, ctx:MithonParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#ifStatement.
    def visitIfStatement(self, ctx:MithonParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#parameterList.
    def visitParameterList(self, ctx:MithonParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#functionCall.
    def visitFunctionCall(self, ctx:MithonParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#argumentList.
    def visitArgumentList(self, ctx:MithonParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#expressionList.
    def visitExpressionList(self, ctx:MithonParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MithonParser.ExpressionStatementContext):
        return self.visitExpression(ctx.expression())


    # Visit a parse tree produced by MithonParser#expression.
    def visitExpression(self, ctx:MithonParser.ExpressionContext):
        return self.visitLogicalOrExpression(ctx.logicalOrExpression())


    # Visit a parse tree produced by MithonParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:MithonParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) > 1:
            result = False
            for expr in ctx.logicalAndExpression():
                result = result or self.visit(expr)
            return result
        else:
            return self.visit(ctx.logicalAndExpression(0))

    # Visit a parse tree produced by MithonParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:MithonParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) > 1:
            result = True
            for expr in ctx.equalityExpression():
                result = result and self.visit(expr)
            return result
        else:
            return self.visit(ctx.equalityExpression(0))

    # Visit a parse tree produced by MithonParser#equalityExpression.
    def visitEqualityExpression(self, ctx:MithonParser.EqualityExpressionContext):
        left = self.visitRelationalExpression(ctx.relationalExpression(0))

        if len(ctx.relationalExpression()) > 1:
            operator = ctx.getChild(1).getText()
            right = self.visitRelationalExpression(ctx.relationalExpression(1))
            if operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
            
        return left


    # Visit a parse tree produced by MithonParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MithonParser.RelationalExpressionContext):
        left = self.visitAdditiveExpression(ctx.additiveExpression(0))

        # jeżeli wyrażenie składa się z więcej niż 1 dziecka, czyli w ogóle mamy operator to wchodzimy dalej
        if ctx.getChildCount() > 1:
            operator = ctx.getChild(1).getText()
            right = self.visitAdditiveExpression(ctx.additiveExpression(1))
            if operator == '<':
                return left < right
            elif operator == '>':
                return left > right
            elif operator == '<=':
                return left <= right
            elif operator == '>=':
                return left >= right
            
        return left

    # Visit a parse tree produced by MithonParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MithonParser.AdditiveExpressionContext):
        left = self.visitMultiplicativeExpression(ctx.multiplicativeExpression(0))
        result = left

        # drzewo rozkładu wstawia znak (+ / -) w co 2 wyraz stąd getChild(2*i - 1) 
        for i in range(1, len(ctx.multiplicativeExpression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visitMultiplicativeExpression(ctx.multiplicativeExpression(i))
            if operator == '+':
                result += right
            elif operator == '-':
                result -= right

        return result


    # Visit a parse tree produced by MithonParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MithonParser.MultiplicativeExpressionContext):
        left = self.visitUnaryExpression(ctx.unaryExpression(0))
        result = left
        for i in range(1, len(ctx.unaryExpression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visitUnaryExpression(ctx.unaryExpression(i))
            if operator == '*':
                result *= right
            elif operator == '/':
                if right != 0:
                    result /= right
                else:
                    raise ZeroDivisionError
        return result


    # Visit a parse tree produced by MithonParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MithonParser.UnaryExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visitPrimaryExpression(ctx.primaryExpression())
        else:
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.unaryExpression())
            if operator == 'not':
                return not operand
            elif operator == '-':
                return -operand
        return None


    # Visit a parse tree produced by MithonParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MithonParser.PrimaryExpressionContext):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Usunięcie cudzysłowów
        elif ctx.getText() == 'true':
            return True
        elif ctx.getText() == 'false':
            return False
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.expression():
            return self.visit(ctx.expression()) 
        else:
            return self.visitChildren(ctx)



del MithonParser

