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
        4,1,47,305,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,3,0,56,8,0,1,0,1,0,3,0,60,8,0,1,0,1,0,1,1,4,1,65,8,1,11,1,12,
        1,66,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,82,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,91,8,3,1,4,1,4,1,4,1,4,1,4,5,
        4,98,8,4,10,4,12,4,101,9,4,3,4,103,8,4,1,4,1,4,1,5,1,5,1,5,5,5,110,
        8,5,10,5,12,5,113,9,5,1,6,1,6,1,6,1,7,1,7,3,7,120,8,7,4,7,122,8,
        7,11,7,12,7,123,1,8,1,8,1,8,1,8,3,8,130,8,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,150,8,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,5,10,167,8,10,10,10,12,10,170,9,10,1,10,1,10,1,10,1,10,
        1,10,3,10,177,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,205,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,5,13,216,8,13,10,13,12,13,219,9,13,1,14,1,14,1,15,
        1,15,1,15,5,15,226,8,15,10,15,12,15,229,9,15,1,16,1,16,1,16,5,16,
        234,8,16,10,16,12,16,237,9,16,1,17,1,17,1,17,5,17,242,8,17,10,17,
        12,17,245,9,17,1,18,1,18,1,18,5,18,250,8,18,10,18,12,18,253,9,18,
        1,19,1,19,1,19,5,19,258,8,19,10,19,12,19,261,9,19,1,20,1,20,1,20,
        5,20,266,8,20,10,20,12,20,269,9,20,1,21,1,21,1,21,3,21,274,8,21,
        1,21,1,21,3,21,278,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,3,22,291,8,22,1,23,1,23,1,23,1,23,1,24,1,24,3,24,
        299,8,24,1,25,1,25,1,26,1,26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,8,1,0,20,21,
        1,0,22,25,1,0,26,27,1,0,28,29,2,0,27,27,30,30,1,0,31,34,1,0,35,36,
        2,0,5,5,37,40,313,0,55,1,0,0,0,2,64,1,0,0,0,4,68,1,0,0,0,6,77,1,
        0,0,0,8,92,1,0,0,0,10,106,1,0,0,0,12,114,1,0,0,0,14,121,1,0,0,0,
        16,129,1,0,0,0,18,149,1,0,0,0,20,151,1,0,0,0,22,204,1,0,0,0,24,206,
        1,0,0,0,26,212,1,0,0,0,28,220,1,0,0,0,30,222,1,0,0,0,32,230,1,0,
        0,0,34,238,1,0,0,0,36,246,1,0,0,0,38,254,1,0,0,0,40,262,1,0,0,0,
        42,277,1,0,0,0,44,290,1,0,0,0,46,292,1,0,0,0,48,296,1,0,0,0,50,300,
        1,0,0,0,52,302,1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,0,55,56,1,0,0,0,
        56,57,1,0,0,0,57,59,3,4,2,0,58,60,3,2,1,0,59,58,1,0,0,0,59,60,1,
        0,0,0,60,61,1,0,0,0,61,62,5,0,0,1,62,1,1,0,0,0,63,65,3,6,3,0,64,
        63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,3,1,0,0,
        0,68,69,5,1,0,0,69,70,5,2,0,0,70,71,5,3,0,0,71,72,5,4,0,0,72,73,
        5,5,0,0,73,74,5,6,0,0,74,75,3,14,7,0,75,76,5,7,0,0,76,5,1,0,0,0,
        77,78,5,1,0,0,78,79,5,41,0,0,79,81,5,3,0,0,80,82,3,10,5,0,81,80,
        1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,5,4,0,0,84,90,3,52,26,
        0,85,91,5,8,0,0,86,87,5,6,0,0,87,88,3,14,7,0,88,89,5,7,0,0,89,91,
        1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,91,7,1,0,0,0,92,93,5,41,0,0,
        93,102,5,3,0,0,94,99,3,28,14,0,95,96,5,9,0,0,96,98,3,28,14,0,97,
        95,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,103,1,
        0,0,0,101,99,1,0,0,0,102,94,1,0,0,0,102,103,1,0,0,0,103,104,1,0,
        0,0,104,105,5,4,0,0,105,9,1,0,0,0,106,111,3,12,6,0,107,108,5,9,0,
        0,108,110,3,12,6,0,109,107,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,
        0,111,112,1,0,0,0,112,11,1,0,0,0,113,111,1,0,0,0,114,115,5,41,0,
        0,115,116,3,52,26,0,116,13,1,0,0,0,117,119,3,16,8,0,118,120,5,47,
        0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,117,1,0,
        0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,15,1,0,0,
        0,125,130,3,20,10,0,126,130,3,22,11,0,127,130,3,18,9,0,128,130,3,
        24,12,0,129,125,1,0,0,0,129,126,1,0,0,0,129,127,1,0,0,0,129,128,
        1,0,0,0,130,17,1,0,0,0,131,132,5,10,0,0,132,133,5,41,0,0,133,134,
        3,52,26,0,134,135,5,11,0,0,135,136,3,28,14,0,136,137,5,8,0,0,137,
        150,1,0,0,0,138,139,5,10,0,0,139,140,5,41,0,0,140,141,3,52,26,0,
        141,142,5,8,0,0,142,150,1,0,0,0,143,144,5,10,0,0,144,145,5,41,0,
        0,145,146,5,11,0,0,146,147,3,28,14,0,147,148,5,8,0,0,148,150,1,0,
        0,0,149,131,1,0,0,0,149,138,1,0,0,0,149,143,1,0,0,0,150,19,1,0,0,
        0,151,152,5,12,0,0,152,153,5,3,0,0,153,154,3,28,14,0,154,155,5,4,
        0,0,155,156,5,6,0,0,156,157,3,14,7,0,157,168,5,7,0,0,158,159,5,13,
        0,0,159,160,5,3,0,0,160,161,3,28,14,0,161,162,5,4,0,0,162,163,5,
        6,0,0,163,164,3,14,7,0,164,165,5,7,0,0,165,167,1,0,0,0,166,158,1,
        0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,176,1,
        0,0,0,170,168,1,0,0,0,171,172,5,14,0,0,172,173,5,6,0,0,173,174,3,
        14,7,0,174,175,5,7,0,0,175,177,1,0,0,0,176,171,1,0,0,0,176,177,1,
        0,0,0,177,21,1,0,0,0,178,179,5,15,0,0,179,180,5,3,0,0,180,181,3,
        52,26,0,181,182,5,41,0,0,182,183,5,11,0,0,183,184,3,28,14,0,184,
        185,5,8,0,0,185,186,3,28,14,0,186,187,5,8,0,0,187,188,3,28,14,0,
        188,189,5,4,0,0,189,190,5,6,0,0,190,191,3,14,7,0,191,192,5,7,0,0,
        192,205,1,0,0,0,193,194,5,15,0,0,194,195,5,3,0,0,195,196,3,52,26,
        0,196,197,5,41,0,0,197,198,5,16,0,0,198,199,5,41,0,0,199,200,5,4,
        0,0,200,201,5,6,0,0,201,202,3,14,7,0,202,203,5,7,0,0,203,205,1,0,
        0,0,204,178,1,0,0,0,204,193,1,0,0,0,205,23,1,0,0,0,206,207,5,17,
        0,0,207,208,5,3,0,0,208,209,3,26,13,0,209,210,5,4,0,0,210,211,5,
        8,0,0,211,25,1,0,0,0,212,217,3,28,14,0,213,214,5,9,0,0,214,216,3,
        28,14,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,
        1,0,0,0,218,27,1,0,0,0,219,217,1,0,0,0,220,221,3,30,15,0,221,29,
        1,0,0,0,222,227,3,32,16,0,223,224,5,18,0,0,224,226,3,32,16,0,225,
        223,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        31,1,0,0,0,229,227,1,0,0,0,230,235,3,34,17,0,231,232,5,19,0,0,232,
        234,3,34,17,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,
        236,1,0,0,0,236,33,1,0,0,0,237,235,1,0,0,0,238,243,3,36,18,0,239,
        240,7,0,0,0,240,242,3,36,18,0,241,239,1,0,0,0,242,245,1,0,0,0,243,
        241,1,0,0,0,243,244,1,0,0,0,244,35,1,0,0,0,245,243,1,0,0,0,246,251,
        3,38,19,0,247,248,7,1,0,0,248,250,3,38,19,0,249,247,1,0,0,0,250,
        253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,37,1,0,0,0,253,251,
        1,0,0,0,254,259,3,40,20,0,255,256,7,2,0,0,256,258,3,40,20,0,257,
        255,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,
        39,1,0,0,0,261,259,1,0,0,0,262,267,3,42,21,0,263,264,7,3,0,0,264,
        266,3,42,21,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,
        268,1,0,0,0,268,41,1,0,0,0,269,267,1,0,0,0,270,271,7,4,0,0,271,278,
        3,42,21,0,272,274,7,4,0,0,273,272,1,0,0,0,273,274,1,0,0,0,274,275,
        1,0,0,0,275,278,3,44,22,0,276,278,3,48,24,0,277,270,1,0,0,0,277,
        273,1,0,0,0,277,276,1,0,0,0,278,43,1,0,0,0,279,291,5,42,0,0,280,
        291,5,43,0,0,281,291,5,45,0,0,282,291,5,44,0,0,283,291,3,8,4,0,284,
        285,5,3,0,0,285,286,3,28,14,0,286,287,5,4,0,0,287,291,1,0,0,0,288,
        291,3,50,25,0,289,291,3,46,23,0,290,279,1,0,0,0,290,280,1,0,0,0,
        290,281,1,0,0,0,290,282,1,0,0,0,290,283,1,0,0,0,290,284,1,0,0,0,
        290,288,1,0,0,0,290,289,1,0,0,0,291,45,1,0,0,0,292,293,3,50,25,0,
        293,294,7,5,0,0,294,295,3,28,14,0,295,47,1,0,0,0,296,298,3,44,22,
        0,297,299,7,6,0,0,298,297,1,0,0,0,298,299,1,0,0,0,299,49,1,0,0,0,
        300,301,5,41,0,0,301,51,1,0,0,0,302,303,7,7,0,0,303,53,1,0,0,0,26,
        55,59,66,81,90,99,102,111,119,123,129,149,168,176,204,217,227,235,
        243,251,259,267,273,277,290,298
    ]

