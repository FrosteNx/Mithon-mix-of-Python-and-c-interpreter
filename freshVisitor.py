from antlr4 import *
from freshParser import freshParser

class freshVisitor(ParseTreeVisitor):

    def __init__(self):
        super().__init__()
        self.scopes = [{}]  # Symbol table to keep track of variable scopes

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

    def visitProgram(self, ctx:freshParser.ProgramContext):
        # Visit the main function first
        self.visitMain_function(ctx.main_function())
        # Visit each function in the program
        for function_ctx in ctx.function_list():
            self.visitFunction(function_ctx)

    def visitFunction(self, ctx:freshParser.FunctionContext):
        # Get function name and return type
        function_name = ctx.NAME().getText()
        return_type = ctx.type_().getText()
        
        self.pushScope()
        self.visitStatements(ctx.statements())
        self.popScope()

    def visitMain_function(self, ctx:freshParser.Main_functionContext):
        self.pushScope()
        self.visitStatements(ctx.statements())
        self.popScope() 

    def visitFunction_call(self, ctx:freshParser.Function_callContext):
        function_name = ctx.NAME().getText()

        if function_name not in self.scopes[0]:
            raise NameError(f"Function '{function_name}' is not defined")
        
        function_ctx = self.scopes[0][function_name]
        self.visit(function_ctx)

    def visitStatements(self, ctx:freshParser.StatementsContext):
        for statement_ctx in ctx.statement():
            self.visit(statement_ctx)

    def visitStatement(self, ctx:freshParser.StatementContext):
        return self.visitChildren(ctx)

    def visitVar_declaration(self, ctx:freshParser.Var_declarationContext):
        name = ctx.NAME().getText()
        var_type = ctx.type_().getText()
        value = self.visit(ctx.expression()) if ctx.expression() else None
        self.addVariable(name, var_type, value)

    def visitIf_statement(self, ctx:freshParser.If_statementContext):
        if_condition = self.visit(ctx.expression())
        if if_condition:
            self.visit(ctx.statements())

    def visitFor_loop_declaration(self, ctx:freshParser.For_loop_declarationContext):
        name = ctx.NAME().getText()
        var_type = ctx.type_().getText()
        value = self.visit(ctx.expression()) if ctx.expression() else None
        self.addVariable(name, var_type, value)

    def visitFor_loop_statement(self, ctx:freshParser.For_loop_statementContext):
        if ctx.for_loop_declaration():  # Variant 1: iterating over a range
            self.pushScope()
            start = self.visitFor_loop_declaration(ctx.for_loop_declaration())
            var_name = ctx.for_loop_declaration().NAME().getText()
            end = self.visit(ctx.expression(1))
            step = self.visit(ctx.expression(2))

            print(start, var_name, end, step)

            for i in range(start, end, step):
                self.scopes[-1][var_name]['value'] = i
                self.visitStatements(ctx.statements())
            
        else:  # Variant 2: iterating over elements in a collection
            var_type = ctx.type().getText()
            var_name = ctx.NAME().getText()
            collection_name = ctx.NAME(1).getText()
            
            self.pushScope()  # Push a new scope for the loop
            
            # Get the collection from the symbol table
            if collection_name in self.symbol_table[-1]:
                collection = self.symbol_table[-1][collection_name]['value']
            else:
                raise NameError(f"Collection '{collection_name}' is not defined")
            
            # Loop over elements in the collection
            for item in collection:
                self.symbol_table[-1][var_name] = {'type': var_type, 'value': item}
                self.visitStatements(ctx.statements())
            
        self.popScope()  # Pop the scope for the loop

    def visitPrint(self, ctx:freshParser.PrintContext):
        expressions = ctx.expression_list().expression()
        for expr in expressions:
            value = self.visit(expr)
            print(value, end=' ')
        print()

    def visitArgument_list(self, ctx:freshParser.Argument_listContext):
        return self.visitChildren(ctx)

    def visitArgument(self, ctx:freshParser.ArgumentContext):
        return self.visitChildren(ctx)

    def visitExpression_list(self, ctx:freshParser.Expression_listContext):
        return [self.visit(expression) for expression in ctx.expression()]

    def visitExpression(self, ctx:freshParser.ExpressionContext):
        return self.visit(ctx.or_expression())

    def visitOr_expression(self, ctx:freshParser.Or_expressionContext):
        left = self.visit(ctx.and_expression(0))
        for i in range(1, len(ctx.and_expression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.and_expression(i))
            if operator == 'or':
                left = left or right
        return left

    def visitAnd_expression(self, ctx:freshParser.And_expressionContext):
        left = self.visit(ctx.eq_expression(0))
        for i in range(1, len(ctx.eq_expression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.eq_expression(i))
            if operator == 'and':
                left = left and right
        return left

    def visitEq_expression(self, ctx:freshParser.Eq_expressionContext):
        left = self.visit(ctx.rel_expression(0))
        for i in range(1, len(ctx.rel_expression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.rel_expression(i))
            if operator == '==':
                left = left == right
            elif operator == '!=':
                left = left != right
        return left

    def visitRel_expression(self, ctx:freshParser.Rel_expressionContext):
        left = self.visit(ctx.add_expression(0))
        for i in range(1, len(ctx.add_expression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.add_expression(i))
            if operator == '<':
                left = left < right
            elif operator == '<=':
                left = left <= right
            elif operator == '>':
                left = left > right
            elif operator == '>=':
                left = left >= right
        return left

    def visitAdd_expression(self, ctx:freshParser.Add_expressionContext):
        left = self.visit(ctx.mul_expression(0))
        for i in range(1, len(ctx.mul_expression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.mul_expression(i))
            if operator == '+':
                left += right
            elif operator == '-':
                left -= right
        return left

    def visitMul_expression(self, ctx:freshParser.Mul_expressionContext):
        left = self.visit(ctx.un_expression(0))
        for i in range(1, len(ctx.un_expression())):
            operator = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.un_expression(i))
            if operator == '*':
                left *= right
            elif operator == '/':
                left /= right
        return left

    def visitUn_expression(self, ctx:freshParser.Un_expressionContext):
        if ctx.getChild(0).getText() == '-':
            return -self.visit(ctx.un_expression())
        elif ctx.getChild(0).getText() == 'not':
            return not self.visit(ctx.un_expression())
        else:
            return self.visit(ctx.basic_expression())

    def visitBasic_expression(self, ctx:freshParser.Basic_expressionContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.DOUBLE():
            return float(ctx.DOUBLE().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove quotes from string
        elif ctx.BOOL():
            return True if ctx.BOOL().getText() == 'true' else False
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.var_reference():
            return self.visit(ctx.var_reference())
        elif ctx.compound_assignment():
            return self.visit(ctx.compound_assignment())

    def visitCompound_assignment(self, ctx:freshParser.Compound_assignmentContext):
        var_name = ctx.var_reference().getText()
        operator = ctx.getChild(1).getText()
        value = self.visit(ctx.expression())
        if var_name in self.symbol_table[-1]:
            if operator == '+=':
                self.symbol_table[-1][var_name]['value'] += value
            elif operator == '-=':
                self.symbol_table[-1][var_name]['value'] -= value
            elif operator == '*=':
                self.symbol_table[-1][var_name]['value'] *= value
            elif operator == '/=':
                self.symbol_table[-1][var_name]['value'] /= value
            return self.symbol_table[-1][var_name]['value']
        else:
            raise NameError(f"Variable '{var_name}' is not defined")

    def visitPostfix_expression(self, ctx:freshParser.Postfix_expressionContext):
        value = self.visit(ctx.basic_expression())
        if ctx.getChildCount() == 2:
            operator = ctx.getChild(1).getText()
            if operator == '++':
                value += 1
            elif operator == '--':
                value -= 1
        return value

    def visitVar_reference(self, ctx:freshParser.Var_referenceContext):
        var_name = ctx.getText()
        for scope in reversed(self.scopes):
            if var_name in scope:
                return scope[var_name]['value']
        raise NameError(f"Variable '{var_name}' is not defined")

    def visitType(self, ctx:freshParser.TypeContext):
        return ctx.getText()
