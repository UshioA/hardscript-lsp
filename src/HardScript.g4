grammar HardScript;

design: (component | binding)+;

component:
	kind = 'component' ID attributes? component_type? '{' element* '}'
	| kind = 'interface' ID attributes? ':' type = expression '{' element* '}';

component_type: ':' from = expression '->' to = expression;

attributes: '(' ID (',' ID)* ')';

element:
	binding										# BindingStatement
	| explicit_data_element						# DataInstantiation
	| 'auto' primary_symbol_list				# DataInstantiation
	| 'auto' expression							# MixedInstantiation
	| expression								# ComponentInstantiation
	| 'for' '(' iterator ')' '{' element* '}'	# Loop;

explicit_data_element:
	kind = 'wire' primary_symbol_list 'of' type = symbol
	| kind = 'bundle' primary_symbol_list 'of' type = symbol;

primary_symbol_list: primary_symbol (',' primary_symbol)*;

expression:
	symbol																					# SymbolExpr
	| number																				# NumberExpr
	| '[' list ']'																			# ListExpr
	| expression (selector)+																# AccessExpr
	| expression '.' primary_symbol															# FieldExpr
	| op = '#-' expression																	# UnaryExpr
	| expression op = '-#'																	# UnaryExpr
	| op = ('+' | '-' | '~' | '!') expression												# UnaryExpr
	| lhs = expression op = '**' rhs = expression											# BinaryExpr
	| lhs = expression op = ('*' | '/' | '%') rhs = expression								# BinaryExpr
	| lhs = expression op = ('+' | '-') rhs = expression									# BinaryExpr
	| lhs = expression op = ('>>' | '<<' | '>>>' | '<<<') rhs = expression					# BinaryExpr
	| lhs = expression op = ('<' | '<=' | '>' | '>=') rhs = expression						# BinaryExpr
	| lhs = expression op = ('==' | '!=') rhs = expression									# BinaryExpr
	| lhs = expression op = '&' rhs = expression											# BinaryExpr
	| lhs = expression op = ('^~' | '~^' | '^') rhs = expression							# BinaryExpr
	| lhs = expression op = '|' rhs = expression											# BinaryExpr
	| lhs = expression op = '&&' rhs = expression											# BinaryExpr
	| lhs = expression op = '||' rhs = expression											# BinaryExpr
	| lhs = expression op = '::' rhs = expression											# BinaryExpr
	| lhs = expression op = '<>' rhs = expression											# BinaryExpr
	| lhs = expression op = '<+>' rhs = expression											# BinaryExpr
	| 'if' cond = expression 'then' thenBranch = expression 'else' elseBranch = expression	#
		ConditionalExpr
	| '(' expression ')' # ParenExpr;

selector:
	'[' expression ']'								# BitSelector
	| '[' from = expression ':' to = expression ']'	# PartSelector;

list:
	expression (',' expression)*				# CommonList
	| from = expression '..' to = expression	# RangeList
	| expression '|' qualifier (',' qualifier)*	# ListComprehension
	|											# EmptyList;

qualifier:
	iterator			# Generator
	| 'when' expression	# Filter
	| binding			# LocalBinding;

iterator: primary_symbol 'in' expression;

binding: 'let' symbol '=' expression;

symbol:
	param_symbol		# ParamSymbol
	| primary_symbol	# PrimarySymbol;

primary_symbol:
	ID							# Identifier
	| ID (interpolation | ID)+	# Interpolated;

param_symbol:
	primary_symbol '(' expression (',' expression)* ')'
	| primary_symbol '(' ')';

interpolation: '$' '{' expression '}';

number:
	UNSIGNED_INTEGER	# IntNumber
	| BOOLEAN			# BoolNumber
	| BIN_NUMBER		# BitVectorNumber
	| HEX_NUMBER		# BitVectorNumber
	| OCT_NUMBER		# BitVectorNumber
	| DEC_NUMBER		# BitVectorNumber;

BOOLEAN: 'true' | 'false';

BIN_NUMBER: UNSIGNED_INTEGER '\'' [bB] [01] [01_]*;
HEX_NUMBER:
	UNSIGNED_INTEGER '\'' [hH] [0-9a-fA-F] [0-9a-fA-F_]*;
OCT_NUMBER: UNSIGNED_INTEGER '\'' [oO] [0-7] [0-7_]*;
DEC_NUMBER: UNSIGNED_INTEGER '\'' [dD] [0-9] [0-9_]*;

UNSIGNED_INTEGER: [0-9] [0-9_]*;

ID: [a-zA-Z_][a-zA-Z_0-9]*;

WHITE_SPACE: [ \t\r\n]+ -> skip;
COMMENT: '//' ~('\n')* '\n' -> skip;