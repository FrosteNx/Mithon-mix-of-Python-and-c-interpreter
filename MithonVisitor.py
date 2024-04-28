# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

# This class defines a complete generic visitor for a parse tree produced by MithonParser.

class MithonVisitor(ParseTreeVisitor):

    def __init__(self):
        self.scopes = [{}]
        super().__init__()
        
    def pushScope(self):
        self.scopes.append({})

    def popScope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def addVariable(self, name, type, value):
        self.scopes[-1][name] = (type, value)

    def lookupVariable(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Undefined variable '{name}'")

    # self.visit(obiekt) -> self.visit[typ obiektu](context)

    def visitProgram(self, ctx:MithonParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx:MithonParser.StatementContext):
        if ctx.varDeclaration():
            self.visitVarDeclaration(ctx.varDeclaration())
        elif ctx.printFunction():
            self.visitPrintFunction(ctx.printFunction())

    # Visit a parse tree produced by MithonParser#statement_list.
    def visitStatement_list(self, ctx:MithonParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MithonParser#printFunction.
    def visitPrintFunction(self, ctx:MithonParser.PrintFunctionContext):
        expressions = ctx.expressionList().expression()
        for expr in expressions:
            value = self.visit(expr)
            print(value, end=' ')
        print()


    def visitVarDeclaration(self, ctx:MithonParser.VarDeclarationContext):
        var_name = None
        var_type = None
        expression_result = None

        if ctx.type_() and ctx.IDENTIFIER() and ctx.expression():
            var_type = ctx.type_().getText()
            var_name = ctx.IDENTIFIER().getText()
            expression_result = self.visit(ctx.expression())
        elif ctx.IDENTIFIER() and ctx.expression() and not ctx.type_():
            var_name = ctx.IDENTIFIER().getText()
            expression_result = self.visit(ctx.expression())
            var_type = type(expression_result).__name__  
        elif ctx.type_() and ctx.IDENTIFIER() and not ctx.expression():
            var_type = ctx.type_().getText()
            var_name = ctx.IDENTIFIER().getText()
            expression_result = None 
        else:
            raise Exception("Invalid variable declaration. Must include a type or initialization.")

        if var_name:
            self.addVariable(var_name, var_type, expression_result)
        else:
            raise Exception("Variable declaration error: Name required")


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
        self.pushScope() 
        self.popScope()  

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
        elif ctx.getChild(0).getText() == 'not':
            operand = self.visitPrimaryExpression(ctx.primaryExpression())
            return not operand
        elif ctx.getChild(0).getText() == '-':
            operand = self.visitPrimaryExpression(ctx.primaryExpression())
            return -operand
        return None


    # Visit a parse tree produced by MithonParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MithonParser.PrimaryExpressionContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.DOUBLE():
            return float(ctx.DOUBLE().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Usunięcie cudzysłowów
        elif ctx.getText() == 'true':
            return True
        elif ctx.getText() == 'false':
            return False
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            var_type, var_value = self.lookupVariable(var_name)
            return var_value
        elif ctx.expression():
            return self.visit(ctx.expression()) 
        else:
            return self.visitChildren(ctx)



del MithonParser