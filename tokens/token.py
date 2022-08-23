from typing import NewType

TokenType = NewType('TokenType', str)


class Token:
    def __init__(self, type: TokenType, literal: str):
        self.type: TokenType = type
        self.literal: str = literal


def lookup_identifier(identifier: str):
    if identifier == INSTANCE or identifier == INSTANCE.lower():
        return INSTANCE
    elif identifier == C_INFO or identifier == C_INFO.lower():
        return C_INFO
    elif identifier == FUNC or identifier == FUNC.lower():
        return FUNC
    elif identifier == VOID or identifier == VOID.lower():
        return VOID
    elif identifier == IF or identifier == IF.lower():
        return IF
    elif identifier == TRUE or identifier == TRUE.lower():
        return TRUE
    elif identifier == FALSE or identifier == FALSE.lower():
        return FALSE
    else:
        return IDENTIFIER


# control
EOF = TokenType("EOF")
ILLEGAL = TokenType("ILLEGAL")

# delimiters
LPAREN = TokenType("LPAREN")
RPAREN = TokenType("RPAREN")
LBRACE = TokenType("LBRACE")
RBRACE = TokenType("RBRACE")
SEMICOLON = TokenType("SEMICOLON")
ASSIGN = TokenType("ASSIGN")
EQUAL = TokenType("EQUAL")
COMMA = TokenType("COMMA")
COMMENT = TokenType("COMMENT")

# types
INT = TokenType("INT")
STRING = TokenType("STRING")

# keywords
FUNC = TokenType("FUNC")
VOID = TokenType("VOID")
INSTANCE = TokenType("INSTANCE")
C_INFO = TokenType("C_INFO")
IDENTIFIER = TokenType("IDENTIFIER")
TRUE = TokenType("TRUE")
FALSE = TokenType("FALSE")
IF = TokenType("IF")
