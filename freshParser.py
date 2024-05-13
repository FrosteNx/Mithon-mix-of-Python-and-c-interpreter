# Generated from fresh.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,3,0,58,8,0,1,0,1,0,3,0,62,8,0,1,0,1,0,1,1,4,1,67,8,
        1,11,1,12,1,68,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,3,3,85,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,95,8,3,1,4,
        1,4,1,4,1,4,1,4,5,4,102,8,4,10,4,12,4,105,9,4,3,4,107,8,4,1,4,1,
        4,1,4,1,5,1,5,1,5,5,5,115,8,5,10,5,12,5,118,9,5,1,6,1,6,1,6,1,7,
        1,7,3,7,125,8,7,4,7,127,8,7,11,7,12,7,128,1,8,1,8,1,8,1,8,1,8,3,
        8,136,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,156,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,173,8,10,10,10,12,10,
        176,9,10,1,10,1,10,1,10,1,10,1,10,3,10,183,8,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,208,8,11,1,12,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,224,8,
        14,10,14,12,14,227,9,14,1,15,1,15,1,16,1,16,1,16,5,16,234,8,16,10,
        16,12,16,237,9,16,1,17,1,17,1,17,5,17,242,8,17,10,17,12,17,245,9,
        17,1,18,1,18,1,18,5,18,250,8,18,10,18,12,18,253,9,18,1,19,1,19,1,
        19,5,19,258,8,19,10,19,12,19,261,9,19,1,20,1,20,1,20,5,20,266,8,
        20,10,20,12,20,269,9,20,1,21,1,21,1,21,5,21,274,8,21,10,21,12,21,
        277,9,21,1,22,1,22,1,22,3,22,282,8,22,1,22,1,22,3,22,286,8,22,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,299,8,
        23,1,24,1,24,1,24,1,24,1,25,1,25,3,25,307,8,25,1,26,1,26,1,27,1,
        27,1,27,0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,0,8,1,0,21,22,1,0,23,26,1,0,27,28,
        1,0,29,30,2,0,28,28,31,31,1,0,32,35,1,0,36,37,2,0,6,6,38,41,321,
        0,57,1,0,0,0,2,66,1,0,0,0,4,70,1,0,0,0,6,80,1,0,0,0,8,96,1,0,0,0,
        10,111,1,0,0,0,12,119,1,0,0,0,14,126,1,0,0,0,16,135,1,0,0,0,18,155,
        1,0,0,0,20,157,1,0,0,0,22,207,1,0,0,0,24,209,1,0,0,0,26,214,1,0,
        0,0,28,220,1,0,0,0,30,228,1,0,0,0,32,230,1,0,0,0,34,238,1,0,0,0,
        36,246,1,0,0,0,38,254,1,0,0,0,40,262,1,0,0,0,42,270,1,0,0,0,44,285,
        1,0,0,0,46,298,1,0,0,0,48,300,1,0,0,0,50,304,1,0,0,0,52,308,1,0,
        0,0,54,310,1,0,0,0,56,58,3,2,1,0,57,56,1,0,0,0,57,58,1,0,0,0,58,
        59,1,0,0,0,59,61,3,4,2,0,60,62,3,2,1,0,61,60,1,0,0,0,61,62,1,0,0,
        0,62,63,1,0,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,67,3,6,3,0,66,65,1,
        0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,
        71,5,1,0,0,71,72,5,2,0,0,72,73,5,3,0,0,73,74,5,4,0,0,74,75,5,5,0,
        0,75,76,5,6,0,0,76,77,5,7,0,0,77,78,3,14,7,0,78,79,5,8,0,0,79,5,
        1,0,0,0,80,81,5,1,0,0,81,82,5,42,0,0,82,84,5,3,0,0,83,85,3,10,5,
        0,84,83,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,4,0,0,87,88,
        5,5,0,0,88,94,3,54,27,0,89,95,5,9,0,0,90,91,5,7,0,0,91,92,3,14,7,
        0,92,93,5,8,0,0,93,95,1,0,0,0,94,89,1,0,0,0,94,90,1,0,0,0,95,7,1,
        0,0,0,96,97,5,42,0,0,97,106,5,3,0,0,98,103,3,30,15,0,99,100,5,10,
        0,0,100,102,3,30,15,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,106,98,1,0,0,
        0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,5,4,0,0,109,110,5,9,0,
        0,110,9,1,0,0,0,111,116,3,12,6,0,112,113,5,10,0,0,113,115,3,12,6,
        0,114,112,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,
        0,117,11,1,0,0,0,118,116,1,0,0,0,119,120,5,42,0,0,120,121,3,54,27,
        0,121,13,1,0,0,0,122,124,3,16,8,0,123,125,5,48,0,0,124,123,1,0,0,
        0,124,125,1,0,0,0,125,127,1,0,0,0,126,122,1,0,0,0,127,128,1,0,0,
        0,128,126,1,0,0,0,128,129,1,0,0,0,129,15,1,0,0,0,130,136,3,20,10,
        0,131,136,3,22,11,0,132,136,3,18,9,0,133,136,3,8,4,0,134,136,3,26,
        13,0,135,130,1,0,0,0,135,131,1,0,0,0,135,132,1,0,0,0,135,133,1,0,
        0,0,135,134,1,0,0,0,136,17,1,0,0,0,137,138,5,11,0,0,138,139,5,42,
        0,0,139,140,3,54,27,0,140,141,5,12,0,0,141,142,3,30,15,0,142,143,
        5,9,0,0,143,156,1,0,0,0,144,145,5,11,0,0,145,146,5,42,0,0,146,147,
        3,54,27,0,147,148,5,9,0,0,148,156,1,0,0,0,149,150,5,11,0,0,150,151,
        5,42,0,0,151,152,5,12,0,0,152,153,3,30,15,0,153,154,5,9,0,0,154,
        156,1,0,0,0,155,137,1,0,0,0,155,144,1,0,0,0,155,149,1,0,0,0,156,
        19,1,0,0,0,157,158,5,13,0,0,158,159,5,3,0,0,159,160,3,30,15,0,160,
        161,5,4,0,0,161,162,5,7,0,0,162,163,3,14,7,0,163,174,5,8,0,0,164,
        165,5,14,0,0,165,166,5,3,0,0,166,167,3,30,15,0,167,168,5,4,0,0,168,
        169,5,7,0,0,169,170,3,14,7,0,170,171,5,8,0,0,171,173,1,0,0,0,172,
        164,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,
        182,1,0,0,0,176,174,1,0,0,0,177,178,5,15,0,0,178,179,5,7,0,0,179,
        180,3,14,7,0,180,181,5,8,0,0,181,183,1,0,0,0,182,177,1,0,0,0,182,
        183,1,0,0,0,183,21,1,0,0,0,184,185,5,16,0,0,185,186,5,3,0,0,186,
        187,3,24,12,0,187,188,5,9,0,0,188,189,3,30,15,0,189,190,5,9,0,0,
        190,191,3,30,15,0,191,192,5,4,0,0,192,193,5,7,0,0,193,194,3,14,7,
        0,194,195,5,8,0,0,195,208,1,0,0,0,196,197,5,16,0,0,197,198,5,3,0,
        0,198,199,3,54,27,0,199,200,5,42,0,0,200,201,5,17,0,0,201,202,5,
        42,0,0,202,203,5,4,0,0,203,204,5,7,0,0,204,205,3,14,7,0,205,206,
        5,8,0,0,206,208,1,0,0,0,207,184,1,0,0,0,207,196,1,0,0,0,208,23,1,
        0,0,0,209,210,3,54,27,0,210,211,5,42,0,0,211,212,5,12,0,0,212,213,
        3,30,15,0,213,25,1,0,0,0,214,215,5,18,0,0,215,216,5,3,0,0,216,217,
        3,28,14,0,217,218,5,4,0,0,218,219,5,9,0,0,219,27,1,0,0,0,220,225,
        3,30,15,0,221,222,5,10,0,0,222,224,3,30,15,0,223,221,1,0,0,0,224,
        227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,29,1,0,0,0,227,225,
        1,0,0,0,228,229,3,32,16,0,229,31,1,0,0,0,230,235,3,34,17,0,231,232,
        5,19,0,0,232,234,3,34,17,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,
        1,0,0,0,235,236,1,0,0,0,236,33,1,0,0,0,237,235,1,0,0,0,238,243,3,
        36,18,0,239,240,5,20,0,0,240,242,3,36,18,0,241,239,1,0,0,0,242,245,
        1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,35,1,0,0,0,245,243,1,
        0,0,0,246,251,3,38,19,0,247,248,7,0,0,0,248,250,3,38,19,0,249,247,
        1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,37,1,
        0,0,0,253,251,1,0,0,0,254,259,3,40,20,0,255,256,7,1,0,0,256,258,
        3,40,20,0,257,255,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,
        1,0,0,0,260,39,1,0,0,0,261,259,1,0,0,0,262,267,3,42,21,0,263,264,
        7,2,0,0,264,266,3,42,21,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,
        1,0,0,0,267,268,1,0,0,0,268,41,1,0,0,0,269,267,1,0,0,0,270,275,3,
        44,22,0,271,272,7,3,0,0,272,274,3,44,22,0,273,271,1,0,0,0,274,277,
        1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,43,1,0,0,0,277,275,1,
        0,0,0,278,279,7,4,0,0,279,286,3,44,22,0,280,282,7,4,0,0,281,280,
        1,0,0,0,281,282,1,0,0,0,282,283,1,0,0,0,283,286,3,46,23,0,284,286,
        3,50,25,0,285,278,1,0,0,0,285,281,1,0,0,0,285,284,1,0,0,0,286,45,
        1,0,0,0,287,299,5,43,0,0,288,299,5,44,0,0,289,299,5,46,0,0,290,299,
        5,45,0,0,291,299,3,8,4,0,292,293,5,3,0,0,293,294,3,30,15,0,294,295,
        5,4,0,0,295,299,1,0,0,0,296,299,3,52,26,0,297,299,3,48,24,0,298,
        287,1,0,0,0,298,288,1,0,0,0,298,289,1,0,0,0,298,290,1,0,0,0,298,
        291,1,0,0,0,298,292,1,0,0,0,298,296,1,0,0,0,298,297,1,0,0,0,299,
        47,1,0,0,0,300,301,3,52,26,0,301,302,7,5,0,0,302,303,3,30,15,0,303,
        49,1,0,0,0,304,306,3,46,23,0,305,307,7,6,0,0,306,305,1,0,0,0,306,
        307,1,0,0,0,307,51,1,0,0,0,308,309,5,42,0,0,309,53,1,0,0,0,310,311,
        7,7,0,0,311,55,1,0,0,0,26,57,61,68,84,94,103,106,116,124,128,135,
        155,174,182,207,225,235,243,251,259,267,275,281,285,298,306
    ]

