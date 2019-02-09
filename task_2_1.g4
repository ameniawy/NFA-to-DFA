grammar task_2_1;

start: (command newline)*;
command: COMMAND SPACE* (REG|MEMORY)? SPACE* COMMA? SPACE* (REG|IMMEDIATE|MEMORY)?;
newline: NEWLINE;

REG: ('AX' | 'BX' | 'CX' | 'DX');
COMMAND: 'AAA'|'ADD'|'INC';
IMMEDIATE: [a-zA-Z0-9]+;
MEMORY: '['REG']';
COMMA: ',' -> skip;
SPACE: ' ' -> skip;
NEWLINE: [\n\r]+ -> skip;
