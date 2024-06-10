# Generated from Mithon.g4 by ANTLR 4.13.1
from antlr4 import ParseTreeListener
from collections import defaultdict
from typing import Optional, List

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
        for child in self.children:
            if child.declaration == declaration:
                return True
        return False
    
    def __str__(self):

        s = f"Scope: {self.declaration}\n"
        if self.parent:
            s += f"Parent: {self.parent.declaration}\n"

        if self.declaration:
            s += str(self.declaration) + "\n"

        for child in self.children:
            s += str(child)

        return s

class MithonListener(ParseTreeListener):

    def __init__(self):
        self.declaration_tree = FunctionDeclarationNode(("main",()), None, [], 0, None)
        self.declaration_stack = [("main",())]

    def get_declarationTree_node(self, decl):

        def dfs(node):
            if not node:
                return None
                
            if node.declaration == decl:
                return node
            
            for child in node.children:
                return dfs(child)

            return None
        
        return dfs(self.declaration_tree)

    def enterFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):
    
        function_name = ctx.IDENTIFIER().getText()
        return_type_ctx = ctx.func_return_type() if ctx.func_return_type() else None
        parameter_list_ctx = ctx.parameterList(0) if ctx.parameterList() else None

        parameter_list, parameters_count = [], []
        if parameter_list_ctx:
            for i in range(len(parameter_list_ctx.IDENTIFIER())):
                parameter_list.append((parameter_list_ctx.type_()[i].getText(), parameter_list_ctx.IDENTIFIER()[i].getText()))
                parameters_count.append(parameter_list_ctx.type_()[i].getText())

        func_declaration = (function_name, tuple(parameters_count))

        func_scope_decl = self.declaration_stack[-1]

        parent_node = self.get_declarationTree_node(func_scope_decl)

        if self.does_function_exits(func_scope_decl, func_declaration):
            raise SyntaxError(f"cannot declare 2 functions with identic name: {function_name} and parameters: {','.join(parameters_count)} in one scope")
        
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
            raise Exception(f"function '{function_name}' must return a value of type {return_type}")
        
    def does_function_return(self, ctx):
        for statement in ctx.statement():
            if 'return' in statement.getText():
                return True
        return False
    
    def does_function_exits(self, scope, declaration):

        scope_node = self.get_declarationTree_node(scope)

        if any(declaration == child.declaration for child in scope_node.get_children()):
            return True
        
        return False

    # Exit a parse tree produced by MithonParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:MithonParser.FunctionDeclarationContext):
        self.declaration_stack.pop(-1)

del MithonParser