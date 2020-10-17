import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def testcase_1(self):
        "Simple declaration"
        input = """Var: a = 0, c, d[2][3], e[2] = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,101))