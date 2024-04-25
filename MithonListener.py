# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

# This class defines a complete listener for a parse tree produced by MithonParser.
class MithonListener(ParseTreeListener):

    def __init__(self):
        self.variables = {}

    @property
    def variables(self):
        return self._variables
    
    @variables.setter
    def variables(self, new_variables):
        self._variables = new_variables

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

        var_name = ctx.IDENTIFIER().getText()
        var_type = ctx.type_().getText() if ctx.type_() else None
        var_value = None
        if ctx.expression():
            var_value = self.exitExpression(ctx.expression())

        if var_type == 'int':
            if not isinstance(var_value, int):
                print(f"Warning: Assigned value is not an integer for variable '{var_name}'. It will be auto-casted to int.")
                var_value = int(var_value)
        elif var_type == 'double':
            if not isinstance(var_value, float):
                print(f"Warning: Assigned value is not a double for variable '{var_name}'")

        self.variables[var_name] = (var_type, var_value)
        
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
        return self.exitLogicalOrExpression(ctx.logicalOrExpression())


    # Enter a parse tree produced by MithonParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:MithonParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:MithonParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) > 1:
            result = False
            for expr in ctx.logicalAndExpression():
                result = result or self.exitLogicalAndExpression(expr)
            return result
        else:
            return self.exitLogicalAndExpression(ctx.logicalAndExpression(0))


    # Enter a parse tree produced by MithonParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:MithonParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:MithonParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) > 1:
            result = True
            for expr in ctx.equalityExpression():
                result = result and self.exitEqualityExpression(expr)
            return result
        else:
            return self.exitEqualityExpression(ctx.equalityExpression(0))


    # Enter a parse tree produced by MithonParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MithonParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MithonParser.EqualityExpressionContext):
        left = self.exitRelationalExpression(ctx.relationalExpression(0))

        if len(ctx.relationalExpression()) > 1:
            operator = ctx.getChild(1).getText()
            right = self.exitRelationalExpression(ctx.relationalExpression(1))
            if operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
            
        return left


    # Enter a parse tree produced by MithonParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MithonParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MithonParser.RelationalExpressionContext):

        left = self.exitAdditiveExpression(ctx.additiveExpression(0))

        if ctx.getChildCount() > 1:
            operator = ctx.getChild(1).getText()
            right = self.exitAdditiveExpression(ctx.additiveExpression(1))
            if operator == '<':
                return left < right
            elif operator == '>':
                return left > right
            elif operator == '<=':
                return left <= right
            elif operator == '>=':
                return left >= right
            
        return left

    # Enter a parse tree produced by MithonParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MithonParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MithonParser.AdditiveExpressionContext):
        left = self.exitMultiplicativeExpression(ctx.multiplicativeExpression(0))
        result = left

        for i in range(1, len(ctx.multiplicativeExpression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.exitMultiplicativeExpression(ctx.multiplicativeExpression(i))
            if operator == '+':
                result += right
            elif operator == '-':
                result -= right

        return result


    # Enter a parse tree produced by MithonParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MithonParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MithonParser.MultiplicativeExpressionContext):
        left = self.exitUnaryExpression(ctx.unaryExpression(0))
        result = left
        for i in range(1, len(ctx.unaryExpression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.exitUnaryExpression(ctx.unaryExpression(i))
            if operator == '*':
                result *= right
            elif operator == '/':
                if right != 0:
                    result /= right
                else:
                    raise ZeroDivisionError
        return result


    # Enter a parse tree produced by MithonParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MithonParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MithonParser.UnaryExpressionContext):
        if ctx.getChildCount() == 1:
            return self.exitPrimaryExpression(ctx.primaryExpression())
        elif ctx.getChild(0).getText() == 'not':
            operand = self.exitPrimaryExpression(ctx.primaryExpression())
            return not operand
        elif ctx.getChild(0).getText() == '-':
            operand = self.exitPrimaryExpression(ctx.primaryExpression())
            return -operand
        return None


    # Enter a parse tree produced by MithonParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:MithonParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by MithonParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:MithonParser.PrimaryExpressionContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.DOUBLE():
            return float(ctx.DOUBLE().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1] 
        elif ctx.getText() == 'true':
            return True
        elif ctx.getText() == 'false':
            return False
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                return self.variables[var_name][1]
            else:
                raise Exception(f"Undefined variable '{var_name}'")
        elif ctx.expression():
            return self.exitExpression(ctx.expression()) 
        else:
            return self.visitChildren(ctx)


del MithonParser