%{
    #include "y.tab.h"
    #include <stdlib.h>
    int rows = 0;
    void yyerror(char *);
%}

%%
 /*Keywords*/
int         {return INTEGER;}

 /*Operators*/
=           {return ASSIGNMENT;}

 /*Other stuff*/
[0-9]+      {yylval = atoi(yytext);return NUMBER;}
-|\+|\*|;|\n|\r\n   {rows++;return *yytext;}


 /*Braces*/
\(          {return ROUND_START;}
\)          {return ROUND_END;}


.           {printf("Invalid Character");return INVALID;}
%%

int yywrap(){
    return 1;
}