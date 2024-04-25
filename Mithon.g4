grammar Mithon;

program: statement* EOF;

statement: 
           statement_list
         | varDeclaration 
         | constDeclaration 
         | tempDeclaration 
         | forLoop
         | ifStatement
         | functionDeclaration
         | printFunction
         | expressionStatement
         | COMMENT
         | 'pass'
         ;

statement_list: INDENT statement+ DEDENT;

printFunction: 'print' '(' expressionList ')';

type: 'int' | 'double' | 'bool' | 'string';

varDeclaration: 
                 type IDENTIFIER '=' expression
              | 'List' '[' type ']' IDENTIFIER '=' '[' expressionList ']'
              | 'ndList' '[' type ']' IDENTIFIER '=' '[' expressionList ']'
              | IDENTIFIER '=' expression
              | type IDENTIFIER
              ;

constDeclaration: 'const' type IDENTIFIER '=' expression;

tempDeclaration: 'temp' type IDENTIFIER '=' expression;

forLoop: 
       'for' '(' type IDENTIFIER '=' expression ';' expression ';' expression ')' ':' statement_list
     | 'for' '(' 'auto' IDENTIFIER 'in' IDENTIFIER ')' ':' statement_list
       ;

ifStatement: 
       'if' '(' expression ')' ':' statement_list ('elif' '(' expression ')' ':' statement_list)* ('else' ':' statement_list)?
       ;

functionDeclaration: 
       'def' IDENTIFIER '(' parameterList ')' '->' type ':' statement_list;

parameterList: type IDENTIFIER (',' type IDENTIFIER)*;

functionCall: IDENTIFIER '(' argumentList ')';

argumentList: expression (',' expression)*;

expressionList: expression (',' expression)*;

expressionStatement: expression;

expression: 
            logicalOrExpression
          ;

logicalOrExpression:
            logicalAndExpression ('or' logicalAndExpression)*
          ;

logicalAndExpression:
            equalityExpression ('and' equalityExpression)*
          ;

equalityExpression:
            relationalExpression (('==' | '!=') relationalExpression)*
          ;

relationalExpression:
            additiveExpression (('<' | '>' | '<=' | '>=') additiveExpression)*
          ;

additiveExpression:
            multiplicativeExpression ((('+' | '-') multiplicativeExpression) | (('+=' | '-=') expression))* 
          ;

multiplicativeExpression:
            unaryExpression ((('*' | '/') unaryExpression) | (('*=' | '/=') expression))* 
          ;

unaryExpression:
            ('not' | '-')? primaryExpression
          ;

primaryExpression:
            '(' expression ')'
          | functionCall
          | IDENTIFIER
          | INTEGER
          | DOUBLE
          | STRING
          | 'true'
          | 'false'
          ;

INDENT: '    ';
DEDENT: '\n';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
INTEGER: [0-9]+;
DOUBLE: [0-9]+'.'[0-9]+;
STRING: '"' .*? '"';
COMMENT: '//' .*? '\n' -> skip; 
WS: [ \t\r\n]+ -> skip;
