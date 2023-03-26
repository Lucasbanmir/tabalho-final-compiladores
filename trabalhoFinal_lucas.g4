grammar trabalhoFinal_lucas;

prog: decVarConst* decFunc* main
    ;
decVarConst: tipo listaIds ';'
    | 'const' tipo listaAtrib ';'
    ;
tipo: 'int'
    | 'real'
    | 'bool'
    | 'String'
    ;
listaIds: ID (',' ID)*
    ;
listaAtrib: atrib (',' atrib)*
    ;
atrib: ID '=' dado
    ;
funcBloco: decVarConst* comandos+
    ;
decFunc: (tipo|'void')? ID '(' (tipo ID (',' tipo ID)*)? ')' '{' funcBloco '}'
    ;
main: 'main' '(' ')' '{' funcBloco '}'
    ;
comandos: print
    |input
    |for
    |'if' '(' expr ')' '{' comandos+ '}' ('else' '{' comandos+ '}')?
    |while
    |return
    |atribuicao
    |callFunc
    ;
comandosLoop:
    |comandos
    |'break'
    |'if' '(' expr ')' '{' (comandos | 'break')+ '}' ('else' '{' (comandos | 'break')+ '}')?
    ;
print: 'print' '(' expr (',' expr)* ')' ';'
    ;
input: 'input' '(' listaIds ')' ';'
    ;
for: 'for' '(' atrib ';' expr ';' expr ')' '{' comandosLoop '}' ';'
    ;
while: 'while' '(' expr ')' '{' comandosLoop '}'
    ;
return: 'return' expr? ';'
    ;
atribuicao: ID '=' expr ';'
    ;
callFunc: ID '(' (expr (',' expr)*)? ')'
    ;
expr: expr or termo
    | termo
    ;
termo: termo and termo2
    | termo2
    ;
termo2: termo2 comp termo3
    | termo3
    ;
termo3: termo3 equal termo4
    | termo4
    ;
termo4: termo4 addMinus termo5
    | termo5
    ;
termo5: termo5 multiDiv termo6
    | termo6
    ;
termo6: minusUni termo6
    | termo7
    ;
termo7: not termo7
    | fator
    ;
fator: '(' expr ')'
    | ID
    | dado
    | callFunc
    ;
dado: INT
    | REAL
    | STRING
    | BOOL
    ;
not: '!'
    ;
minusUni: '-'
    ;
multiDiv: '*'
    |'/'
    ;
addMinus: '+'
    |'-'
    ;
equal: '=='
    |'!='
    ;
comp: '>='
    |'<='
    |'>'
    |'<'
    ;
and: '&&'
    ;
or: '||'
    ;

// Regras lexicas
INT: [0-9]+;
BOOL: 'TRUE' | 'FALSE';
REAL: [0-9]+.[0-9]+;
STRING: '"' .*? '"';
ID: [a-zA-Z]([a-zA-Z0-9]*);
WS: [ \t\r\n]+ -> skip ;
COMMENT1: '//' .*? '\n' -> skip;
COMMENT2: '/*' .*? '*/' -> skip;