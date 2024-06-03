grammar Mithon;

program: statement* EOF;

statement: 
           statement_list
         | varDeclaration 
         | constDeclaration 
         | forLoop
         | whileLoop
         | ifStatement
         | functionDeclaration
         | printFunction
         | returnStatement
         | expressionStatement
         | augAssignment
         | COMMENT
         | 'pass'
         ;

statement_list: '{' statement+ '}';

printFunction: 'print' '(' expressionList ')';

type: 'int' | 'float' | 'bool' | 'str';

complexType: 'List' '[' type ']' | 'Matrix' '[' type ']' | 'Array' '[' INTEGER ',' type ']';

func_return_type: type | 'None' | complexType;

varDeclaration: 
                (type|complexType) IDENTIFIER '=' expression
              | name '=' expression
              | (type|complexType) IDENTIFIER
              ;

constDeclaration: 'const' varDeclaration;

forLoop: 
        'for' '(' type IDENTIFIER '=' expression ';' expression ';' expression ')' statement_list
      | 'for' '(' type* IDENTIFIER 'in' IDENTIFIER ')' statement_list
      | 'for' statement_list
      ;

whileLoop: 'while' '(' expression ')' statement_list;

ifStatement: 
       'if' '(' expression ')' statement_list ('elif' '(' expression ')' statement_list)* ('else' statement_list)?
       ;

functionDeclaration: 
       'def' IDENTIFIER '(' parameterList* ')' '->' func_return_type statement_list;

parameterList: type IDENTIFIER (',' type IDENTIFIER)*;

functionCall: IDENTIFIER '(' argumentList* ')';

argumentList: expression (',' expression)*;

expressionList: expression (',' expression)*;

expressionStatement: expression;

returnStatement: 'return' expression;

expression: 
              augAssignment
            | logicalOrExpression
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
            multiplicativeExpression (('+' | '-') multiplicativeExpression)* 
          ;

multiplicativeExpression:
            unaryExpression (('*' | '/') unaryExpression)* 
          ;

unaryExpression:
          'not' primaryExpression
          | '-' primaryExpression
          | primaryExpression
          ;
          
primaryExpression:
            '(' expression ')'
          | functionCall
          | IDENTIFIER
          | INTEGER
          | DOUBLE
          | STRING
          | list
          | listIndexation
          | 'true'
          | 'false'
          | 'break'
          | 'continue'
          ;

list: '[' expressionList ']';

name: listIndexation | IDENTIFIER;

listIndexation: IDENTIFIER '[' expression ']';

augAssignment:
            name '+=' expression
          | name '-=' expression
          | name '*=' expression
          | name '/=' expression
          | name '%=' expression
          ;

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
INTEGER: [0-9]+;
DOUBLE: [0-9]+'.'[0-9]+;
STRING: '"' .*? '"';
COMMENT: '//' .*? '\n' -> skip; 
WS: [ \t\r\n]+ -> skip;
