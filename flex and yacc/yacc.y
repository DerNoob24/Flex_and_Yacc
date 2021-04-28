%{
    #include <stdio.h>
    int yylex();
    void yyerror(char *);
%}

%token INTEGER

%token ASSIGNMENT

%token NUMBER
%token LINE_END

%token ROUND_START
%token ROUND_END

%token INVALID

%%
program:        program expr '\n'           {printf("%d\n", $2);}
            |   ;

expr:           NUMBER                      { $$ = $1;}
            |   expr '+' expr          { $$ = $1 + $3;}
            |   expr '-' expr          { $$ = $1 - $3;}
            |   expr '*' expr          { $$ = $1 * $3;}
            |   ROUND_START expr ROUND_END { $$ = ($2);};

%%

void yyerror(char *s){ fprintf(stderr, "%s\n", s);}

int main(){
    yyparse();
    return 0;
}