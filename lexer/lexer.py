import re
from tokens import token


def new_token(token_type: token.TokenType, literal: str):
    return token.Token(token_type, literal)


def is_letter(character: str):
    pattern = re.compile("[A-Za-z0-9_.]+")
    if pattern.fullmatch(character) is not None:
        return True
    else:
        return False


def is_digit(character: str):
    return character.isdigit()


def is_not_quote(character: str):
    return character != "\""


def is_end_of_line(character: str):
    return character != '\n'


def is_eof(character: str):
    return character is None


class Lexer:
    def __init__(self, input):
        self.input: str = input
        self.position: int = 0
        self.read_position: int = 0
        self.current_character: str = None

        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.current_character = None
        else:
            self.current_character = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def read_string(self):
        pos = self.position

        # read opening quote
        self.read_char()

        # read characters in between quotes
        while is_not_quote(self.current_character):
            self.read_char()

        # read ending quote
        self.read_char()
        return self.input[pos:self.position]

    def read_to_the_end_of_line(self):
        pos = self.position
        while is_end_of_line(self.current_character):
            self.read_char()
        return self.input[pos:self.position]

    def read_identifier(self):
        pos = self.position
        while is_letter(self.current_character):
            self.read_char()
        return self.input[pos:self.position]

    def peek_character(self):
        if self.read_position >= len(self.input):
            return 0
        return self.input[self.read_position]

    def read_number(self):
        pos = self.position
        while is_digit(self.current_character):
            self.read_char()
        return self.input[pos:self.position]

    def skip_whitespace(self):
        while self.current_character == ' ' or self.current_character == '\t' or self.current_character == '\n' or self.current_character == '\r':
            self.read_char()

    def next_token(self):
        tok: token.Token

        self.skip_whitespace()

        if self.current_character == ";":
            tok = new_token(token.SEMICOLON, self.current_character)
        elif self.current_character == "(":
            tok = new_token(token.LPAREN, self.current_character)
        elif self.current_character == ")":
            tok = new_token(token.RPAREN, self.current_character)
        elif self.current_character == "{":
            tok = new_token(token.LBRACE, self.current_character)
        elif self.current_character == "}":
            tok = new_token(token.RBRACE, self.current_character)
        elif self.current_character == ",":
            tok = new_token(token.COMMA, self.current_character)
        elif self.current_character == "/":
            if self.peek_character() == "/":
                token_literal = self.read_to_the_end_of_line()
                tok = new_token(token.COMMENT, token_literal)
            else:
                tok = new_token(token.ILLEGAL, self.current_character)
        elif self.current_character == "=":
            if self.peek_character() == "=":
                character = self.current_character
                self.read_char()
                literal = character + self.current_character
                tok = new_token(token.EQUAL, literal)
            else:
                tok = new_token(token.ASSIGN, self.current_character)
        else:
            if self.current_character == "\"":
                token_literal = self.read_string()
                tok = new_token(token.STRING, token_literal)
                return tok
            elif is_eof(self.current_character):
                tok = new_token(token.EOF, "")
                return tok
            elif is_digit(self.current_character):
                token_literal = self.read_number()
                tok = new_token(token.INT, token_literal)
                return tok
            elif is_letter(self.current_character):
                token_literal = self.read_identifier()
                token_type = token.lookup_identifier(token_literal)
                tok = new_token(token_type, token_literal)
                return tok
            else:
                tok = new_token(token.ILLEGAL, self.current_character)

        self.read_char()
        return tok