class freshParser ( Parser ):

    grammarFileName = "fresh.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'main'", "'('", "')'", "'None'", 
                     "'{'", "'}'", "';'", "','", "'var'", "'='", "'if'", 
                     "'elif'", "'else'", "'for'", "'in'", "'print'", "'or'", 
                     "'and'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'+'", "'-'", "'*'", "'/'", "'not'", "'+='", "'-='", 
                     "'*='", "'/='", "'++'", "'--'", "'int'", "'float'", 
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
                      "<INVALID>", "NAME", "INTEGER", "DOUBLE", "BOOL", 
                      "STRING", "COMMENT", "WS" ]

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
    RULE_print = 12
    RULE_expression_list = 13
    RULE_expression = 14
    RULE_or_expression = 15
    RULE_and_expression = 16
    RULE_eq_expression = 17
    RULE_rel_expression = 18
    RULE_add_expression = 19
    RULE_mul_expression = 20
    RULE_un_expression = 21
    RULE_basic_expression = 22
    RULE_compound_assignment = 23
    RULE_postfix_expression = 24
    RULE_var_reference = 25
    RULE_type = 26

    ruleNames =  [ "program", "function_list", "main_function", "function", 
                   "function_call", "argument_list", "argument", "statements", 
                   "statement", "var_declaration", "if_statement", "for_loop_statement", 
                   "print", "expression_list", "expression", "or_expression", 
                   "and_expression", "eq_expression", "rel_expression", 
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
    NAME=41
    INTEGER=42
    DOUBLE=43
    BOOL=44
    STRING=45
    COMMENT=46
    WS=47

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
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 54
                self.function_list()


            self.state = 57
            self.main_function()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 58
                self.function_list()


            self.state = 61
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
            self.state = 64 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 63
                    self.function()

                else:
                    raise NoViableAltException(self)
                self.state = 66 
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
            self.state = 68
            self.match(freshParser.T__0)
            self.state = 69
            self.match(freshParser.T__1)
            self.state = 70
            self.match(freshParser.T__2)
            self.state = 71
            self.match(freshParser.T__3)
            self.state = 72
            self.match(freshParser.T__4)
            self.state = 73
            self.match(freshParser.T__5)
            self.state = 74
            self.statements()
            self.state = 75
            self.match(freshParser.T__6)
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
            self.state = 77
            self.match(freshParser.T__0)
            self.state = 78
            self.match(freshParser.NAME)
            self.state = 79
            self.match(freshParser.T__2)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 80
                self.argument_list()


            self.state = 83
            self.match(freshParser.T__3)
            self.state = 84
            self.type_()
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 85
                self.match(freshParser.T__7)
                pass
            elif token in [6]:
                self.state = 86
                self.match(freshParser.T__5)
                self.state = 87
                self.statements()
                self.state = 88
                self.match(freshParser.T__6)
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
            self.state = 92
            self.match(freshParser.NAME)
            self.state = 93
            self.match(freshParser.T__2)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68170928881672) != 0):
                self.state = 94
                self.expression()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 95
                    self.match(freshParser.T__8)
                    self.state = 96
                    self.expression()
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 104
            self.match(freshParser.T__3)
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
            self.state = 106
            self.argument()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 107
                self.match(freshParser.T__8)
                self.state = 108
                self.argument()
                self.state = 113
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
            self.state = 114
            self.match(freshParser.NAME)
            self.state = 115
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
            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.statement()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==47:
                    self.state = 118
                    self.match(freshParser.WS)


                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 168960) != 0)):
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
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.if_statement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.for_loop_statement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.var_declaration()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
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
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(freshParser.T__9)
                self.state = 132
                self.match(freshParser.NAME)
                self.state = 133
                self.type_()
                self.state = 134
                self.match(freshParser.T__10)
                self.state = 135
                self.expression()
                self.state = 136
                self.match(freshParser.T__7)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(freshParser.T__9)
                self.state = 139
                self.match(freshParser.NAME)
                self.state = 140
                self.type_()
                self.state = 141
                self.match(freshParser.T__7)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(freshParser.T__9)
                self.state = 144
                self.match(freshParser.NAME)
                self.state = 145
                self.match(freshParser.T__10)
                self.state = 146
                self.expression()
                self.state = 147
                self.match(freshParser.T__7)
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
            self.state = 151
            self.match(freshParser.T__11)
            self.state = 152
            self.match(freshParser.T__2)
            self.state = 153
            self.expression()
            self.state = 154
            self.match(freshParser.T__3)
            self.state = 155
            self.match(freshParser.T__5)
            self.state = 156
            self.statements()
            self.state = 157
            self.match(freshParser.T__6)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 158
                self.match(freshParser.T__12)
                self.state = 159
                self.match(freshParser.T__2)
                self.state = 160
                self.expression()
                self.state = 161
                self.match(freshParser.T__3)
                self.state = 162
                self.match(freshParser.T__5)
                self.state = 163
                self.statements()
                self.state = 164
                self.match(freshParser.T__6)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 171
                self.match(freshParser.T__13)
                self.state = 172
                self.match(freshParser.T__5)
                self.state = 173
                self.statements()
                self.state = 174
                self.match(freshParser.T__6)


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

        def type_(self):
            return self.getTypedRuleContext(freshParser.TypeContext,0)


        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(freshParser.NAME)
            else:
                return self.getToken(freshParser.NAME, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(freshParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(freshParser.ExpressionContext,i)


        def statements(self):
            return self.getTypedRuleContext(freshParser.StatementsContext,0)


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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(freshParser.T__14)
                self.state = 179
                self.match(freshParser.T__2)
                self.state = 180
                self.type_()
                self.state = 181
                self.match(freshParser.NAME)
                self.state = 182
                self.match(freshParser.T__10)
                self.state = 183
                self.expression()
                self.state = 184
                self.match(freshParser.T__7)
                self.state = 185
                self.expression()
                self.state = 186
                self.match(freshParser.T__7)
                self.state = 187
                self.expression()
                self.state = 188
                self.match(freshParser.T__3)
                self.state = 189
                self.match(freshParser.T__5)
                self.state = 190
                self.statements()
                self.state = 191
                self.match(freshParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(freshParser.T__14)
                self.state = 194
                self.match(freshParser.T__2)
                self.state = 195
                self.type_()
                self.state = 196
                self.match(freshParser.NAME)
                self.state = 197
                self.match(freshParser.T__15)
                self.state = 198
                self.match(freshParser.NAME)
                self.state = 199
                self.match(freshParser.T__3)
                self.state = 200
                self.match(freshParser.T__5)
                self.state = 201
                self.statements()
                self.state = 202
                self.match(freshParser.T__6)
                pass


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
        self.enterRule(localctx, 24, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(freshParser.T__16)
            self.state = 207
            self.match(freshParser.T__2)
            self.state = 208
            self.expression_list()
            self.state = 209
            self.match(freshParser.T__3)
            self.state = 210
            self.match(freshParser.T__7)
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
        self.enterRule(localctx, 26, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.expression()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 213
                self.match(freshParser.T__8)
                self.state = 214
                self.expression()
                self.state = 219
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
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
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
        self.enterRule(localctx, 30, self.RULE_or_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.and_expression()
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 223
                    self.match(freshParser.T__17)
                    self.state = 224
                    self.and_expression() 
                self.state = 229
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
        self.enterRule(localctx, 32, self.RULE_and_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.eq_expression()
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 231
                    self.match(freshParser.T__18)
                    self.state = 232
                    self.eq_expression() 
                self.state = 237
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
        self.enterRule(localctx, 34, self.RULE_eq_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.rel_expression()
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 239
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.rel_expression() 
                self.state = 245
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
        self.enterRule(localctx, 36, self.RULE_rel_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.add_expression()
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 247
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 248
                    self.add_expression() 
                self.state = 253
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
        self.enterRule(localctx, 38, self.RULE_add_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.mul_expression()
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 255
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.mul_expression() 
                self.state = 261
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
        self.enterRule(localctx, 40, self.RULE_mul_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.un_expression()
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.un_expression() 
                self.state = 269
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
        self.enterRule(localctx, 42, self.RULE_un_expression)
        self._la = 0 # Token type
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                _la = self._input.LA(1)
                if not(_la==27 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                self.un_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27 or _la==30:
                    self.state = 272
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 275
                self.basic_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
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
        self.enterRule(localctx, 44, self.RULE_basic_expression)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(freshParser.INTEGER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(freshParser.DOUBLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(freshParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.match(freshParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                self.match(freshParser.T__2)
                self.state = 285
                self.expression()
                self.state = 286
                self.match(freshParser.T__3)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.var_reference()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 289
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
        self.enterRule(localctx, 46, self.RULE_compound_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.var_reference()
            self.state = 293
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 294
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
        self.enterRule(localctx, 48, self.RULE_postfix_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.basic_expression()
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==35 or _la==36):
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
        self.enterRule(localctx, 50, self.RULE_var_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
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
        self.enterRule(localctx, 52, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2061584302112) != 0)):
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





