import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_identifier(self):
        """test legal identifier"""
        self.assertTrue(TestLexer.checkLexeme("Var: x","Var,:,x,<EOF>", 1))
    
    def test_float(self):
        """test legal float"""
        self.assertTrue(TestLexer.checkLexeme("Var: a = 0XABCD;","Var,:,a,=,0XABCD,;,<EOF>", 2))
    
    def test_wrong_format_float(self):
        """test wrong format float"""
        self.assertTrue(TestLexer.checkLexeme("Var: c, d = 6, e, f;","Var,:,c,,,d,=,6,,,e,,,f,;,<EOF>", 3))

    def testcase_4(self):
        "successfull return tokens"
        self.assertTrue(TestLexer.checkLexeme("Var: b[2][3] = {{2,3,4},{4,5,6}};","Var,:,b,[,2,],[,3,],=,{{2,3,4},{4,5,6}},;,<EOF>", 4))
    
    def testcase_5(self):
        "successfull return tokens"
        self.assertTrue(TestLexer.checkLexeme("0 199 0xFF 0XABC 0o567 0O77","0,199,0xFF,0XABC,0o567,0O77,<EOF>", 5))

    def testcase_6(self):
        "test legal float number"
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12000.120000e-1","12.0e3,12e3,12.e5,12.0e3,12000.120000e-1,<EOF>", 6))
    
    def testcase_7(self):
        "test legal float number"
        self.assertTrue(TestLexer.checkLexeme("0x0 0o0","0,x,0,0,o,0,<EOF>", 7))
    
    def testcase_8(self):
        "test valid comment"
        self.assertTrue(TestLexer.checkLexeme("**This is a valid comment**","<EOF>",8))

    def testcase_9(self):
        "test valid comment"
        self.assertTrue(TestLexer.checkLexeme("**This is a valid comment\n*Line1\n*Line2\n**","<EOF>",9))
    
    def testcase_10(self):
        "test valid comment"
        self.assertTrue(TestLexer.checkLexeme("****\n Var: x = 5;","Var,:,x,=,5,;,<EOF>",10))

    def testcase_11(self):
        "test valid string"
        self.assertTrue(TestLexer.checkLexeme("\"*This is a valid string*\t\"","*This is a valid string*\t,<EOF>",11))

    def testcase_12(self):
        "test valid string"
        self.assertTrue(TestLexer.checkLexeme("\"He asked me: '\"Where is John?'\"\"","He asked me: '\"Where is John?'\",<EOF>",12))

    def testcase_13(self):
        "test array literal"
        self.assertTrue(TestLexer.checkLexeme("1230.e5{{1 ,  2,3  }}","1230.e5,{{1 ,  2,3  }},<EOF>",13))
    
    def testcase_14(self):
        "test mix character literal"
        self.assertTrue(TestLexer.checkLexeme("\"Principle of programming language\"0x0x123{{{1,2,3}}","Principle of programming language,0,x,0x123,{,{{1,2,3}},<EOF>",14))

    def testcase_15(self):
        "test array literal"
        self.assertTrue(TestLexer.checkLexeme("{\"What's is PPL?\",{1,2,3},0x123,0O77}","{,What's is PPL?,,,{1,2,3},,,0x123,,,0O77,},<EOF>",15))
    
    def testcase_16(self):
        "test array of strings literal"
        self.assertTrue(TestLexer.checkLexeme("{\"string1\",\"string2\",\"string3\"}","{\"string1\",\"string2\",\"string3\"},<EOF>",16))

    def testcase_17(self):
        "test literal"
        self.assertTrue(TestLexer.checkLexeme("\"This is a string contain intlit 1xABC and floatlit 77.e31\"","This is a string contain intlit 1xABC and floatlit 77.e31,<EOF>",17))

    def testcase_18(self):
        "test comment"
        self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",18))

    def testcase_19(self):
        "test comment"
        self.assertTrue(TestLexer.checkLexeme("*** **","<EOF>",19))

    def testcase_20(self):
        "illegal comment"
        self.assertTrue(TestLexer.checkLexeme("**This is an invalid comment*","Unterminated Comment",20))

    def testcase_21(self):
        "string check"
        self.assertTrue(TestLexer.checkLexeme("\"I asked: \'Why? \' \"","I asked: \'Why? \' ,<EOF>",21))
    
    def testcase_22(self):
        "string check"
        self.assertTrue(TestLexer.checkLexeme(r""" "Cause you are \n such a \r good \b boy" """,r"Cause you are \n such a \r good \b boy,<EOF>",22))

    def testcase_23(self):
        "unclose string"
        self.assertTrue(TestLexer.checkLexeme("\"This is an unclosed string","Unclosed String: This is an unclosed string",23))

    def testcase_24(self):
        "string check"
        self.assertTrue(TestLexer.checkLexeme("0x1234myID\"Today is ** sunny\"**Begin comment\n*Line1\n*Line2\n**","0x1234,myID,Today is ** sunny,<EOF>",24))
    def testcase_25(self):
        "check float number"
        self.assertTrue(TestLexer.checkLexeme("10.","10.,<EOF>",25))
    
    