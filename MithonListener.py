# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import ParseTreeListener
from collections import defaultdict
from typing import Optional, List
from MithonVisitor import MithonError

if "." in __name__:
    from .MithonParser import MithonParser
else:
    from MithonParser import MithonParser

class FunctionDeclarationNode():
    def __init__(self, declaration, parent, children, depth, func_body):
        self.declaration = declaration
        self.parent = parent
        self.children = children
        self.depth = depth
        self.func_body = func_body

    def get_children(self):
        return self.children

    def get_declaration(self):
        return self.declaration
    
    def get_body(self):
        return self.func_body
    
    def does_function_exist(self, declaration):
        return any(child.declaration == declaration for child in self.children)
    
    def __str__(self):
        s = f"Scope: {self.declaration}\n"
        if self.parent:
            s += '\t' * self.depth + f"Parent: {self.parent.declaration}\n"
        for child in self.children:
            s += '\t' * child.depth + str(child)
        return s

class MithonListener(ParseTreeListener):
    def __init__(self, lines):
        self.declaration_tree = FunctionDeclarationNode(("main", ()), None, [], 0, None)
        self.declaration_stack = [("main", ())]
        self.lines = lines

    def get_declarationTree_node(self, decl):
        def dfs(node):
            if not node:
                return None
            if node.declaration == decl:
                return node
            for child in node.children:
                result = dfs(child)
                if result:
                    return result
            return None

        return dfs(self.declaration_tree)

    def enterFunctionDeclaration(self, ctx: MithonParser.FunctionDeclarationContext):
        line = ctx.start.line
        column = ctx.start.column
        line_content = self.lines[line - 1]

        function_name = ctx.IDENTIFIER().getText()
        return_type_ctx = ctx.func_return_type() if ctx.func_return_type() else None
        parameter_list_ctx = ctx.parameterList()

        parameter_list, parameters_count = [], []
        if parameter_list_ctx:
            for param in parameter_list_ctx:
                for i in range(0, len(param.children), 3):  # Adjust step based on actual grammar
                    param_type_ctx = param.getChild(i)
                    param_name_ctx = param.getChild(i + 1)
                    if isinstance(param_type_ctx, MithonParser.TypeContext) or isinstance(param_type_ctx, MithonParser.ComplexTypeContext):
                        param_type = param_type_ctx.getText()
                        param_name = param_name_ctx.getText()
                        parameter_list.append((param_type, param_name))
                        parameters_count.append(param_type)

        func_declaration = (function_name, tuple(parameters_count))

        func_scope_decl = self.declaration_stack[-1]

        parent_node = self.get_declarationTree_node(func_scope_decl)

        if self.does_function_exits(func_scope_decl, func_declaration):
            error_code = f"cannot declare 2 functions with identic name: {function_name} and {len(parameters_count)} parameter(s) "
            if parameters_count:
                error_code += f"{','.join(parameters_count)} "
            error_code += f"in one scope: {func_scope_decl}"
            raise MithonError(error_code, line, column, line_content, "SyntaxError", func_scope_decl)

        function_body = ctx.statement_list()

        return_type = return_type_ctx.getText() if return_type_ctx else None

        func = FunctionDeclarationNode(
            func_declaration,
            parent_node,
            [],
            parent_node.depth + 1,
            {
                'return_type': return_type,
                'parameters': parameter_list,
                'body': function_body
            }
        )

        parent_node.children.append(func)

        self.declaration_stack.append(func_declaration)

        if return_type != 'None' and not self.does_function_return(function_body):
            raise MithonError(f"function with return type: {return_type} doesnt return anything", line, column, line_content, "TypeError", func_scope_decl)
        
    def does_function_return(self, ctx):
        for statement in ctx.statement():
            if 'return' in statement.getText():
                return True
        return False
    
    def does_function_exits(self, scope, declaration):
        scope_node = self.get_declarationTree_node(scope)
        if scope_node.does_function_exist(declaration):
            return True
        return False

    def exitFunctionDeclaration(self, ctx: MithonParser.FunctionDeclarationContext):
        self.declaration_stack.pop(-1)