class freshParser ( Parser ):

    grammarFileName = "fresh.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'main'", "'('", "')'", "'->'", 
                     "'None'", "'{'", "'}'", "';'", "','", "'var'", "'='", 
                     "'if'", "'elif'", "'else'", "'for'", "'in'", "'print'", 
                     "'or'", "'and'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'+'", "'-'", "'*'", "'/'", "'not'", "'+='", 
                     "'-='", "'*='", "'/='", "'++'", "'--'", "'int'", "'float'", 
                     "'bool'", "'auto'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NAME", "INTEGER", "DOUBLE", 
                      "BOOL", "STRING", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_function_list = 1
    RULE_main_function = 2
    RULE_function = 3
    RULE_function_call = 4
    RULE_argument_list = 5
    RULE_argument = 6
    RULE_statements = 7
    RULE_statement = 8
    RULE_var_declaration = 9
    RULE_if_statement = 10
    RULE_for_loop_statement = 11
    RULE_for_loop_declaration = 12
    RULE_print = 13
    RULE_expression_list = 14
    RULE_expression = 15
    RULE_or_expression = 16
    RULE_and_expression = 17
    RULE_eq_expression = 18
    RULE_rel_expression = 19
    RULE_add_expression = 20
    RULE_mul_expression = 21
    RULE_un_expression = 22
    RULE_basic_expression = 23
    RULE_compound_assignment = 24
    RULE_postfix_expression = 25
    RULE_var_reference = 26
    RULE_type = 27

    ruleNames =  [ "program", "function_list", "main_function", "function", 
                   "function_call", "argument_list", "argument", "statements", 
                   "statement", "var_declaration", "if_statement", "for_loop_statement", 
                   "for_loop_declaration", "print", "expression_list", "expression", 
                   "or_expression", "and_expression", "eq_expression", "rel_expression", 
                   "add_expression", "mul_expression", "un_expression", 
                   "basic_expression", "compound_assignment", "postfix_expression", 
                   "var_reference", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    NAME=42
    INTEGER=43
    DOUBLE=44
    BOOL=45
    STRING=46
    COMMENT=47
    WS=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_function(self):
            return self.getTypedRuleContext(freshParser.Main_functionContext,0)


        def EOF(self):
            return self.getToken(freshParser.EOF, 0)

        def function_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.Function_listContext)
            else:
                return self.getTypedRuleContext(freshParser.Function_listContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = freshParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 56
                self.function_list()


            self.state = 59
            self.main_function()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 60
                self.function_list()


            self.state = 63
            self.match(freshParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.FunctionContext)
            else:
                return self.getTypedRuleContext(freshParser.FunctionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_function_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_list" ):
                listener.enterFunction_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_list" ):
                listener.exitFunction_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_list" ):
                return visitor.visitFunction_list(self)
            else:
                return visitor.visitChildren(self)




    def function_list(self):

        localctx = freshParser.Function_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 65
                    self.function()

                else:
                    raise NoViableAltException(self)
                self.state = 68 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(freshParser.StatementsContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_main_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_function" ):
                listener.enterMain_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_function" ):
                listener.exitMain_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function" ):
                return visitor.visitMain_function(self)
            else:
                return visitor.visitChildren(self)




    def main_function(self):

        localctx = freshParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(freshParser.T__0)
            self.state = 71
            self.match(freshParser.T__1)
            self.state = 72
            self.match(freshParser.T__2)
            self.state = 73
            self.match(freshParser.T__3)
            self.state = 74
            self.match(freshParser.T__4)
            self.state = 75
            self.match(freshParser.T__5)
            self.state = 76
            self.match(freshParser.T__6)
            self.state = 77
            self.statements()
            self.state = 78
            self.match(freshParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(freshParser.NAME, 0)

        def type_(self):
            return self.getTypedRuleContext(freshParser.TypeContext,0)


        def statements(self):
            return self.getTypedRuleContext(freshParser.StatementsContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(freshParser.Argument_listContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = freshParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(freshParser.T__0)
            self.state = 81
            self.match(freshParser.NAME)
            self.state = 82
            self.match(freshParser.T__2)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 83
                self.argument_list()


            self.state = 86
            self.match(freshParser.T__3)
            self.state = 87
            self.match(freshParser.T__4)
            self.state = 88
            self.type_()
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 89
                self.match(freshParser.T__8)
                pass
            elif token in [7]:
                self.state = 90
                self.match(freshParser.T__6)
                self.state = 91
                self.statements()
                self.state = 92
                self.match(freshParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(freshParser.NAME, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(freshParser.ExpressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = freshParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(freshParser.NAME)
            self.state = 97
            self.match(freshParser.T__2)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 136341857763336) != 0):
                self.state = 98
                self.expression()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 99
                    self.match(freshParser.T__9)
                    self.state = 100
                    self.expression()
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 108
            self.match(freshParser.T__3)
            self.state = 109
            self.match(freshParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(freshParser.ArgumentContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_list" ):
                listener.enterArgument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_list" ):
                listener.exitArgument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = freshParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.argument()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 112
                self.match(freshParser.T__9)
                self.state = 113
                self.argument()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(freshParser.NAME, 0)

        def type_(self):
            return self.getTypedRuleContext(freshParser.TypeContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = freshParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(freshParser.NAME)
            self.state = 120
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.StatementContext)
            else:
                return self.getTypedRuleContext(freshParser.StatementContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(freshParser.WS)
            else:
                return self.getToken(freshParser.WS, i)

        def getRuleIndex(self):
            return freshParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = freshParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 123
                    self.match(freshParser.WS)


                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046849024) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(freshParser.If_statementContext,0)


        def for_loop_statement(self):
            return self.getTypedRuleContext(freshParser.For_loop_statementContext,0)


        def var_declaration(self):
            return self.getTypedRuleContext(freshParser.Var_declarationContext,0)


        def function_call(self):
            return self.getTypedRuleContext(freshParser.Function_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(freshParser.PrintContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = freshParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.if_statement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.for_loop_statement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.var_declaration()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.function_call()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.print_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(freshParser.NAME, 0)

        def type_(self):
            return self.getTypedRuleContext(freshParser.TypeContext,0)


        def expression(self):
            return self.getTypedRuleContext(freshParser.ExpressionContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_var_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declaration" ):
                listener.enterVar_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declaration" ):
                listener.exitVar_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration" ):
                return visitor.visitVar_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration(self):

        localctx = freshParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_declaration)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(freshParser.T__10)
                self.state = 138
                self.match(freshParser.NAME)
                self.state = 139
                self.type_()
                self.state = 140
                self.match(freshParser.T__11)
                self.state = 141
                self.expression()
                self.state = 142
                self.match(freshParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(freshParser.T__10)
                self.state = 145
                self.match(freshParser.NAME)
                self.state = 146
                self.type_()
                self.state = 147
                self.match(freshParser.T__8)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.match(freshParser.T__10)
                self.state = 150
                self.match(freshParser.NAME)
                self.state = 151
                self.match(freshParser.T__11)
                self.state = 152
                self.expression()
                self.state = 153
                self.match(freshParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(freshParser.ExpressionContext,i)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.StatementsContext)
            else:
                return self.getTypedRuleContext(freshParser.StatementsContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = freshParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(freshParser.T__12)
            self.state = 158
            self.match(freshParser.T__2)
            self.state = 159
            self.expression()
            self.state = 160
            self.match(freshParser.T__3)
            self.state = 161
            self.match(freshParser.T__6)
            self.state = 162
            self.statements()
            self.state = 163
            self.match(freshParser.T__7)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 164
                self.match(freshParser.T__13)
                self.state = 165
                self.match(freshParser.T__2)
                self.state = 166
                self.expression()
                self.state = 167
                self.match(freshParser.T__3)
                self.state = 168
                self.match(freshParser.T__6)
                self.state = 169
                self.statements()
                self.state = 170
                self.match(freshParser.T__7)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 177
                self.match(freshParser.T__14)
                self.state = 178
                self.match(freshParser.T__6)
                self.state = 179
                self.statements()
                self.state = 180
                self.match(freshParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_loop_declaration(self):
            return self.getTypedRuleContext(freshParser.For_loop_declarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(freshParser.ExpressionContext,i)


        def statements(self):
            return self.getTypedRuleContext(freshParser.StatementsContext,0)


        def type_(self):
            return self.getTypedRuleContext(freshParser.TypeContext,0)


        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(freshParser.NAME)
            else:
                return self.getToken(freshParser.NAME, i)

        def getRuleIndex(self):
            return freshParser.RULE_for_loop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop_statement" ):
                listener.enterFor_loop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop_statement" ):
                listener.exitFor_loop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_statement" ):
                return visitor.visitFor_loop_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_statement(self):

        localctx = freshParser.For_loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_loop_statement)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(freshParser.T__15)
                self.state = 185
                self.match(freshParser.T__2)
                self.state = 186
                self.for_loop_declaration()
                self.state = 187
                self.match(freshParser.T__8)
                self.state = 188
                self.expression()
                self.state = 189
                self.match(freshParser.T__8)
                self.state = 190
                self.expression()
                self.state = 191
                self.match(freshParser.T__3)
                self.state = 192
                self.match(freshParser.T__6)
                self.state = 193
                self.statements()
                self.state = 194
                self.match(freshParser.T__7)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(freshParser.T__15)
                self.state = 197
                self.match(freshParser.T__2)
                self.state = 198
                self.type_()
                self.state = 199
                self.match(freshParser.NAME)
                self.state = 200
                self.match(freshParser.T__16)
                self.state = 201
                self.match(freshParser.NAME)
                self.state = 202
                self.match(freshParser.T__3)
                self.state = 203
                self.match(freshParser.T__6)
                self.state = 204
                self.statements()
                self.state = 205
                self.match(freshParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(freshParser.TypeContext,0)


        def NAME(self):
            return self.getToken(freshParser.NAME, 0)

        def expression(self):
            return self.getTypedRuleContext(freshParser.ExpressionContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_for_loop_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop_declaration" ):
                listener.enterFor_loop_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop_declaration" ):
                listener.exitFor_loop_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_declaration" ):
                return visitor.visitFor_loop_declaration(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_declaration(self):

        localctx = freshParser.For_loop_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_loop_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.type_()
            self.state = 210
            self.match(freshParser.NAME)
            self.state = 211
            self.match(freshParser.T__11)
            self.state = 212
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(freshParser.Expression_listContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = freshParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(freshParser.T__17)
            self.state = 215
            self.match(freshParser.T__2)
            self.state = 216
            self.expression_list()
            self.state = 217
            self.match(freshParser.T__3)
            self.state = 218
            self.match(freshParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(freshParser.ExpressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = freshParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.expression()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 221
                self.match(freshParser.T__9)
                self.state = 222
                self.expression()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_expression(self):
            return self.getTypedRuleContext(freshParser.Or_expressionContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = freshParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.or_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.And_expressionContext)
            else:
                return self.getTypedRuleContext(freshParser.And_expressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_expression" ):
                listener.enterOr_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_expression" ):
                listener.exitOr_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_expression" ):
                return visitor.visitOr_expression(self)
            else:
                return visitor.visitChildren(self)




    def or_expression(self):

        localctx = freshParser.Or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_or_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.and_expression()
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 231
                    self.match(freshParser.T__18)
                    self.state = 232
                    self.and_expression() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eq_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.Eq_expressionContext)
            else:
                return self.getTypedRuleContext(freshParser.Eq_expressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expression" ):
                listener.enterAnd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expression" ):
                listener.exitAnd_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expression" ):
                return visitor.visitAnd_expression(self)
            else:
                return visitor.visitChildren(self)




    def and_expression(self):

        localctx = freshParser.And_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_and_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.eq_expression()
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 239
                    self.match(freshParser.T__19)
                    self.state = 240
                    self.eq_expression() 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eq_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.Rel_expressionContext)
            else:
                return self.getTypedRuleContext(freshParser.Rel_expressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_eq_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq_expression" ):
                listener.enterEq_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq_expression" ):
                listener.exitEq_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq_expression" ):
                return visitor.visitEq_expression(self)
            else:
                return visitor.visitChildren(self)




    def eq_expression(self):

        localctx = freshParser.Eq_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_eq_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.rel_expression()
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 247
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 248
                    self.rel_expression() 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.Add_expressionContext)
            else:
                return self.getTypedRuleContext(freshParser.Add_expressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_rel_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_expression" ):
                listener.enterRel_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_expression" ):
                listener.exitRel_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_expression" ):
                return visitor.visitRel_expression(self)
            else:
                return visitor.visitChildren(self)




    def rel_expression(self):

        localctx = freshParser.Rel_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_rel_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.add_expression()
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 255
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.add_expression() 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.Mul_expressionContext)
            else:
                return self.getTypedRuleContext(freshParser.Mul_expressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_add_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_expression" ):
                listener.enterAdd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_expression" ):
                listener.exitAdd_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expression" ):
                return visitor.visitAdd_expression(self)
            else:
                return visitor.visitChildren(self)




    def add_expression(self):

        localctx = freshParser.Add_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_add_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.mul_expression()
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.mul_expression() 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def un_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.Un_expressionContext)
            else:
                return self.getTypedRuleContext(freshParser.Un_expressionContext,i)


        def getRuleIndex(self):
            return freshParser.RULE_mul_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_expression" ):
                listener.enterMul_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_expression" ):
                listener.exitMul_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expression" ):
                return visitor.visitMul_expression(self)
            else:
                return visitor.visitChildren(self)




    def mul_expression(self):

        localctx = freshParser.Mul_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_mul_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.un_expression()
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 271
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 272
                    self.un_expression() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Un_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def un_expression(self):
            return self.getTypedRuleContext(freshParser.Un_expressionContext,0)


        def basic_expression(self):
            return self.getTypedRuleContext(freshParser.Basic_expressionContext,0)


        def postfix_expression(self):
            return self.getTypedRuleContext(freshParser.Postfix_expressionContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_un_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUn_expression" ):
                listener.enterUn_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUn_expression" ):
                listener.exitUn_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUn_expression" ):
                return visitor.visitUn_expression(self)
            else:
                return visitor.visitChildren(self)




    def un_expression(self):

        localctx = freshParser.Un_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_un_expression)
        self._la = 0 # Token type
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                _la = self._input.LA(1)
                if not(_la==28 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                self.un_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28 or _la==31:
                    self.state = 280
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==31):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 283
                self.basic_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.postfix_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(freshParser.INTEGER, 0)

        def DOUBLE(self):
            return self.getToken(freshParser.DOUBLE, 0)

        def STRING(self):
            return self.getToken(freshParser.STRING, 0)

        def BOOL(self):
            return self.getToken(freshParser.BOOL, 0)

        def function_call(self):
            return self.getTypedRuleContext(freshParser.Function_callContext,0)


        def expression(self):
            return self.getTypedRuleContext(freshParser.ExpressionContext,0)


        def var_reference(self):
            return self.getTypedRuleContext(freshParser.Var_referenceContext,0)


        def compound_assignment(self):
            return self.getTypedRuleContext(freshParser.Compound_assignmentContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_basic_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_expression" ):
                listener.enterBasic_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_expression" ):
                listener.exitBasic_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_expression" ):
                return visitor.visitBasic_expression(self)
            else:
                return visitor.visitChildren(self)




    def basic_expression(self):

        localctx = freshParser.Basic_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_basic_expression)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(freshParser.INTEGER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(freshParser.DOUBLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.match(freshParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 290
                self.match(freshParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 291
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 292
                self.match(freshParser.T__2)
                self.state = 293
                self.expression()
                self.state = 294
                self.match(freshParser.T__3)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 296
                self.var_reference()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 297
                self.compound_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_reference(self):
            return self.getTypedRuleContext(freshParser.Var_referenceContext,0)


        def expression(self):
            return self.getTypedRuleContext(freshParser.ExpressionContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_compound_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_assignment" ):
                listener.enterCompound_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_assignment" ):
                listener.exitCompound_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_assignment" ):
                return visitor.visitCompound_assignment(self)
            else:
                return visitor.visitChildren(self)




    def compound_assignment(self):

        localctx = freshParser.Compound_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_compound_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.var_reference()
            self.state = 301
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 302
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_expression(self):
            return self.getTypedRuleContext(freshParser.Basic_expressionContext,0)


        def getRuleIndex(self):
            return freshParser.RULE_postfix_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_expression" ):
                listener.enterPostfix_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_expression" ):
                listener.exitPostfix_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_expression" ):
                return visitor.visitPostfix_expression(self)
            else:
                return visitor.visitChildren(self)




    def postfix_expression(self):

        localctx = freshParser.Postfix_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_postfix_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.basic_expression()
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 305
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(freshParser.NAME, 0)

        def getRuleIndex(self):
            return freshParser.RULE_var_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_reference" ):
                listener.enterVar_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_reference" ):
                listener.exitVar_reference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_reference" ):
                return visitor.visitVar_reference(self)
            else:
                return visitor.visitChildren(self)




    def var_reference(self):

        localctx = freshParser.Var_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_var_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(freshParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return freshParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = freshParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4123168604224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





