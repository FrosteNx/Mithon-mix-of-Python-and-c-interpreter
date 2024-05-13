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
        self.scopes[-1][name] = (type, value)  # Store as a tuple

    def lookupVariable(self, name):
        # Check from the most recent scope to the outer scopes
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable {name} not defined")

    # self.visit(obiekt) -> self.visit[typ obiektu](context)

    def visitProgram(self, ctx:MithonParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx:MithonParser.StatementContext):
        if ctx.varDeclaration():
            self.visitVarDeclaration(ctx.varDeclaration())
        elif ctx.printFunction():
            self.visitPrintFunction(ctx.printFunction())
        elif ctx.ifStatement():
            self.visitIfStatement(ctx.ifStatement())
        elif ctx.forLoop():
            self.visitForLoop(ctx.forLoop())

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


    def visitForLoop(self, ctx:MithonParser.ForLoopContext):
        loop_var_name = ctx.IDENTIFIER(0).getText()

        init_expr = ctx.expression(0)
        init_value = self.visit(init_expr)
        self.addVariable(loop_var_name, type(init_value).__name__, init_value)

        condition_expr = ctx.expression(1)
        condition = self.visit(condition_expr)
        
        self.pushScope()

        while condition:
            self.visit(ctx.statement_list())

            increment_expr = ctx.expression(2)
            increment_value = self.visit(increment_expr)
            self.updateVariable(loop_var_name, increment_value)

            condition = self.visit(condition_expr)

        self.popScope()

        
    def updateVariable(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                var_type = scope[name][0]  
                scope[name] = (var_type, value) 
                return
        raise Exception(f"Variable {name} not defined")

    # Visit a parse tree produced by MithonParser#ifStatement.
    def visitIfStatement(self, ctx:MithonParser.IfStatementContext):
        if_condition = self.visit(ctx.expression(0))
        
        if if_condition:
            self.pushScope()
            self.visit(ctx.statement_list(0))
            self.popScope()
        else:
            handled = False
            for i in range(1, len(ctx.expression())):
                expr = ctx.expression(i)
                result = self.visit(expr)
                if result:
                    self.pushScope()
                    self.visit(ctx.statement_list(i))
                    self.popScope()
                    handled = True
                    break
            
            if not handled:
                else_index = len(ctx.expression()) 
                else_stmt_list = ctx.statement_list(else_index)
                
                if else_stmt_list is not None:
                    self.pushScope()
                    self.visit(else_stmt_list)
                    self.popScope()
                    
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
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = ctx.getChild(0).getText()  
        right = self.visit(ctx.getChild(2))  
        operator = ctx.getChild(1).getText() 

        if operator in ('+', '-'):
            left_value = self.visit(ctx.getChild(0)) 
            if operator == '+':
                return left_value + right
            elif operator == '-':
                return left_value - right
        elif operator == '+=':
            if not isinstance(left, str) or not self.is_variable(left):
                raise Exception(f"Left-hand side of '+=' must be a variable, got {left}")
            original_value = self.lookupVariable(left)
            new_value = original_value[1] + right
            self.updateVariable(left, new_value)
            return new_value
        elif operator == '-=':
            if not isinstance(left, str) or not self.is_variable(left):
                raise Exception(f"Left-hand side of '-=' must be a variable, got {left}")
            original_value = self.lookupVariable(left)
            new_value = original_value[1] - right
            self.updateVariable(left, new_value)
            return new_value
        else:
            raise Exception("Unsupported operator: " + operator)
        
    def is_variable(self, name):
        return any(name in scope for scope in self.scopes)

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
            var_info = self.lookupVariable(var_name)  
            if var_info is not None:
                var_type, var_value = var_info 
                return var_value
            else:
                raise Exception(f"Variable '{var_name}' is not defined or has no value.")
        elif ctx.expression():
            return self.visit(ctx.expression()) 
        else:
            return self.visitChildren(ctx)


del MithonParser