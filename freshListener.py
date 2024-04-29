# Generated from fresh.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .freshParser import freshParser
else:
    from freshParser import freshParser

# This class defines a complete listener for a parse tree produced by freshParser.
class freshListener(ParseTreeListener):

    # Enter a parse tree produced by freshParser#program.
    def enterProgram(self, ctx:freshParser.ProgramContext):
        pass

    # Exit a parse tree produced by freshParser#program.
    def exitProgram(self, ctx:freshParser.ProgramContext):
        pass


    # Enter a parse tree produced by freshParser#function_list.
    def enterFunction_list(self, ctx:freshParser.Function_listContext):
        pass

    # Exit a parse tree produced by freshParser#function_list.
    def exitFunction_list(self, ctx:freshParser.Function_listContext):
        pass


    # Enter a parse tree produced by freshParser#main_function.
    def enterMain_function(self, ctx:freshParser.Main_functionContext):
        pass

    # Exit a parse tree produced by freshParser#main_function.
    def exitMain_function(self, ctx:freshParser.Main_functionContext):
        pass


    # Enter a parse tree produced by freshParser#function.
    def enterFunction(self, ctx:freshParser.FunctionContext):
        pass

    # Exit a parse tree produced by freshParser#function.
    def exitFunction(self, ctx:freshParser.FunctionContext):
        pass


    # Enter a parse tree produced by freshParser#function_call.
    def enterFunction_call(self, ctx:freshParser.Function_callContext):
        pass

    # Exit a parse tree produced by freshParser#function_call.
    def exitFunction_call(self, ctx:freshParser.Function_callContext):
        pass


    # Enter a parse tree produced by freshParser#argument_list.
    def enterArgument_list(self, ctx:freshParser.Argument_listContext):
        pass

    # Exit a parse tree produced by freshParser#argument_list.
    def exitArgument_list(self, ctx:freshParser.Argument_listContext):
        pass


    # Enter a parse tree produced by freshParser#argument.
    def enterArgument(self, ctx:freshParser.ArgumentContext):
        pass

    # Exit a parse tree produced by freshParser#argument.
    def exitArgument(self, ctx:freshParser.ArgumentContext):
        pass


    # Enter a parse tree produced by freshParser#statements.
    def enterStatements(self, ctx:freshParser.StatementsContext):
        pass

    # Exit a parse tree produced by freshParser#statements.
    def exitStatements(self, ctx:freshParser.StatementsContext):
        pass


    # Enter a parse tree produced by freshParser#statement.
    def enterStatement(self, ctx:freshParser.StatementContext):
        pass

    # Exit a parse tree produced by freshParser#statement.
    def exitStatement(self, ctx:freshParser.StatementContext):
        pass


    # Enter a parse tree produced by freshParser#var_declaration.
    def enterVar_declaration(self, ctx:freshParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by freshParser#var_declaration.
    def exitVar_declaration(self, ctx:freshParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by freshParser#if_statement.
    def enterIf_statement(self, ctx:freshParser.If_statementContext):
        pass

    # Exit a parse tree produced by freshParser#if_statement.
    def exitIf_statement(self, ctx:freshParser.If_statementContext):
        pass


    # Enter a parse tree produced by freshParser#for_loop_statement.
    def enterFor_loop_statement(self, ctx:freshParser.For_loop_statementContext):
        pass

    # Exit a parse tree produced by freshParser#for_loop_statement.
    def exitFor_loop_statement(self, ctx:freshParser.For_loop_statementContext):
        pass


    # Enter a parse tree produced by freshParser#print.
    def enterPrint(self, ctx:freshParser.PrintContext):
        pass

    # Exit a parse tree produced by freshParser#print.
    def exitPrint(self, ctx:freshParser.PrintContext):
        pass


    # Enter a parse tree produced by freshParser#expression_list.
    def enterExpression_list(self, ctx:freshParser.Expression_listContext):
        pass

    # Exit a parse tree produced by freshParser#expression_list.
    def exitExpression_list(self, ctx:freshParser.Expression_listContext):
        pass


    # Enter a parse tree produced by freshParser#expression.
    def enterExpression(self, ctx:freshParser.ExpressionContext):
        pass

    # Exit a parse tree produced by freshParser#expression.
    def exitExpression(self, ctx:freshParser.ExpressionContext):
        pass


    # Enter a parse tree produced by freshParser#or_expression.
    def enterOr_expression(self, ctx:freshParser.Or_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#or_expression.
    def exitOr_expression(self, ctx:freshParser.Or_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#and_expression.
    def enterAnd_expression(self, ctx:freshParser.And_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#and_expression.
    def exitAnd_expression(self, ctx:freshParser.And_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#eq_expression.
    def enterEq_expression(self, ctx:freshParser.Eq_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#eq_expression.
    def exitEq_expression(self, ctx:freshParser.Eq_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#rel_expression.
    def enterRel_expression(self, ctx:freshParser.Rel_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#rel_expression.
    def exitRel_expression(self, ctx:freshParser.Rel_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#add_expression.
    def enterAdd_expression(self, ctx:freshParser.Add_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#add_expression.
    def exitAdd_expression(self, ctx:freshParser.Add_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#mul_expression.
    def enterMul_expression(self, ctx:freshParser.Mul_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#mul_expression.
    def exitMul_expression(self, ctx:freshParser.Mul_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#un_expression.
    def enterUn_expression(self, ctx:freshParser.Un_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#un_expression.
    def exitUn_expression(self, ctx:freshParser.Un_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#basic_expression.
    def enterBasic_expression(self, ctx:freshParser.Basic_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#basic_expression.
    def exitBasic_expression(self, ctx:freshParser.Basic_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#compound_assignment.
    def enterCompound_assignment(self, ctx:freshParser.Compound_assignmentContext):
        pass

    # Exit a parse tree produced by freshParser#compound_assignment.
    def exitCompound_assignment(self, ctx:freshParser.Compound_assignmentContext):
        pass


    # Enter a parse tree produced by freshParser#postfix_expression.
    def enterPostfix_expression(self, ctx:freshParser.Postfix_expressionContext):
        pass

    # Exit a parse tree produced by freshParser#postfix_expression.
    def exitPostfix_expression(self, ctx:freshParser.Postfix_expressionContext):
        pass


    # Enter a parse tree produced by freshParser#var_reference.
    def enterVar_reference(self, ctx:freshParser.Var_referenceContext):
        pass

    # Exit a parse tree produced by freshParser#var_reference.
    def exitVar_reference(self, ctx:freshParser.Var_referenceContext):
        pass


    # Enter a parse tree produced by freshParser#type.
    def enterType(self, ctx:freshParser.TypeContext):
        pass

    # Exit a parse tree produced by freshParser#type.
    def exitType(self, ctx:freshParser.TypeContext):
        pass



del freshParser