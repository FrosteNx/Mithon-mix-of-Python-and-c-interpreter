# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

class MithonError(Exception):

    def __init__(self, message, line_number, column_number, line_content, error_type, context):
        self.message = message
        self.line_number = line_number
        self.column_number = column_number
        self.line_content = line_content.strip('\n')
        self.error_type = error_type
        self.ctx = context

class MithonVisitor(ParseTreeVisitor):

    def __init__(self, lines, funcTree):
        self.scopes = [{}]
        self.loop_depth = 0
        self.lines = lines
        self.errors = []
        self.function_tree = funcTree
        self.function_scope_stack = [("main", ())]

        super().__init__()

    
    def does_function_exist(self, scope_node, declaration):

        for child in scope_node.children:
            if child.declaration == declaration:
                self.function_scope_stack.append(declaration)
                return child
        
        if scope_node.parent:
            if scope_node.declaration in self.function_scope_stack:
                self.function_scope_stack.remove(scope_node.declaration)
            return self.does_function_exist(scope_node.parent, declaration)
        
        return None


    def get_functionTree_node(self, declaration):

        def dfs(node):
            if not node:
                return None
                
            if node.declaration == declaration:
                return node
            
            for child in node.children:
                result = dfs(child)
                if result:
                    return result

            return None
        
        return dfs(self.function_tree)

    def pushScope(self):
        self.scopes.append({})


    def popScope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()


    def addVariable(self, name, var_type, value, modifier={"const":False}):
        self.scopes[-1][name] = (var_type, value, modifier)


    def lookupVariable(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(f"variable {name} not defined")


    def updateVariable(self, name, value):

        for scope in reversed(self.scopes):
            if name in scope:
                if scope[name][-1]["const"]:
                    raise TypeError("cannot modify const variable")
                var_type = scope[name][0]  
                modifier = scope[name][-1]
                scope[name] = (var_type, value, modifier) 
                return
            
        raise Exception(f"variable {name} not defined")


    def is_variable(self, name):
        return any(name in scope for scope in self.scopes)


    def visitProgram(self, ctx:MithonParser.ProgramContext):

        for statement in ctx.statement():
            if not statement.functionDeclaration():
                self.visit(statement)
            

    def visitStatement(self, ctx:MithonParser.StatementContext):

        line = ctx.start.line
        column = ctx.start.column
        line_content = self.lines[line - 1]

        try:
            if ctx.varDeclaration():
                return self.visitVarDeclaration(ctx.varDeclaration())
            elif ctx.constDeclaration():
                return self.visitConstDeclaration(ctx.constDeclaration())
            elif ctx.printFunction():
                return self.visitPrintFunction(ctx.printFunction())
            elif ctx.returnStatement():
                return self.visitReturnStatement(ctx.returnStatement())
            elif ctx.ifStatement():
                return self.visitIfStatement(ctx.ifStatement())
            elif ctx.forLoop():
                return self.visitForLoop(ctx.forLoop())
            elif ctx.whileLoop():
                return self.visitWhileLoop(ctx.whileLoop())
            elif ctx.expressionStatement():
                return self.visitExpressionStatement(ctx.expressionStatement())
            elif ctx.augAssignment():
                return self.visitAugAssignment(ctx.augAssignment())
            
        except Exception as e:
            self.errors.append(MithonError(e, line, column, line_content, type(e).__name__, self.function_scope_stack[-1][0]))
            if len(self.function_scope_stack) > 1:
                self.function_scope_stack.pop(-1)
            raise

    def visitAugAssignment(self, ctx: MithonParser.AugAssignmentContext):
        name_ctx = ctx.name()
        indices = []
        var_name = name_ctx.IDENTIFIER().getText()

        for expr_ctx in name_ctx.expression():
            indices.append(self.visit(expr_ctx))

        if indices:
            variable_values = self.lookupVariable(var_name)[1]
            for index in indices[:-1]:
                variable_values = variable_values[index]

            final_index = indices[-1]
            if final_index >= len(variable_values) or final_index < 0:
                raise IndexError("index out of range")

            left_value = variable_values[final_index]
        else:
            left_value_type = self.lookupVariable(var_name)[0]
            operator = ctx.getChild(1).getText()
            if left_value_type in ("List", "Matrix", "Array"):
                right = ctx.getChild(2)
                self.augAssignmentResultComplexTypes(var_name, right, operator)
                return

            left_value = self.lookupVariable(var_name)[1]

        operator = ctx.getChild(1).getText()
        right_value = self.visitExpression(ctx.getChild(2))

        if type(left_value) != type(right_value):
            raise TypeError(f"unsupported operand type(s) for {operator}: {type(left_value).__name__} and {type(right_value).__name__}")

        new_value = self.augAssignmentResult(operator, left_value, self.lookupVariable(var_name)[0], right_value)

        if indices:
            variable_values[final_index] = new_value
            self.updateVariable(var_name, self.lookupVariable(var_name)[1])
        else:
            self.updateVariable(var_name, new_value)

    def augAssignmentResult(self, operator, left_value, left_type, right_value):
        match operator:
            case "+=":
                return left_value + right_value
            case "-=":
                return left_value - right_value
            case "*=":
                return left_value * right_value
            case "/=":
                if right_value != 0:
                    if left_type == "int":
                        return int(left_value / right_value)
                    elif left_type == "float":
                        return float(left_value / right_value)
                else:
                    raise ZeroDivisionError("division by zero")
            case "%=":
                if right_value != 0:
                    return left_value % right_value
                else:
                    raise ZeroDivisionError("integer modulo by zero")
                

    def augAssignmentResultComplexTypes(self, left, right, operator):
        l_t, l_values, l_modifier = self.lookupVariable(left)

        #print(left, right, operator)
        
        if operator in ("+=", "-="):
            if l_t in ("Matrix", "Array", "List"):
                right_expr_text = right.getText()
                right_value = self.visit(right)

                if l_t == "Matrix":
                    if isinstance(right_expr_text, str) and self.is_variable(right_expr_text):
                        r_t, r_values, r_modifier = self.lookupVariable(right_expr_text)

                        if r_t != "Matrix":
                            raise TypeError(f"Both operands must be Matrices. Right type: {r_t}")
                        if len(r_values) != len(l_values):
                            raise ValueError(f"Matrix lengths: {len(l_values)}, {len(r_values)} do not match")
                        if l_modifier["el_type"] != r_modifier["el_type"]:
                            raise TypeError(f"Matrix element types: {l_modifier['el_type']}, {r_modifier['el_type']} do not match")

                        if operator == '+=':
                            for i, el in enumerate(r_values):
                                l_values[i] += el
                        elif operator == '-=':
                            for i, el in enumerate(r_values):
                                l_values[i] -= el

                        self.updateVariable(left, l_values)
                        return l_values
                    else:
                        if type(right_value).__name__ != l_modifier["el_type"]:
                            raise TypeError(f"Matrix element types: {l_modifier['el_type']} and right value type: {type(right_value).__name__ } do not match")

                        if operator == '+=':
                            for i in range(len(l_values)):
                                l_values[i] += right_value
                        elif operator == '-=':
                            for i in range(len(l_values)):
                                l_values[i] -= right_value

                        self.updateVariable(left, l_values)
                        return l_values

                elif l_t in ("List", "Array"):
                    if operator == '-':
                        raise TypeError(f"Cannot subtract from a variable of type {l_t}")

                    if isinstance(right_value, str) and self.is_variable(right_value):
                        r_t, r_values, r_modifier = self.lookupVariable(right_value)

                        if l_t != r_t:
                            raise TypeError(f"Cannot add variables of types {l_t} and {r_t}")
                        if l_modifier["el_type"] != r_modifier["el_type"]:
                            raise TypeError("List element types do not match")

                        if l_t == "Array" and len(l_values) + len(r_values) > l_modifier['max_el_count']:
                            raise ValueError(f"Array size exceeds maximum of {l_modifier['max_el_count']}")

                        l_values += r_values
                        self.updateVariable(left, l_values)
                    elif isinstance(right_value, list):
                        if any(type(el).__name__ != l_modifier["el_type"] for el in right_value):
                            raise TypeError("List element types do not match")

                        if l_t == "Array" and len(l_values) + len(right_value) > l_modifier['max_el_count']:
                            raise ValueError(f"Array size exceeds maximum of {l_modifier['max_el_count']}")

                        l_values += right_value
                        self.updateVariable(left, l_values)
                    else:
                        raise TypeError("Cannot add non-list value to a List or Array")

                    return l_values
                
        elif operator in ("*=", "/=", "%="):
            if l_t in ("List", "Matrix", "Array"):
                l_t, l_values, l_modifier = self.lookupVariable(left)

                right_expr_text = right.getText()
                right_value = self.visit(right)

                if isinstance(right_expr_text, str) and self.is_variable(right_expr_text) and self.lookupVariable(right_expr_text)[0] == "Matrix":
                    r_t, r_values, r_modifier = self.lookupVariable(right_expr_text)

                    if len(r_values) != len(l_values):
                        raise ValueError("Matrix dimensions do not match")
                    if l_modifier["el_type"] != r_modifier["el_type"]:
                        raise TypeError("Matrix element types do not match")

                    if operator == '*=':
                        for i in range(len(l_values)):
                            l_values[i] *= r_values[i]
                    elif operator == '/=':
                        for i in range(len(l_values)):
                            if l_modifier["el_type"] == "int":
                                l_values[i] = int(l_values[i] / r_values[i])
                            elif l_modifier["el_type"] == "float":
                                l_values[i] = float(l_values[i] / r_values[i])

                    self.updateVariable(left, l_values)
                else:
                    if l_modifier["el_type"] != type(right_value).__name__:
                        raise TypeError("Matrix element types do not match")

                    if operator == '*=':
                        for i in range(len(l_values)):
                            l_values[i] *= right_value
                    elif operator == '/=':
                        for i in range(len(l_values)):
                            if l_modifier["el_type"] == "int":
                                l_values[i] = int(l_values[i] / right_value)
                            elif l_modifier["el_type"] == "float":
                                l_values[i] = float(l_values[i] / right_value)
                                
                    self.updateVariable(left, l_values)

            return l_values



    def visitStatement_list(self, ctx: MithonParser.Statement_listContext):
        return_value = None 
        
        for statement in ctx.statement():
            return_value = self.visit(statement)
            
            if return_value == 'break':
                return 'break'

            if return_value == 'continue':
                return 'continue'

            if return_value is not None:
                return return_value
        
        return return_value


    def visitPrintFunction(self, ctx:MithonParser.PrintFunctionContext):
        expressions = ctx.expressionList().expression()
        for expr in expressions:
            value = self.visit(expr)
            print(value, end=' ')
        print()


    def prepareVariable(self, ctx, modifiers=None):
        t = ctx.type_()
        ct = ctx.complexType()
        n = ctx.name()
        i = ctx.IDENTIFIER()
        e = ctx.expression()

        expression_result = None

        if t and i and e:
            modifiers = {"const": False}
            var_type = t.getText()
            var_name = i.getText()
            expression_result = self.visit(e)

            if self.is_variable(var_name):
                t, values, modifier = self.lookupVariable(var_name)
                raise NameError(f"cannot redeclare variable {var_name} of type {t}")

            if type(expression_result).__name__ != var_type:
                raise TypeError(f"initial value: {expression_result} with type: {type(expression_result).__name__} doesnt match declared type: {var_type} for variable {var_name}")

        elif ct and i and e:
            modifiers = {"const": False}

            var_declaration = ct.getText().split('[')
            var_type = var_declaration[0]

            el_max_count = 10e10

            match var_type:
                case "List" | "Matrix":
                    el_type = var_declaration[1][:-1]
                case "Array":
                    el_type = var_declaration[1][:-1].split(',')[1]
                    el_max_count = var_declaration[1][:-1].split(',')[0]

            var_name = i.getText()
            expression_result = self.visit(e)

            if not isinstance(expression_result, list):
                raise SyntaxError(f"invalid {var_type} declaration. Provided value has to be in [values] format")

            for i, exp in enumerate(expression_result):
                if type(exp).__name__ != el_type:
                    raise TypeError(f"invalid element type: {type(exp).__name__} for {var_type} with element type: {el_type}")

            modifiers["el_type"] = el_type
            modifiers["el_max_count"] = el_max_count

        elif n and e and not t:
            modifiers = {"const": False}

            if n.IDENTIFIER():
                var_name = n.getText()
                expression_result = self.visit(e)

                if not ct and isinstance(expression_result, list) and not self.is_variable(var_name):
                    raise SyntaxError("complexType has to be specified: List[type], Matrix[type], Array[int, type]")

                var_type = type(expression_result).__name__

                if self.is_variable(var_name):
                    self.updateVariable(var_name, expression_result)
                else:
                    self.addVariable(var_name, var_type, expression_result, modifiers)
                return

            elif n.listIndexation():
                var_name = n.listIndexation().IDENTIFIER().getText()
                var_type, variable_values, modifiers = self.lookupVariable(var_name)
                index = self.visit(n.listIndexation().expression())

                if index > len(variable_values):
                    raise IndexError("index out of range")

                new_value = self.visit(e)
                variable_values[index] = new_value
                self.updateVariable(var_name, variable_values)
                return

        elif (t or ct) and i and not e:
            var_type = t.getText() if t else ct.getText()
            var_name = i.getText()

            if modifiers:
                raise TypeError(f"cannot declare const variable {var_name} without providing initial value")

            if t:
                expression_result = {"int":0, "float":0.0, "str":"", "bool":False}[var_type]
                modifiers = {"const":False}
            elif ct:
                var_declaration = ct.getText().split('[')
                var_type = var_declaration[0]

                el_max_count = 10e10

                match var_type:
                    case "List" | "Matrix":
                        el_type = var_declaration[1][:-1]
                    case "Array":
                        el_type = var_declaration[1][:-1].split(',')[1]
                        el_max_count = var_declaration[1][:-1].split(',')[0]

                expression_result = []

                modifiers = {"const":False, "el_type":el_type, "el_max_count":el_max_count}

            if self.is_variable(var_name):
                t, values, modifier = self.lookupVariable(var_name)
                raise NameError(f"cannot redeclare variable {var_name} of type {t}")

        else:
            raise SyntaxError("invalid variable declaration. Must include a type or initialization")

        if var_name:
            self.addVariable(var_name, var_type, expression_result, modifiers)
        else:
            raise SyntaxError("variable declaration error: Name required")
        
    def convert_to_numeric_type(self, var_type, value):
        try:
            if var_type == "int":
                return int(value)
            elif var_type == "float":
                return float(value)
        except ValueError:
            raise TypeError(f"Cannot convert {value} to {var_type}")

    def visitVarDeclaration(self, ctx:MithonParser.VarDeclarationContext):
        self.prepareVariable(ctx)


    def visitConstDeclaration(self, ctx:MithonParser.ConstDeclarationContext):

        self.prepareVariable(ctx.varDeclaration(), {"const" : True})


    def visitForLoop(self, ctx:MithonParser.ForLoopContext):
        self.loop_depth += 1

        if len(ctx.IDENTIFIER()) > 1:

            content_var_name = ctx.IDENTIFIER(1).getText()
            content_type, content_values, content_modifier = self.lookupVariable(content_var_name)
            content_inner_type = content_modifier["el_type"]

            loop_var_name = ctx.IDENTIFIER(0).getText()

            if ctx.type_() and ctx.type_()[0].getText() != content_inner_type:
                raise TypeError(f"provided type: {ctx.type_()[0].getText()} doesnt match with collection inner type: {content_inner_type}")

            loop_values = iter(content_values)

            init_value = next(loop_values, -1)

            self.addVariable(loop_var_name, content_inner_type, init_value)

            i = 0

            self.pushScope()

            while True:

                temp = self.lookupVariable(loop_var_name)[1]
                
                return_value = self.visit(ctx.statement_list())

                if return_value == 'break':
                    break

                if return_value == 'continue':
                    continue

                if return_value is not None:
                    self.popScope()
                    self.loop_depth -= 1 
                    return return_value

                if temp != self.lookupVariable(loop_var_name)[1]:
                    content_values[i] = self.lookupVariable(loop_var_name)[1]
                    self.updateVariable(content_var_name, content_values)    
                
                new_value = next(loop_values, "eof")
                if new_value != "eof":
                    self.updateVariable(loop_var_name, new_value)
                else:
                    break

                i += 1
            
            self.popScope()

        else:
            loop_var_name = ctx.IDENTIFIER(0).getText()

            init_expr = ctx.expression(0)
            init_value = self.visit(init_expr)
            self.addVariable(loop_var_name, type(init_value).__name__, init_value, {"const" : False})

            condition_expr = ctx.expression(1)
            condition = self.visit(condition_expr)
            
            self.pushScope()

            while condition:

                return_value = self.visit(ctx.statement_list())

                if return_value == 'break':
                    break

                if return_value == 'continue':
                    continue

                if return_value is not None:
                    self.popScope()
                    self.loop_depth -= 1 
                    return return_value

                increment_expr = ctx.expression(2)
                increment_value = self.visit(increment_expr)

                condition = self.visit(condition_expr)

            self.popScope()

        self.loop_depth -= 1 


    def visitWhileLoop(self, ctx: MithonParser.WhileLoopContext):
            self.loop_depth += 1
            condition = self.visit(ctx.expression())
            self.pushScope()

            while condition:
                return_value = self.visit(ctx.statement_list())

                if return_value == 'break':
                    break

                if return_value == 'continue':
                    continue

                if return_value is not None:
                    self.popScope()
                    self.loop_depth -= 1
                    return return_value

                condition = self.visit(ctx.expression())

            self.popScope()
            self.loop_depth -= 1


    def visitIfStatement(self, ctx:MithonParser.IfStatementContext):
        if_condition = self.visit(ctx.expression(0))
        
        if if_condition:
            self.pushScope()
            return_value = self.visit(ctx.statement_list(0))
            self.popScope()
            if return_value is not None:
                return return_value
        else:
            handled = False
            for i in range(1, len(ctx.expression())):
                expr = ctx.expression(i)
                result = self.visit(expr)
                if result:
                    self.pushScope()
                    return_value = self.visit(ctx.statement_list(i))
                    self.popScope()
                    if return_value is not None: 
                        return return_value
                    handled = True
                    break
            
            if not handled:
                else_index = len(ctx.expression()) 
                else_stmt_list = ctx.statement_list(else_index)
                
                if else_stmt_list is not None:
                    self.pushScope()
                    return_value = self.visit(else_stmt_list)
                    self.popScope()
                    if return_value is not None:
                        return return_value
                    
    '''
    def visitFunctionDeclaration(self, ctx: MithonParser.FunctionDeclarationContext):
        function_name = ctx.IDENTIFIER().getText()
        return_type_ctx = ctx.func_return_type() if ctx.func_return_type() else None
        parameter_list_ctx = ctx.parameterList(0) if ctx.parameterList() else None

        parameter_list, parameters_count = [], []
        if parameter_list_ctx:
            for i in range(len(parameter_list_ctx.IDENTIFIER())):
                parameter_list.append((parameter_list_ctx.type_()[i].getText(), parameter_list_ctx.IDENTIFIER()[i].getText()))
                parameters_count.append(parameter_list_ctx.type_()[i].getText())

        if tuple([function_name, tuple(parameters_count)]) in self.function_declarations:
            raise SyntaxError("cannot declare 2 functions with identic names")
        
        if self.is_variable(function_name):
            raise SyntaxError("cannot declare function with identic name as a variable")

        function_body = ctx.statement_list()

        return_type = return_type_ctx.getText() if return_type_ctx else None

        self.function_declarations[tuple([function_name, tuple(parameters_count)])] = {
            'return_type': return_type,
            'parameters': parameter_list,
            'body': function_body
        }
        
        if return_type != 'None' and not self.doesFunctionReturn(function_body):
            raise Exception(f"function '{function_name}' must return a value of type {return_type}")

    def doesFunctionReturn(self, ctx):
        for statement in ctx.statement():
            if 'return' in statement.getText():
                return True
        return False
    '''

    def visitParameterList(self, ctx:MithonParser.ParameterListContext):
        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx: MithonParser.FunctionCallContext):

        function_name = ctx.IDENTIFIER().getText()
        argument_list = ctx.argumentList() if ctx.argumentList() else []

        argument_count = []
        
        for i in range(len(argument_list.expression())):
            argument_count.append(self.get_type(argument_list.expression(i)))

        #print(argument_list.expression(0).getText())
        #print(argument_count)
        argument_count = tuple(argument_count)
        #print(argument_count)

        if function_name == 'len':
            if len(argument_list.expression()) != 1:
                raise TypeError(f"function 'len' expects 1 argument, but {len(argument_list.expression())} were provided")
            arg_value = self.visit(argument_list.expression(0))
            return self.handle_len_function(arg_value)
        
        elif function_name == 'append':
            if len(argument_list.expression()) != 2:
                raise TypeError(f"function 'append' expects 2 arguments, but {len(argument_list.expression())} were provided")
            
            var = argument_list.expression()[0].getText()

            if not self.is_variable(var):
                raise NameError("variable not defined")

            t, values, modifier = self.lookupVariable(var)

            if not isinstance(values, list):
                raise TypeError("cannot append to a non-complex type")
            
            if modifier["const"]:
                raise TypeError("cannot modify const variable")
            
            if len(values) + 1 > int(modifier["el_max_count"]):
                raise IndexError(f"maximum size: {modifier['el_max_count']} of {t} reached")

            new_value = self.visit(argument_list.expression()[1])

            if type(new_value).__name__ != modifier["el_type"]:
                raise TypeError(f"cannot append: {type(new_value).__name__} to {t} of type: {modifier['el_type']}")
            
            values.append(new_value)

            self.updateVariable(var, values)

            return None
            
        elif function_name == 'sum':
            if len(argument_list.expression()) != 1:
                raise TypeError(f"function 'sum' expects 1 argument, but {len(argument_list.expression())} were provided")
            arg_value = self.visit(argument_list.expression(0))
            return self.handle_sum_function(arg_value)

        elif function_name == 'max':
            if len(argument_list.expression()) != 1:
                raise TypeError(f"function 'max' expects 1 argument, but {len(argument_list.expression())} were provided")
            arg_value = self.visit(argument_list.expression(0))
            return self.handle_max_function(arg_value)

        elif function_name == 'min':
            if len(argument_list.expression()) != 1:
                raise TypeError(f"function 'min' expects 1 argument, but {len(argument_list.expression())} were provided")
            arg_value = self.visit(argument_list.expression(0))
            return self.handle_min_function(arg_value)
        

        elif function_name == 'reverse':
            if len(argument_list.expression()) != 1:
                raise TypeError(f"function 'reverse' expects 1 argument, but {len(argument_list.expression())} were provided")
            var = argument_list.expression(0).getText()
            self.handle_reverse_function(var)
            return

        elif function_name == 'remove':
            if len(argument_list.expression()) != 2:
                raise TypeError(f"function 'remove' expects 2 arguments, but {len(argument_list.expression())} were provided")
            list_name = argument_list.expression(0).getText()
            element = self.visit(argument_list.expression(1))
            return self.handle_remove_function(list_name, element)
        
        elif function_name == 'sort':
            if len(argument_list.expression()) < 1 or len(argument_list.expression()) > 2:
                raise TypeError(f"function 'sort' expects 1 or 2 arguments, but {len(argument_list.expression())} were provided")
            var = argument_list.expression(0).getText()
            order = self.visit(argument_list.expression(1)) if len(argument_list.expression()) == 2 else 'ascending'
            if isinstance(order, str):
                self.handle_sort_function(var, order)
            else:
                raise TypeError(f"order must be a string, but got {type(order).__name__}")
        
        elif function_name == 'sorted':
            if len(argument_list.expression()) < 1 or len(argument_list.expression()) > 2:
                raise TypeError(f"function 'sorted' expects 1 or 2 arguments, but {len(argument_list.expression())} were provided")
            var = argument_list.expression(0).getText()
            order = self.visit(argument_list.expression(1)) if len(argument_list.expression()) == 2 else 'ascending'
            if isinstance(order, str):
                return self.handle_sorted_function(var, order)
            else:
                raise TypeError(f"order must be a string, but got {type(order).__name__}")

        elif function_name == 'pop':
            if len(argument_list.expression()) != 1:
                raise TypeError(f"function 'pop' expects 1 argument, but {len(argument_list.expression())} were provided")
            var = argument_list.expression(0).getText()
            return self.handle_pop_function(var)
        
        elif function_name == 'mean':
            if len(argument_list.expression()) != 1:
                raise TypeError(f"function 'mean' expects 1 argument, but {len(argument_list.expression())} were provided")
            arg_value = self.visit(argument_list.expression(0))
            return self.handle_mean_function(arg_value)
        
        else:
            func_scope = self.function_scope_stack[-1]
            func_scope_node = self.get_functionTree_node(func_scope)
            
            #print(func_scope_node)
            temporary_func_scope_stack = self.function_scope_stack[::]
            func_node = self.does_function_exist(func_scope_node, (function_name, argument_count))

            if not func_node:
                self.function_scope_stack = temporary_func_scope_stack
                error_code = f"function: {function_name} with {len(argument_count)} argument(s)"
                if argument_count:
                    error_code += f" of type: {','.join(argument_count)}"
                error_code += " not defined"
                raise NameError(error_code)

            if (function_name, argument_count) not in self.function_scope_stack:
                self.function_scope_stack.append((function_name, argument_count))

            parameter_list = func_node.func_body["parameters"]
            function_body = func_node.func_body["body"]

            if (not argument_list and parameter_list) or (argument_list and len(argument_list.expression()) != len(parameter_list)):
                raise TypeError(f"Function '{function_name}' expects {len(parameter_list)} arguments, but {len(argument_list.expression())} were provided")

            if argument_list:
                argument_list = argument_list.expression()

            self.pushScope()

            #print(parameter_list, argument_list)

            for parameter, argument in zip(parameter_list, argument_list):
                arg_value = self.visit(argument)
                #if not self.match_type(parameter[0], arg_value):
                #    raise TypeError(f"Argument {parameter[1]} expected type: {parameter[0]}. Got: {self.get_type(arg_value)} instead.")
                self.addVariable(parameter[1], parameter[0], arg_value)

            return_value = self.visit(function_body)

            self.popScope()

            if (function_name, argument_count) in self.function_scope_stack:
                self.function_scope_stack.remove((function_name, argument_count))

            return return_value

        
    def get_type(self, argument):

        arg_text = argument.getText()
        #print(argument)
        if self.is_variable(arg_text):
            t, value, modifier = self.lookupVariable(arg_text)
            if t in ("List", "Matrix"):
                return t + '[' + modifier["el_type"] + ']'
            elif t == "Array":
                return t + '[' + modifier["el_max_count"] + "," + modifier["el_type"] + "]"
            else:
                return t
        else:
            arg_value = self.visit(argument)
            #print(arg_value)
            return type(arg_value).__name__

    def handle_len_function(self, arg):
        if isinstance(arg, (str, list)):
            return len(arg)
        else:
            raise TypeError(f"function 'len' is not applicable to type: {type(arg).__name__}")
        
    def handle_sum_function(self, arg):
        if isinstance(arg, list):
            return sum(arg)
        else:
            raise TypeError(f"function 'sum' is not applicable to type: {type(arg).__name__}")

    def handle_max_function(self, arg):
        if isinstance(arg, list):
            return max(arg)
        else:
            raise TypeError(f"function 'max' is not applicable to type: {type(arg).__name__}")

    def handle_min_function(self, arg):
        if isinstance(arg, list):
            return min(arg)
        else:
            raise TypeError(f"function 'min' is not applicable to type: {type(arg).__name__}")

    def handle_reverse_function(self, var):
        if not self.is_variable(var):
            raise NameError(f"Variable '{var}' is not defined")
        t, values, modifier = self.lookupVariable(var)
        if not isinstance(values, list):
            raise TypeError(f"function 'reverse' is not applicable to type: {type(values).__name__}")
        values.reverse()
        self.updateVariable(var, values)

    def handle_remove_function(self, list_name, element):
        if not self.is_variable(list_name):
            raise NameError(f"variable '{list_name}' is not defined")
        
        var_type, values, modifier = self.lookupVariable(list_name)

        if not isinstance(values, list):
            raise TypeError(f"function 'remove' is not applicable to type: {type(values).__name__}")

        if element not in values:
            raise ValueError(f"element '{element}' not found in list '{list_name}'")

        values.remove(element)
        self.updateVariable(list_name, values)
        
    def handle_sort_function(self, var, order='ascending'):
        if not self.is_variable(var):
            raise NameError(f"variable '{var}' is not defined")
        t, values, modifier = self.lookupVariable(var)
        if not isinstance(values, list):
            raise TypeError(f"function 'sort' is not applicable to type: {type(values).__name__}")
        if order == 'ascending':
            values.sort()
        elif order == 'descending':
            values.sort(reverse=True)
        else:
            raise ValueError(f"invalid order: {order}. Use 'ascending' or 'descending'.")
        self.updateVariable(var, values)

    def handle_sorted_function(self, var, order='ascending'):
        if not self.is_variable(var):
            raise NameError(f"variable '{var}' is not defined")
        t, values, modifier = self.lookupVariable(var)
        if not isinstance(values, list):
            raise TypeError(f"function 'sorted' is not applicable to type: {type(values).__name__}")
        if order == 'ascending':
            new_values = sorted(values)
        elif order == 'descending':
            new_values = sorted(values, reverse=True)
        else:
            raise ValueError(f"invalid order: {order}. Use 'ascending' or 'descending'.")
        return new_values

    def handle_pop_function(self, var):
        if not self.is_variable(var):
            raise NameError(f"Variable '{var}' is not defined")
        t, values, modifier = self.lookupVariable(var)
        if not isinstance(values, list):
            raise TypeError(f"function 'pop' is not applicable to type: {type(values).__name__}")
        if len(values) == 0:
            raise IndexError("pop from empty list")
        popped_value = values.pop()
        self.updateVariable(var, values)
        return popped_value
    
    def handle_mean_function(self, arg):
        if isinstance(arg, list) and all(isinstance(x, (int, float)) for x in arg):
            return sum(arg) / len(arg) if len(arg) > 0 else 0
        else:
            raise TypeError(f"function 'mean' is not applicable to type: {type(arg).__name__} or list contains non-numeric elements")

    def visitReturnStatement(self, ctx: MithonParser.ReturnStatementContext):
        return_value = self.visit(ctx.expression())
        return return_value


    def visitArgumentList(self, ctx:MithonParser.ArgumentListContext):
        return self.visitChildren(ctx)


    def visitExpressionList(self, ctx:MithonParser.ExpressionListContext):
        return self.visitChildren(ctx)


    def visitExpressionStatement(self, ctx:MithonParser.ExpressionStatementContext):
        return self.visit(ctx.expression())


    def visitExpression(self, ctx:MithonParser.ExpressionContext):
        if ctx.logicalOrExpression():
            return self.visitLogicalOrExpression(ctx.logicalOrExpression())
        elif ctx.augAssignment():
            return self.visitAugAssignment(ctx.augAssignment())


    def visitLogicalOrExpression(self, ctx:MithonParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) > 1:
            result = False
            for expr in ctx.logicalAndExpression():
                result = result or self.visit(expr)
            return result
        else:
            return self.visit(ctx.logicalAndExpression(0))


    def visitLogicalAndExpression(self, ctx:MithonParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) > 1:
            result = True
            for expr in ctx.equalityExpression():
                result = result and self.visit(expr)
            return result
        else:
            return self.visit(ctx.equalityExpression(0))


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


    def visitRelationalExpression(self, ctx:MithonParser.RelationalExpressionContext):
        left = self.visitAdditiveExpression(ctx.additiveExpression(0))

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


    def visitAdditiveExpression(self, ctx: MithonParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        operator = ctx.getChild(1).getText()
        left_expr = ctx.getChild(0)
        left_expr_text = left_expr.getText()
        left_value = self.visit(left_expr)

        #print(left_expr_text, left_value, operator)

        # Check if the left operand is a variable and retrieve its value
        if self.is_variable(left_expr_text) and self.lookupVariable(left_expr_text)[0] in ("Matrix", "Array", "List"):
            l_t, l_val, l_modifier = self.lookupVariable(left_expr_text)

            #print(l_t, l_val, l_modifier)
            
            if l_t in ("Matrix", "Array", "List"):
                l_values = l_val.copy()
                right_expr = ctx.getChild(2)
                right_expr_text = right_expr.getText()
                right_value = self.visit(right_expr)

                if l_t == "Matrix":
                    if isinstance(right_expr_text, str) and self.is_variable(right_expr_text):
                        r_t, r_values, r_modifier = self.lookupVariable(right_expr_text)

                        if r_t != "Matrix":
                            raise TypeError(f"Both operands must be Matrices. Right type: {r_t}")
                        if len(r_values) != len(l_values):
                            raise ValueError(f"Matrix lengths: {len(l_values)}, {len(r_values)} do not match")
                        if l_modifier["el_type"] != r_modifier["el_type"]:
                            raise TypeError(f"Matrix element types: {l_modifier['el_type']}, {r_modifier['el_type']} do not match")

                        if operator == '+':
                            for i, el in enumerate(r_values):
                                l_values[i] += el
                        elif operator == '-':
                            for i, el in enumerate(r_values):
                                l_values[i] -= el

                        #self.updateVariable(left_expr_text, l_values)
                        return l_values
                    else:
                        if type(right_value).__name__ != l_modifier["el_type"]:
                            raise TypeError(f"Matrix element types: {l_modifier['el_type']} and right value type: {type(right_value).__name__ } do not match")

                        if operator == '+':
                            for i in range(len(l_values)):
                                l_values[i] += right_value
                        elif operator == '-':
                            for i in range(len(l_values)):
                                l_values[i] -= right_value

                        #self.updateVariable(left_expr_text, l_values)
                        return l_values

                elif l_t in ("List", "Array"):
                    if operator == '-':
                        raise TypeError(f"Cannot subtract from a variable of type {l_t}")

                    if isinstance(right_value, str) and self.is_variable(right_value):
                        r_t, r_values, r_modifier = self.lookupVariable(right_value)

                        if l_t != r_t:
                            raise TypeError(f"Cannot add variables of types {l_t} and {r_t}")
                        if l_modifier["el_type"] != r_modifier["el_type"]:
                            raise TypeError("List element types do not match")

                        if l_t == "Array" and len(l_values) + len(r_values) > l_modifier['max_el_count']:
                            raise ValueError(f"Array size exceeds maximum of {l_modifier['max_el_count']}")

                        l_values += r_values
                        #self.updateVariable(left_value, l_values)
                    elif isinstance(right_value, list):
                        if any(type(el).__name__ != l_modifier["el_type"] for el in right_value):
                            raise TypeError("List element types do not match")

                        if l_t == "Array" and len(l_values) + len(right_value) > l_modifier['max_el_count']:
                            raise ValueError(f"Array size exceeds maximum of {l_modifier['max_el_count']}")

                        l_values += right_value
                        #self.updateVariable(left_value, l_values)
                    else:
                        raise TypeError("Cannot add non-list value to a List or Array")

                    return l_values
                
            else:
                right_value = self.visit(ctx.getChild(2))

                if operator == '+':
                    return left_value + right_value
                elif operator == '-':
                    return left_value - right_value

        else:
            right_value = self.visit(ctx.getChild(2))
            if operator in ('+', '-'):
                
                if type(left_value) != type(right_value):
                    raise TypeError(f"Cannot add/subtract values of types {type(left_value).__name__} and {type(right_value).__name__}")

                if operator == '+':
                    return left_value + right_value
                elif operator == '-':
                    return left_value - right_value

        raise NameError(f"Unsupported operator: {operator}")
        

    def visitMultiplicativeExpression(self, ctx: MithonParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        left_expr = ctx.getChild(0)
        left_expr_text = left_expr.getText()
        left_value = self.visit(left_expr)

        if isinstance(left_expr_text, str) and self.is_variable(left_expr_text) and self.lookupVariable(left_expr_text)[0] == "Matrix":
            l_t, l_val, l_modifier = self.lookupVariable(left_expr_text)
            l_values = l_val.copy()

            for i in range(1, len(ctx.unaryExpression())):
                operator = ctx.getChild(2 * i - 1).getText()
                right_expr = ctx.unaryExpression(i)
                right_expr_text = right_expr.getText()
                right_value = self.visit(right_expr)

                if isinstance(right_expr_text, str) and self.is_variable(right_expr_text) and self.lookupVariable(right_expr_text)[0] == "Matrix":
                    r_t, r_values, r_modifier = self.lookupVariable(right_expr_text)

                    if len(r_values) != len(l_values):
                        raise ValueError("Matrix dimensions do not match")
                    if l_modifier["el_type"] != r_modifier["el_type"]:
                        raise TypeError("Matrix element types do not match")

                    if operator == '*':
                        for i in range(len(l_values)):
                            l_values[i] *= r_values[i]
                    elif operator == '/':
                        for i in range(len(l_values)):
                            l_values[i] /= r_values[i]

                    #self.updateVariable(left_expr_text, l_values)
                else:
                    if l_modifier["el_type"] != type(right_value).__name__:
                        raise TypeError("Matrix element types do not match")

                    if operator == '*':
                        for i in range(len(l_values)):
                            l_values[i] *= right_value
                    elif operator == '/':
                        for i in range(len(l_values)):
                            l_values[i] /= right_value

                    #self.updateVariable(left_expr_text, l_values)

            return l_values
        else:
            left_value = self.visitUnaryExpression(ctx.unaryExpression(0))
            result = left_value

            for i in range(1, len(ctx.unaryExpression())):
                operator = ctx.getChild(2 * i - 1).getText()
                right_value = self.visitUnaryExpression(ctx.unaryExpression(i))

                if type(left_value) != type(right_value):
                    raise TypeError(f"Cannot multiply/divide values of types {type(left_value).__name__} and {type(right_value).__name__}")

                if operator == '*':
                    result *= right_value
                elif operator == '/':
                    if right_value != 0:
                        result /= right_value
                    else:
                        raise ZeroDivisionError("Division by zero")
                elif operator == '%':
                    if right_value != 0:
                        result %= right_value
                    else:
                        raise ZeroDivisionError("Modulo by zero")

            return result


    def visitUnaryExpression(self, ctx:MithonParser.UnaryExpressionContext):
        if ctx.typeConversion():
            return self.visitTypeConversion(ctx.typeConversion())
        elif ctx.getChildCount() == 1:
            return self.visitPrimaryExpression(ctx.primaryExpression())
        elif ctx.getChild(0).getText() == 'not':
            operand = self.visitPrimaryExpression(ctx.primaryExpression())
            return not operand
        elif ctx.getChild(0).getText() == '-':
            operand = self.visitPrimaryExpression(ctx.primaryExpression())
            return -operand
        return None
    

    def visitTypeConversion(self, ctx):
        target_type = ctx.type_().getText()
        expression_value = self.visit(ctx.expression())

        if target_type == 'int':
            return int(expression_value)
        elif target_type == 'float':
            return float(expression_value)
        elif target_type == 'bool':
            return bool(expression_value)
        elif target_type == 'str':
            return str(expression_value)
        else:
            raise ValueError(f"Unsupported type conversion: {target_type}")


    def visitPrimaryExpression(self, ctx:MithonParser.PrimaryExpressionContext):
        #print(ctx.getText())
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
        elif ctx.name():
            return self.visitName(ctx.name())
        elif ctx.list_():
            return [self.visitExpression(exp) for exp in ctx.list_().expressionList().expression()]
        elif ctx.getText() == 'break':
            if self.loop_depth > 0:
                return 'break'
            else:
                raise SyntaxError("'break' is only allowed within a loop")
        elif ctx.getText() == 'continue':
            if self.loop_depth > 0:
                return 'continue'
            else:
                raise SyntaxError("'continue' is only allowed within a loop")
        elif ctx.expression():
            return self.visit(ctx.expression()) 
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        else:
            return self.visitChildren(ctx)
        
    def visitName(self, ctx:MithonParser.NameContext):
        var_name = ctx.IDENTIFIER().getText()
        var_info = self.lookupVariable(var_name)
        if var_info is None:
            raise NameError(f"Variable '{var_name}' is not defined or has no value")

        var_type, var_value, modifier = var_info

        if ctx.expression():
            for index_ctx in ctx.expression():
                index = self.visit(index_ctx)
                if not isinstance(var_value, (list, str)):
                    raise TypeError("Invalid type for indexation")
                if index >= len(var_value) or index < 0:
                    raise IndexError(f"Index {index} out of range for length {len(var_value)}")
                var_value = var_value[index]

        return var_value


del MithonParser