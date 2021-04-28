%option noyywrap
%{
	int upper = 0;
	int lower = 0;
	int number = 0;
	int line = 0;
	int whitespace = 0;
	int punctuation = 0;
	int all = 0;
%}

%%
[A-Z]		{upper++;all++;}
[a-z]		{lower++;all++;}
[0-9]		{number++;all++;}
\n		{line++;all++;}
[ \t]		{whitespace++;all++;}
[\.!;\?:\,]	{punctuation++;all++;}
.		{all++;}
%%

int main(int argc, char *argv[])
{
	if (argc < 2) {
		printf("ERROR: missing file\n");
		printf("please use the Programm like this:\n");
		printf("./test.out <Filename>");
		return 0;
	} else if (argc > 2) {
		printf("EORROR: to many arguments supplied\n");
		printf("please use the Programm like this:\n");
		printf("./test.out <Filename>");
		return 0;
	}
	FILE *file;
	file = fopen(argv[1], "r");
	yyin = file;
	yylex();
	printf("upper case: %i \n", upper);
	printf("lower case: %i \n", lower);
	printf("numbers: %i \n", number);
	printf("lines: %i \n", line);
	printf("whitespaces: %i \n", whitespace);
	printf("punctuation marks: %i \n", punctuation);
	printf("all: %i \n", all);
	int x = all - upper - lower - number - line - whitespace - punctuation;
	printf("unrecognized: %i", x);
	return 0;
}
