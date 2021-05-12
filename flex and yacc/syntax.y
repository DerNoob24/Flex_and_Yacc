%{
    #include <stdio.h>
    int yylex();
    void yyerror(char *);
%}

%token INTEGER
%token STRING

%token LINE_END
%token IF
%token ELSE
%token WHILE
%token FOR

%token OR
%token AND

%token ASSIGNMENT

%token LOWER_CASE
%token UPPER_CASE
%token NUMBER

%token ROUND_START
%token ROUND_END

%token INVALID

%left	'+' '-'
%left	'*' '/'
%nonassoc	UMINUS

%%
program:        program expr '\n'           {printf("%d\n", $2);}
            |   ;

expr:           NUMBER                      { $$ = $1;}
            |   expr '+' expr          { $$ = $1 + $3;}
            |   expr '-' expr          { $$ = $1 - $3;}
            |   expr '*' expr          { $$ = $1 * $3;}
	    |   expr '/' expr	       { $$ = $1 / $3;}
            |   ROUND_START expr ROUND_END { $$ = ($2);}
	    |	'-' expr %prec UMINUS;

%%

void yyerror(char *s){ fprintf(stderr, "%s\n", s);}

int main(){
    yyparse();
    return 0;
}