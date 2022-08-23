import unittest
from dataclasses import dataclass
from tokens import token
import lexer


class TestLexer(unittest.TestCase):
    def test_next_token(self):
        @dataclass
        class TestCase:
            expected_type: token.TokenType
            expected_literal: str

        test_cases = [
            TestCase(expected_type=token.LPAREN, expected_literal="("),
            TestCase(expected_type=token.RPAREN, expected_literal=")"),
            TestCase(expected_type=token.LBRACE, expected_literal="{"),
            TestCase(expected_type=token.RBRACE, expected_literal="}"),
            TestCase(expected_type=token.SEMICOLON, expected_literal=";"),
            TestCase(expected_type=token.ASSIGN, expected_literal="="),
            TestCase(expected_type=token.EQUAL, expected_literal="=="),
            TestCase(expected_type=token.COMMA, expected_literal=","),
            TestCase(expected_type=token.FUNC, expected_literal="func"),
            TestCase(expected_type=token.VOID, expected_literal="void"),
            TestCase(expected_type=token.INSTANCE, expected_literal="instance"),
            TestCase(expected_type=token.C_INFO, expected_literal="C_INFO"),
            TestCase(expected_type=token.IDENTIFIER, expected_literal="it_is_identifier"),
            TestCase(expected_type=token.INT, expected_literal="1234"),
            TestCase(expected_type=token.TRUE, expected_literal="TRUE"),
            TestCase(expected_type=token.FALSE, expected_literal="FALSE"),
            TestCase(expected_type=token.STRING, expected_literal="\"string\""),
            TestCase(expected_type=token.IF, expected_literal="if"),
            TestCase(expected_type=token.COMMENT, expected_literal="//comment"),
            TestCase(expected_type=token.EOF, expected_literal=""),
        ]

        # GIVEN
        script = """
        ( ) { } ; = == , func void instance C_INFO it_is_identifier 1234 TRUE FALSE \"string\" if //comment
        """

        l = lexer.Lexer(script)

        for tc in test_cases:

            # WHEN
            tok = l.next_token()

            # THEN
            if tok.type != tc.expected_type:
                self.fail("wrong tokens type, got={}, expected={}".format(tok.type, tc.expected_type))

            if tok.literal != tc.expected_literal:
                self.fail("wrong tokens literal, got={}, expected={}".format(tok.literal, tc.expected_literal))

    def test_next_token_with_illegal_token(self):
        @dataclass
        class TestCase:
            expected_type: token.TokenType
            expected_literal: str

        test_case = TestCase(expected_type=token.ILLEGAL, expected_literal="!")

        # GIVEN
        script = """
        !
        """

        l = lexer.Lexer(script)

        # WHEN
        tok = l.next_token()

        # THEN
        if tok.type != test_case.expected_type:
            self.fail("wrong tokens type, got={}, expected={}".format(tok.type, test_case.expected_type))

        if tok.literal != test_case.expected_literal:
            self.fail("wrong tokens literal, got={}, expected={}".format(tok.literal, test_case.expected_literal))
