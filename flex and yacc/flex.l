%{
    #include "y.tab.h"
    #include <stdlib.h>
    int	rows = 0;
    void yyerror(char *);
%}

%%

int		{return INTEGER;}
str		{return STRING;}

if		{return IF;}
else		{return ELSE;}
while		{return WHILE;}
for		{return FOR;}
\|\|		{return OR;}
&&		{return AND;}


=		{return AS;}

[a-z]+		{yylval = atoi(yytext);printf("letter");return LOWER_CASE;}
[A-Z]+		{yylval = atoi(yytext);return UPPER_CASE;}
[0-9]+		{yylval = atoi(yytext);return NUMBER;}
-|\+|\*|\/|;|\n		{rows++;return *yytext;}
[ \t]		; //skip whitespaces


\(		{return ROUND_START;}
\)		{return ROUND_END;}

.		{printf("Invalid Character");return	INVALID;}

"/""*"(.|\n)*"*""/"	{printf("multiline Comment\n");}
%%

int yywrap(){ return 0; }