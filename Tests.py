import lexical as lex
import unittest


class TestDataAssignment(unittest.TestCase):    
    def test_BoolTrueOrFalse(self):
        lexer=lex.getLexer()
        lexer.input("True true False false")
        self.assertEqual(lexer.token().type,"BOOL")
        self.assertNotEqual(lexer.token().type,"BOOL")
        self.assertEqual(lexer.token().type,"BOOL")
        self.assertNotEqual(lexer.token().type,"BOOL")

    def test_HexRead(self):
        lexer=lex.getLexer()
        lexer.input("0x23f 23f")
        self.assertEqual(lexer.token().type,"HEX")
        self.assertNotEqual(lexer.token().type,"HEX")

    def test_HexOnlyAtoF(self):
        lexer=lex.getLexer()
        lexer.input("0x23g")
        self.assertEqual(lexer.token().value,"0x23")

    def test_HexMustHaveVal(self):
        lexer=lex.getLexer()
        lexer.input("0x")
        self.assertNotEqual(lexer.token().type,"HEX")

    def test_FloatRead(self):
        lexer=lex.getLexer()
        lexer.input("12.0 a")
        self.assertEqual(lexer.token().type,"FLOAT")
        self.assertNotEqual(lexer.token().type,"FLOAT")

    def test_FloatisnotInt(self):
        lexer=lex.getLexer()
        lexer.input("12")
        self.assertNotEqual(lexer.token().type,"FLOAT")

    def test_IntRead(self):
        lexer=lex.getLexer()
        lexer.input("12 a")
        self.assertEqual(lexer.token().type,"INT")
        self.assertNotEqual(lexer.token().type,"INT")

    def test_IntisnotFloat(self):
        lexer=lex.getLexer()
        lexer.input("-12.0")
        self.assertNotEqual(lexer.token().type,"INT")

    def test_CharRead(self):
        lexer=lex.getLexer()
        lexer.input("'a' a")
        self.assertEqual(lexer.token().type,"CHAR")
        self.assertNotEqual(lexer.token().type,"CHAR")

    def test_CharifSingleQuoteOnly(self):
        lexer=lex.getLexer()
        lexer.input(""" 'a' "a" """)
        self.assertEqual(lexer.token().type,"CHAR")
        self.assertNotEqual(lexer.token().type,"CHAR")

    def test_StringRead(self):
        lexer=lex.getLexer()
        lexer.input("\"test\" 'a' ")
        self.assertEqual(lexer.token().type,"STRING")
        self.assertNotEqual(lexer.token().type,"STRING")

    def test_StringifDoubleQuoteOnly(self):
        lexer=lex.getLexer()
        lexer.input("\"a\" 'a'")
        self.assertEqual(lexer.token().type,"STRING")
        self.assertNotEqual(lexer.token().type,"STRING")

    def test_StringcanHaveNumbersAndSymbols(self):
        lexer=lex.getLexer()
        lexer.input("\"-12.0 5\"")
        self.assertEqual(lexer.token().type,"STRING")

    def test_CommentIgnoredUntilNewLine(self):
        lexer=lex.getLexer()
        lexer.input("#this should not exist\n\"This Should\"")
        self.assertEqual(lexer.token().type,"STRING")

if __name__ == '__main__':
    unittest.main()
    
