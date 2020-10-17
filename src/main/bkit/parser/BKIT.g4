// MSSV: 1810814
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

// Parser
program                        : var_declaration_stmt* func_declaration* EOF; 
var_declaration_stmt           : VAR COLON var_list SEMI;
var_list                       : (variable (ASSIGN literal)? (COMMA variable (ASSIGN literal)?)*);    //toi ve coi
func_declaration               : FUNCTION COLON ID (PARAMETER COLON para_list)? func_body;
para_list                      : para (COMMA para)*;
para                           : ID | index_expression;
index_expression               : ID (LQ INTLIT RQ)+;
func_body                      : BODY COLON (var_declaration_stmt)* stmt_list END_BODY DOT;
stmt_list                      : (assign_stmt
                               | if_stmt 
                               | for_stmt 
                               | while_stmt 
                               | do_while_stmt 
                               | break_stmt 
                               | continue_stmt 
                               | call_stmt 
                               | return_stmt)*;
assign_stmt                    : variable ASSIGN expression SEMI;
if_stmt                        : IF expression THEN stmt_list (ELSE_IF expression THEN stmt_list)* (ELSE stmt_list)? END_IF DOT;
for_stmt                       : FOR LP ID ASSIGN expression COMMA expression COMMA expression RP DO stmt_list END_FOR DOT;
while_stmt                     : WHILE expression DO stmt_list END_WHILE DOT;
do_while_stmt                  : DO stmt_list WHILE expression END_DO DOT;
break_stmt                     : BREAK SEMI;
continue_stmt                  : CONTINUE SEMI;
call_stmt                      : ID LP para_func_list RP SEMI;
para_func_list                 : (expression (COMMA expression)*)?;
return_stmt                    : RETURN expression? SEMI;
expression                     : relational_exp | non_relational_exp;
relational_exp                 : non_relational_exp relational_ope non_relational_exp;
relational_ope                 : EQUAL_INT | UNEQUAL | SMALL_INT | LARGE_INT | SMALL_EQUAL_INT | LARGE_EQUAL_INT 
                               | EQUAL_FLOAT | SMALL_FLOAT | LARGE_FLOAT | SMALL_EQUAL_FLOAT | LARGE_EQUAL_FLOAT;
non_relational_exp             : non_relational_exp (AND | OR) exp1 | exp1;
exp1                           : exp1 (ADD_INT | ADD_FLOAT | SUB_INT | SUB_FLOAT) exp2 | exp2;
exp2                           : exp2 (MUL_INT | MUL_FLOAT | DIV_INT | DIV_FLOAT | MODULO) exp3 | exp3;
exp3                           : NOT exp3 | exp4;
exp4                           : (SUB_INT | SUB_FLOAT) exp4 | exp5;
exp5                           : LQ (exp5 | exp6) RQ | exp6;
exp6                           : ID LP argument_list RP | exp7;
argument_list                  : (ID (COMMA ID)*)?;
exp7                           : ID | INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | ARRAYLIT | LP expression RP;
variable                       : ID | ID (LQ INTLIT RQ)+ (ASSIGN ARRAYLIT)?;
literal                        : INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | MULTI_ARRAYLIT | ARRAYLIT;

// Lexer
//TOKENS SET
fragment DIGIT          : [0-9];
fragment NON_ZERO_DIGIT : [1-9];
fragment LOWER_CHAR     : [a-z];
fragment UPPER_CHAR     : [A-Z];
fragment SIGN           : [+-];

//Identifiers
ID                  : LOWER_CHAR(LOWER_CHAR | UPPER_CHAR | '_' | SIGN)*;

//Keywords
BODY                : 'Body';
BREAK               : 'Break';
CONTINUE            : 'Continue';
DO                  : 'Do';
ELSE                : 'Else';
ELSE_IF             : 'ElseIf';
END_BODY            : 'EndBody';
END_IF              : 'EndIf';
END_FOR             : 'EndFor';
END_WHILE           : 'EndWhile';
FOR                 : 'For';
FUNCTION            : 'Function';
IF                  : 'If';
PARAMETER           : 'Parameter';
RETURN              : 'Return';
THEN                : 'Then';
VAR                 : 'Var';
WHILE               : 'While';
TRUE                : 'True';
FALSE               : 'False';
END_DO              : 'EndDo';
COMMENT             : '**'.*?'**'-> skip;

//Operators
ADD_INT             : '+';
ADD_FLOAT           : '+.';
SUB_INT             : '-';
SUB_FLOAT           : '-.';
MUL_INT             : '*';
MUL_FLOAT           : '*.';
DIV_INT             : '\\';
DIV_FLOAT           : '\\.';
MODULO              : '%';
NOT                 : '!';
AND                 : '&&';
OR                  : '||';
EQUAL_INT           : '==';
UNEQUAL             : '!=';
LARGE_INT           : '>';
SMALL_INT           : '<';
LARGE_EQUAL_INT     : '>=';
SMALL_EQUAL_INT     : '<=';
LARGE_FLOAT         : '>.';
SMALL_FLOAT         : '<.';
LARGE_EQUAL_FLOAT   : '>=.';
SMALL_EQUAL_FLOAT   : '<=.';
ASSIGN              : '=';
EQUAL_FLOAT         : '=\\=';

//Separators
LP                  : '(';
RP                  : ')';
LQ                  : '[';
RQ                  : ']';
LB                  : '{';
RB                  : '}';
SEMI                : ';';
COLON               : ':';
COMMA               : ',';
DOT                 : '.';

//Literals
MULTI_ARRAYLIT      : LB ' '* (' '* ARRAYLIT ' '* (' '* COMMA ' '* ARRAYLIT ' '*)*)* ' '* RB;
ARRAYLIT            : LB (' '* (INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT) ' '* (' '* COMMA ' '* (INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT) ' '*)*)? RB;
fragment DEC        : [0] | [1-9][0-9]*;
fragment HEX        : [xX][1-9A-F][0-9A-F]*;
fragment OCT        : [oO][1-7][0-7]*;
INTLIT              : DEC | '0'(HEX | OCT);

fragment INT_PART   : DEC;
fragment DEC_PART   : '.'?[0-9]*;
fragment EXP_PART   : [eE][+-]?[0-9]+;
FLOATLIT            : INT_PART DEC_PART? EXP_PART?;
BOOLEANLIT          : TRUE | FALSE;
fragment SPEC_SEQUENCE : [\b\f\r\t\\];
fragment STR_CHAR      : (~[\n"] | SPEC_SEQUENCE | '\'"'); 
STRINGLIT              : '"'STR_CHAR*'"' {
        y = str(self.text)
        self.text = y[1:-1]
};
WS                  : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{
    raise ErrorToken(self.text)
};
UNCLOSE_STRING: '"'STR_CHAR*{
    raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: UNCLOSE_STRING ('\\' ~[nrbtf] | '\''){
    raise IllegalEscape(self.text[1:])
};
UNTERMINATED_COMMENT: '**' (~('*')~('*'))*;