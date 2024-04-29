grammar fresh;

program: function_list? main_function function_list? EOF;

function_list: function+;

main_function: 'def' 'main' '(' ')' 'None' '{' statements '}';

function: 'def' NAME '(' argument_list? ')' type (';' |'{' statements '}');

function_call: NAME '(' (expression (',' expression)*)? ')';

argument_list: argument (',' argument)*;

argument: NAME type;

statements: (statement WS?)+;

statement
    : if_statement
    | for_loop_statement
    | var_declaration 
    | print;

var_declaration
    : 'var' NAME type '=' expression ';' 
    | 'var' NAME type ';'
    | 'var' NAME '=' expression ';';

if_statement
    : 'if' '(' expression ')' '{' statements '}' ('elif' '(' expression ')' '{' statements '}')* ('else' '{' statements '}')?;

for_loop_statement
    : 'for' '(' type NAME '=' expression ';' expression ';' expression ')' '{' statements '}'
    | 'for' '(' type NAME 'in' NAME ')' '{' statements '}';

print: 'print' '(' expression_list ')' ';';

expression_list: expression (',' expression)*;

expression: or_expression;

or_expression: and_expression ( 'or' and_expression)*;

and_expression: eq_expression ( 'and' eq_expression)*;

eq_expression: rel_expression ( ('=='|'!=') rel_expression)*;

rel_expression: add_expression ( ('<'|'<='|'>'|'>=') add_expression)*;

add_expression: mul_expression ( ('+'|'-') mul_expression)*; 

mul_expression: un_expression ( ('*'|'/') un_expression)*;

un_expression: ('not'|'-') un_expression | ('not'|'-')? basic_expression | postfix_expression;

basic_expression
    : INTEGER 
    | DOUBLE 
    | STRING 
    | BOOL 
    | function_call 
    | '(' expression ')'
    | var_reference
    | compound_assignment;

compound_assignment: var_reference ('+=' | '-=' | '*=' | '/=') expression;

postfix_expression: basic_expression ( '++' | '--' )?;

var_reference: NAME;

type
    : 'int' 
    | 'float' 
    | 'bool' 
    | 'None' 
    | 'auto';

/* Terminals */
NAME: [a-zA-Z][a-zA-Z0-9]*;
INTEGER: [0-9]+;
DOUBLE: [0-9]+'.'[0-9]+;
BOOL: 'false' | 'true';
STRING: '"' .*? '"';
COMMENT: '//' .*? '\n' -> skip; 
WS: [ \t\r\n]+ -> skip;