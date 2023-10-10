## Group Members
- 121154 Curtis Thuranira
- 134788 Adrian Wanjau
- 135159 Eric Kabogo
- 135580 Elvis Rono
- 134442 Isaac Baimet
- 95007 John Kaburu
- 134678 Bridget Muthee

for question 1 we saved the file as lexical.py and question 2 is flex.py

### Logic Used:

1. The program first splits the input text into individual lines.
2. It defines a function is_comment that checks each line to determine whether it is a comment or not.
3. Inside the is_comment function:
- It strips leading and trailing whitespace from the line.
- It checks if the line starts with single-line comment markers (// or #) to identify single-line comments.
- It checks if the line starts with the beginning of multi-line comment markers (/* or ''') to identify multi-line comments.
- If a line starts a multi-line comment and does not end with the end marker (*/ or '''), it sets a flag to indicate that we are in the middle of a multi-line comment.
- If the line ends a multi-line comment (by having the end marker) while the flag indicates that we are in a multi-line comment, it clears the flag.
- If none of the above conditions match, the line is considered not a comment.
4. The program maintains a list in_multi_line_comment to keep track of whether it is currently inside a multi-line comment.
5. It iterates through each line and calls the is_comment function to determine whether each line is a comment or not.
6. Based on the result, it prints whether each line is a comment or not.

### Importance of Lexical and Syntax Analysis Concepts:

#### Lexical Analysis
Lexical analysis involves breaking down the input into tokens or lexemes. In this program, we perform a simplified form of lexical analysis when we check each line to identify comment markers (//, #, /*, '''). Although we are not parsing the entire program structure, understanding tokenization and patterns is crucial for this task.
#### Syntax Analysis
Syntax analysis typically deals with the hierarchical structure of a program. In this program, we are not performing full syntax analysis since we are only identifying individual lines as comments or not. However, concepts of context and structure are indirectly involved, as we need to consider the context of each line and whether it forms a valid comment or not based on patterns and delimiters.

## Question 2
To use this Flex lexer:
- run the following command:
```
flex -o identifier_lexer.c flex_lexer.l                                                    
gcc -o flex_lexer identifier_lexer.c -lfl
```
- Run the lexer with your input:
```
./flex_lexer
```
