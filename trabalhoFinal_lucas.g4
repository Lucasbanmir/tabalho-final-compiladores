grammar trabalhoFinal_lucas;

prog: decVarConst* decFunc* main
    ;
decVarConst: tipo listaIds ';' #decVar
    | 'const' tipo listaAtrib ';' #decConst
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
decFunc: (tipo|'void')? ID '(' parametros ')' '{' funcBloco '}' #decFuncao
    ;
parametros: (tipo ID (',' tipo ID)*)?
    ;
main: 'main' '(' parametros ')' '{' funcBloco '}'
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
comandosLoop: (comandos | break | 'if' '(' expr ')' '{' (comandos | break)+ '}' ('else' '{' (comandos | break)+ '}')? )+
    ;
break: 'break' ';'
    ;
print: 'print' '(' expr (',' expr)* ')' ';' #decPrint
    ;
input: 'input' '(' listaIds ')' ';' #decInput
    ;
for returns [idx]: 'for' '(' ID '=' fator ';' expr ';' ID '=' expr ')' '{' comandosLoop '}'
    ;
while: 'while' '(' expr ')' '{' comandosLoop '}'
    ;
return: 'return' expr? ';'
    ;
atribuicao: ID '=' expr ';' #decAtrib
    ;
callFunc: ID '(' (expr (',' expr)*)? ')' ';'
    ;
expr returns [type, inh_type]: expr or termo #orOp
    | termo #passTermo
    ;
termo returns [type]: termo and termo2 #andOp
    | termo2 #passTermo2
    ;
termo2 returns [type]: termo2 comp termo3 #compOp
    | termo3 #passTermo3
    ;
termo3 returns [type]: termo3 equal termo4 #equalOp
    | termo4 #passTermo4
    ;
termo4 returns [type]: termo4 addMinus termo5 #addMinusOp
    | termo5 #passTermo5
    ;
termo5 returns [type]: termo5 multiDiv termo6 #multiDivOp
    | termo6 #passTermo6
    ;
termo6 returns [type]: minusUni termo6 #minusUniOp
    | termo7 #passTermo7
    ;
termo7 returns [type]: not termo7 #notOp
    | fator #passFator
    ;
fator returns [type]: '(' expr ')' #parenExprFat
    | ID #idFat
    | dado #dadoFat
    | callFunc #callFuncaoFat
    ;
dado returns [type]: INT #intDado
    | REAL #realDado
    | STRING #stringDado
    | BOOL #boolDado
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
VOID: 'void';
INT: [0-9]+;
BOOL: 'TRUE' | 'FALSE';
REAL: [0-9]+.[0-9]+;
STRING: '"' .*? '"';
ID: [a-zA-Z]([a-zA-Z0-9]*);
WS: [ \t\r\n]+ -> skip ;
COMMENT1: '//' .*? '\n' -> skip;
COMMENT2: '/*' .*? '*/' -> skip;