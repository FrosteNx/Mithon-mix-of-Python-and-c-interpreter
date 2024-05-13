grammar Mithon;

program: statement* EOF;

statement: 
           varDeclaration
         | constDeclaration
         | tempDeclaration
         | forLoop
         | ifStatement
         | functionDeclaration
         | printFunction
         | expression
         | COMMENT
         ;

printFunction: 'print' '(' expression ')';

varDeclaration: 
                 type IDENTIFIER '=' expression
              | 'List' '[' type ']' IDENTIFIER '=' '[' expressionList ']'
              | 'ndList' '[' type ']' IDENTIFIER '=' '[' expressionList ']'
              | IDENTIFIER '=' expression
              | type IDENTIFIER
              ;

constDeclaration: 'const' type IDENTIFIER '=' expression;

tempDeclaration: 'temp' type IDENTIFIER '=' expression;

type: 'int' | 'double' | 'bool' | 'string';

forLoop: 
       'for' '(' type IDENTIFIER '=' expression ';' expression ';' expression ')' ':' statement*
     | 'for' '(' 'auto' IDENTIFIER 'in' IDENTIFIER ')' ':' statement*
       ;

ifStatement: 
       'if' '(' expression ')' ':' statement* ('elif' '(' expression ')' ':' statement*)* ('else' ':' statement*)?
       ;

functionDeclaration: 
       'def' IDENTIFIER '(' parameterList ')' '->' type ':' statement*;

parameterList: type IDENTIFIER (',' type IDENTIFIER)*;

functionCall: IDENTIFIER '(' argumentList ')';

argumentList: expression (',' expression)*;

expressionList: expression (',' expression)*;

expression: 
            expression '+' expression
          | expression '-' expression
          | expression '*' expression
          | expression '/' expression
          | expression '%' expression
          | IDENTIFIER '%' expression
          | IDENTIFIER '+=' expression
          | IDENTIFIER '-=' expression
          | IDENTIFIER '*=' expression
          | IDENTIFIER '/=' expression
          | IDENTIFIER '%=' expression
          | expression '==' expression
          | expression '!=' expression
          | expression '<' expression
          | expression '>' expression
          | expression 'and' expression
          | expression 'or' expression
          | 'not' expression
          | '(' expression ')'
          | functionCall
          | IDENTIFIER
          | NUMBER
          | STRING
          | 'true'
          | 'false'
          ;

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' .*? '"';
COMMENT: '//' .*? '\n' -> skip; 
WS: [ \t\r\n]+ -> skip;
