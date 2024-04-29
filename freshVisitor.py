# Generated from fresh.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .freshParser import freshParser
else:
    from freshParser import freshParser

# This class defines a complete generic visitor for a parse tree produced by freshParser.

class freshVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by freshParser#program.
    def visitProgram(self, ctx:freshParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#function_list.
    def visitFunction_list(self, ctx:freshParser.Function_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#main_function.
    def visitMain_function(self, ctx:freshParser.Main_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#function.
    def visitFunction(self, ctx:freshParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#function_call.
    def visitFunction_call(self, ctx:freshParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#argument_list.
    def visitArgument_list(self, ctx:freshParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#argument.
    def visitArgument(self, ctx:freshParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#statements.
    def visitStatements(self, ctx:freshParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#statement.
    def visitStatement(self, ctx:freshParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#var_declaration.
    def visitVar_declaration(self, ctx:freshParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#if_statement.
    def visitIf_statement(self, ctx:freshParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#for_loop_statement.
    def visitFor_loop_statement(self, ctx:freshParser.For_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#print.
    def visitPrint(self, ctx:freshParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#expression_list.
    def visitExpression_list(self, ctx:freshParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#expression.
    def visitExpression(self, ctx:freshParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#or_expression.
    def visitOr_expression(self, ctx:freshParser.Or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#and_expression.
    def visitAnd_expression(self, ctx:freshParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#eq_expression.
    def visitEq_expression(self, ctx:freshParser.Eq_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#rel_expression.
    def visitRel_expression(self, ctx:freshParser.Rel_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#add_expression.
    def visitAdd_expression(self, ctx:freshParser.Add_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#mul_expression.
    def visitMul_expression(self, ctx:freshParser.Mul_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#un_expression.
    def visitUn_expression(self, ctx:freshParser.Un_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#basic_expression.
    def visitBasic_expression(self, ctx:freshParser.Basic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#compound_assignment.
    def visitCompound_assignment(self, ctx:freshParser.Compound_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#postfix_expression.
    def visitPostfix_expression(self, ctx:freshParser.Postfix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#var_reference.
    def visitVar_reference(self, ctx:freshParser.Var_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by freshParser#type.
    def visitType(self, ctx:freshParser.TypeContext):
        return self.visitChildren(ctx)



del freshParser