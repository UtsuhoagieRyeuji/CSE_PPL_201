# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0286\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7\u00b5")
        buf.write("\n\7\f\7\16\7\u00b8\13\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\7\35\u0140\n\35\f\35\16\35\u0143\13\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\3>\3?\3?\3@\3@\7@\u01a2\n@\f@\16@\u01a5\13@\3@")
        buf.write("\7@\u01a8\n@\f@\16@\u01ab\13@\3@\3@\7@\u01af\n@\f@\16")
        buf.write("@\u01b2\13@\3@\7@\u01b5\n@\f@\16@\u01b8\13@\3@\3@\7@\u01bc")
        buf.write("\n@\f@\16@\u01bf\13@\3@\3@\7@\u01c3\n@\f@\16@\u01c6\13")
        buf.write("@\7@\u01c8\n@\f@\16@\u01cb\13@\7@\u01cd\n@\f@\16@\u01d0")
        buf.write("\13@\3@\7@\u01d3\n@\f@\16@\u01d6\13@\3@\3@\3A\3A\7A\u01dc")
        buf.write("\nA\fA\16A\u01df\13A\3A\3A\3A\3A\5A\u01e5\nA\3A\7A\u01e8")
        buf.write("\nA\fA\16A\u01eb\13A\3A\7A\u01ee\nA\fA\16A\u01f1\13A\3")
        buf.write("A\3A\7A\u01f5\nA\fA\16A\u01f8\13A\3A\3A\3A\3A\5A\u01fe")
        buf.write("\nA\3A\7A\u0201\nA\fA\16A\u0204\13A\7A\u0206\nA\fA\16")
        buf.write("A\u0209\13A\5A\u020b\nA\3A\3A\3B\3B\3B\7B\u0212\nB\fB")
        buf.write("\16B\u0215\13B\5B\u0217\nB\3C\3C\3C\7C\u021c\nC\fC\16")
        buf.write("C\u021f\13C\3D\3D\3D\7D\u0224\nD\fD\16D\u0227\13D\3E\3")
        buf.write("E\3E\3E\5E\u022d\nE\5E\u022f\nE\3F\3F\3G\5G\u0234\nG\3")
        buf.write("G\7G\u0237\nG\fG\16G\u023a\13G\3H\3H\5H\u023e\nH\3H\6")
        buf.write("H\u0241\nH\rH\16H\u0242\3I\3I\5I\u0247\nI\3I\5I\u024a")
        buf.write("\nI\3J\3J\5J\u024e\nJ\3K\3K\3L\3L\3L\3L\5L\u0256\nL\3")
        buf.write("M\3M\7M\u025a\nM\fM\16M\u025d\13M\3M\3M\3M\3N\6N\u0263")
        buf.write("\nN\rN\16N\u0264\3N\3N\3O\3O\3O\3P\3P\7P\u026e\nP\fP\16")
        buf.write("P\u0271\13P\3P\3P\3Q\3Q\3Q\3Q\5Q\u0279\nQ\3Q\3Q\3R\3R")
        buf.write("\3R\3R\3R\7R\u0282\nR\fR\16R\u0285\13R\3\u0141\2S\3\2")
        buf.write("\5\2\7\2\t\2\13\2\r\3\17\4\21\5\23\6\25\7\27\b\31\t\33")
        buf.write("\n\35\13\37\f!\r#\16%\17\'\20)\21+\22-\23/\24\61\25\63")
        buf.write("\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O")
        buf.write("$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u")
        buf.write("\67w8y9{:};\177<\u0081=\u0083\2\u0085\2\u0087\2\u0089")
        buf.write(">\u008b\2\u008d\2\u008f\2\u0091?\u0093@\u0095\2\u0097")
        buf.write("\2\u0099A\u009bB\u009dC\u009fD\u00a1E\u00a3F\3\2\24\3")
        buf.write("\2\62;\3\2\63;\3\2c|\3\2C\\\4\2--//\3\2\62\62\4\2ZZzz")
        buf.write("\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\4\2GGgg\5")
        buf.write("\2\n\13\16\17^^\4\2\f\f$$\5\2\13\f\16\17\"\"\7\2ddhhp")
        buf.write("pttvv\3\2,,\2\u02a7\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\3\u00a5\3\2\2")
        buf.write("\2\5\u00a7\3\2\2\2\7\u00a9\3\2\2\2\t\u00ab\3\2\2\2\13")
        buf.write("\u00ad\3\2\2\2\r\u00af\3\2\2\2\17\u00b9\3\2\2\2\21\u00be")
        buf.write("\3\2\2\2\23\u00c4\3\2\2\2\25\u00cd\3\2\2\2\27\u00d0\3")
        buf.write("\2\2\2\31\u00d5\3\2\2\2\33\u00dc\3\2\2\2\35\u00e4\3\2")
        buf.write("\2\2\37\u00ea\3\2\2\2!\u00f1\3\2\2\2#\u00fa\3\2\2\2%\u00fe")
        buf.write("\3\2\2\2\'\u0107\3\2\2\2)\u010a\3\2\2\2+\u0114\3\2\2\2")
        buf.write("-\u011b\3\2\2\2/\u0120\3\2\2\2\61\u0124\3\2\2\2\63\u012a")
        buf.write("\3\2\2\2\65\u012f\3\2\2\2\67\u0135\3\2\2\29\u013b\3\2")
        buf.write("\2\2;\u0149\3\2\2\2=\u014b\3\2\2\2?\u014e\3\2\2\2A\u0150")
        buf.write("\3\2\2\2C\u0153\3\2\2\2E\u0155\3\2\2\2G\u0158\3\2\2\2")
        buf.write("I\u015a\3\2\2\2K\u015d\3\2\2\2M\u015f\3\2\2\2O\u0161\3")
        buf.write("\2\2\2Q\u0164\3\2\2\2S\u0167\3\2\2\2U\u016a\3\2\2\2W\u016d")
        buf.write("\3\2\2\2Y\u016f\3\2\2\2[\u0171\3\2\2\2]\u0174\3\2\2\2")
        buf.write("_\u0177\3\2\2\2a\u017a\3\2\2\2c\u017d\3\2\2\2e\u0181\3")
        buf.write("\2\2\2g\u0185\3\2\2\2i\u0187\3\2\2\2k\u018b\3\2\2\2m\u018d")
        buf.write("\3\2\2\2o\u018f\3\2\2\2q\u0191\3\2\2\2s\u0193\3\2\2\2")
        buf.write("u\u0195\3\2\2\2w\u0197\3\2\2\2y\u0199\3\2\2\2{\u019b\3")
        buf.write("\2\2\2}\u019d\3\2\2\2\177\u019f\3\2\2\2\u0081\u01d9\3")
        buf.write("\2\2\2\u0083\u0216\3\2\2\2\u0085\u0218\3\2\2\2\u0087\u0220")
        buf.write("\3\2\2\2\u0089\u022e\3\2\2\2\u008b\u0230\3\2\2\2\u008d")
        buf.write("\u0233\3\2\2\2\u008f\u023b\3\2\2\2\u0091\u0244\3\2\2\2")
        buf.write("\u0093\u024d\3\2\2\2\u0095\u024f\3\2\2\2\u0097\u0255\3")
        buf.write("\2\2\2\u0099\u0257\3\2\2\2\u009b\u0262\3\2\2\2\u009d\u0268")
        buf.write("\3\2\2\2\u009f\u026b\3\2\2\2\u00a1\u0274\3\2\2\2\u00a3")
        buf.write("\u027c\3\2\2\2\u00a5\u00a6\t\2\2\2\u00a6\4\3\2\2\2\u00a7")
        buf.write("\u00a8\t\3\2\2\u00a8\6\3\2\2\2\u00a9\u00aa\t\4\2\2\u00aa")
        buf.write("\b\3\2\2\2\u00ab\u00ac\t\5\2\2\u00ac\n\3\2\2\2\u00ad\u00ae")
        buf.write("\t\6\2\2\u00ae\f\3\2\2\2\u00af\u00b6\5\7\4\2\u00b0\u00b5")
        buf.write("\5\7\4\2\u00b1\u00b5\5\t\5\2\u00b2\u00b5\7a\2\2\u00b3")
        buf.write("\u00b5\5\13\6\2\u00b4\u00b0\3\2\2\2\u00b4\u00b1\3\2\2")
        buf.write("\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8")
        buf.write("\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\16\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ba\7D\2\2\u00ba")
        buf.write("\u00bb\7q\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7{\2\2\u00bd")
        buf.write("\20\3\2\2\2\u00be\u00bf\7D\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write("\u00c1\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7m\2\2\u00c3")
        buf.write("\22\3\2\2\2\u00c4\u00c5\7E\2\2\u00c5\u00c6\7q\2\2\u00c6")
        buf.write("\u00c7\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7k\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\24\3\2\2\2\u00cd\u00ce\7F\2\2\u00ce\u00cf\7q\2\2\u00cf")
        buf.write("\26\3\2\2\2\u00d0\u00d1\7G\2\2\u00d1\u00d2\7n\2\2\u00d2")
        buf.write("\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\30\3\2\2\2\u00d5")
        buf.write("\u00d6\7G\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7u\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9\u00da\7K\2\2\u00da\u00db\7h\2\2\u00db")
        buf.write("\32\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de\7p\2\2\u00de")
        buf.write("\u00df\7f\2\2\u00df\u00e0\7D\2\2\u00e0\u00e1\7q\2\2\u00e1")
        buf.write("\u00e2\7f\2\2\u00e2\u00e3\7{\2\2\u00e3\34\3\2\2\2\u00e4")
        buf.write("\u00e5\7G\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7f\2\2\u00e7")
        buf.write("\u00e8\7K\2\2\u00e8\u00e9\7h\2\2\u00e9\36\3\2\2\2\u00ea")
        buf.write("\u00eb\7G\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7f\2\2\u00ed")
        buf.write("\u00ee\7H\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7t\2\2\u00f0")
        buf.write(" \3\2\2\2\u00f1\u00f2\7G\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7f\2\2\u00f4\u00f5\7Y\2\2\u00f5\u00f6\7j\2\2\u00f6")
        buf.write("\u00f7\7k\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7g\2\2\u00f9")
        buf.write("\"\3\2\2\2\u00fa\u00fb\7H\2\2\u00fb\u00fc\7q\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd$\3\2\2\2\u00fe\u00ff\7H\2\2\u00ff")
        buf.write("\u0100\7w\2\2\u0100\u0101\7p\2\2\u0101\u0102\7e\2\2\u0102")
        buf.write("\u0103\7v\2\2\u0103\u0104\7k\2\2\u0104\u0105\7q\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106&\3\2\2\2\u0107\u0108\7K\2\2\u0108")
        buf.write("\u0109\7h\2\2\u0109(\3\2\2\2\u010a\u010b\7R\2\2\u010b")
        buf.write("\u010c\7c\2\2\u010c\u010d\7t\2\2\u010d\u010e\7c\2\2\u010e")
        buf.write("\u010f\7o\2\2\u010f\u0110\7g\2\2\u0110\u0111\7v\2\2\u0111")
        buf.write("\u0112\7g\2\2\u0112\u0113\7t\2\2\u0113*\3\2\2\2\u0114")
        buf.write("\u0115\7T\2\2\u0115\u0116\7g\2\2\u0116\u0117\7v\2\2\u0117")
        buf.write("\u0118\7w\2\2\u0118\u0119\7t\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write(",\3\2\2\2\u011b\u011c\7V\2\2\u011c\u011d\7j\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e\u011f\7p\2\2\u011f.\3\2\2\2\u0120")
        buf.write("\u0121\7X\2\2\u0121\u0122\7c\2\2\u0122\u0123\7t\2\2\u0123")
        buf.write("\60\3\2\2\2\u0124\u0125\7Y\2\2\u0125\u0126\7j\2\2\u0126")
        buf.write("\u0127\7k\2\2\u0127\u0128\7n\2\2\u0128\u0129\7g\2\2\u0129")
        buf.write("\62\3\2\2\2\u012a\u012b\7V\2\2\u012b\u012c\7t\2\2\u012c")
        buf.write("\u012d\7w\2\2\u012d\u012e\7g\2\2\u012e\64\3\2\2\2\u012f")
        buf.write("\u0130\7H\2\2\u0130\u0131\7c\2\2\u0131\u0132\7n\2\2\u0132")
        buf.write("\u0133\7u\2\2\u0133\u0134\7g\2\2\u0134\66\3\2\2\2\u0135")
        buf.write("\u0136\7G\2\2\u0136\u0137\7p\2\2\u0137\u0138\7f\2\2\u0138")
        buf.write("\u0139\7F\2\2\u0139\u013a\7q\2\2\u013a8\3\2\2\2\u013b")
        buf.write("\u013c\7,\2\2\u013c\u013d\7,\2\2\u013d\u0141\3\2\2\2\u013e")
        buf.write("\u0140\13\2\2\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2")
        buf.write("\2\u0141\u0142\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144")
        buf.write("\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\7,\2\2\u0145")
        buf.write("\u0146\7,\2\2\u0146\u0147\3\2\2\2\u0147\u0148\b\35\2\2")
        buf.write("\u0148:\3\2\2\2\u0149\u014a\7-\2\2\u014a<\3\2\2\2\u014b")
        buf.write("\u014c\7-\2\2\u014c\u014d\7\60\2\2\u014d>\3\2\2\2\u014e")
        buf.write("\u014f\7/\2\2\u014f@\3\2\2\2\u0150\u0151\7/\2\2\u0151")
        buf.write("\u0152\7\60\2\2\u0152B\3\2\2\2\u0153\u0154\7,\2\2\u0154")
        buf.write("D\3\2\2\2\u0155\u0156\7,\2\2\u0156\u0157\7\60\2\2\u0157")
        buf.write("F\3\2\2\2\u0158\u0159\7^\2\2\u0159H\3\2\2\2\u015a\u015b")
        buf.write("\7^\2\2\u015b\u015c\7\60\2\2\u015cJ\3\2\2\2\u015d\u015e")
        buf.write("\7\'\2\2\u015eL\3\2\2\2\u015f\u0160\7#\2\2\u0160N\3\2")
        buf.write("\2\2\u0161\u0162\7(\2\2\u0162\u0163\7(\2\2\u0163P\3\2")
        buf.write("\2\2\u0164\u0165\7~\2\2\u0165\u0166\7~\2\2\u0166R\3\2")
        buf.write("\2\2\u0167\u0168\7?\2\2\u0168\u0169\7?\2\2\u0169T\3\2")
        buf.write("\2\2\u016a\u016b\7#\2\2\u016b\u016c\7?\2\2\u016cV\3\2")
        buf.write("\2\2\u016d\u016e\7@\2\2\u016eX\3\2\2\2\u016f\u0170\7>")
        buf.write("\2\2\u0170Z\3\2\2\2\u0171\u0172\7@\2\2\u0172\u0173\7?")
        buf.write("\2\2\u0173\\\3\2\2\2\u0174\u0175\7>\2\2\u0175\u0176\7")
        buf.write("?\2\2\u0176^\3\2\2\2\u0177\u0178\7@\2\2\u0178\u0179\7")
        buf.write("\60\2\2\u0179`\3\2\2\2\u017a\u017b\7>\2\2\u017b\u017c")
        buf.write("\7\60\2\2\u017cb\3\2\2\2\u017d\u017e\7@\2\2\u017e\u017f")
        buf.write("\7?\2\2\u017f\u0180\7\60\2\2\u0180d\3\2\2\2\u0181\u0182")
        buf.write("\7>\2\2\u0182\u0183\7?\2\2\u0183\u0184\7\60\2\2\u0184")
        buf.write("f\3\2\2\2\u0185\u0186\7?\2\2\u0186h\3\2\2\2\u0187\u0188")
        buf.write("\7?\2\2\u0188\u0189\7^\2\2\u0189\u018a\7?\2\2\u018aj\3")
        buf.write("\2\2\2\u018b\u018c\7*\2\2\u018cl\3\2\2\2\u018d\u018e\7")
        buf.write("+\2\2\u018en\3\2\2\2\u018f\u0190\7]\2\2\u0190p\3\2\2\2")
        buf.write("\u0191\u0192\7_\2\2\u0192r\3\2\2\2\u0193\u0194\7}\2\2")
        buf.write("\u0194t\3\2\2\2\u0195\u0196\7\177\2\2\u0196v\3\2\2\2\u0197")
        buf.write("\u0198\7=\2\2\u0198x\3\2\2\2\u0199\u019a\7<\2\2\u019a")
        buf.write("z\3\2\2\2\u019b\u019c\7.\2\2\u019c|\3\2\2\2\u019d\u019e")
        buf.write("\7\60\2\2\u019e~\3\2\2\2\u019f\u01a3\5s:\2\u01a0\u01a2")
        buf.write("\7\"\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01ce\3\2\2\2")
        buf.write("\u01a5\u01a3\3\2\2\2\u01a6\u01a8\7\"\2\2\u01a7\u01a6\3")
        buf.write("\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01b0\5\u0081A\2\u01ad\u01af\7\"\2\2\u01ae\u01ad\3\2")
        buf.write("\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01c9\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3")
        buf.write("\u01b5\7\"\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b9\3")
        buf.write("\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01bd\5{>\2\u01ba\u01bc")
        buf.write("\7\"\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01c0\u01c4\5\u0081A\2\u01c1\u01c3")
        buf.write("\7\"\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c8\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c7\u01b6\3\2\2\2\u01c8\u01cb\3")
        buf.write("\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cd")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01a9\3\2\2\2\u01cd")
        buf.write("\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d4\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d3\7")
        buf.write("\"\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6")
        buf.write("\u01d4\3\2\2\2\u01d7\u01d8\5u;\2\u01d8\u0080\3\2\2\2\u01d9")
        buf.write("\u020a\5s:\2\u01da\u01dc\7\"\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01e4\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e5\5")
        buf.write("\u0089E\2\u01e1\u01e5\5\u0091I\2\u01e2\u01e5\5\u0093J")
        buf.write("\2\u01e3\u01e5\5\u0099M\2\u01e4\u01e0\3\2\2\2\u01e4\u01e1")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e9\3\2\2\2\u01e6\u01e8\7\"\2\2\u01e7\u01e6\3\2\2\2")
        buf.write("\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3")
        buf.write("\2\2\2\u01ea\u0207\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ee")
        buf.write("\7\"\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f2\u01f6\5{>\2\u01f3\u01f5\7\"")
        buf.write("\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01fd\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f9\u01fe\5\u0089E\2\u01fa\u01fe\5\u0091")
        buf.write("I\2\u01fb\u01fe\5\u0093J\2\u01fc\u01fe\5\u0099M\2\u01fd")
        buf.write("\u01f9\3\2\2\2\u01fd\u01fa\3\2\2\2\u01fd\u01fb\3\2\2\2")
        buf.write("\u01fd\u01fc\3\2\2\2\u01fe\u0202\3\2\2\2\u01ff\u0201\7")
        buf.write("\"\2\2\u0200\u01ff\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0206\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0205\u01ef\3\2\2\2\u0206\u0209\3\2\2\2")
        buf.write("\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020b\3")
        buf.write("\2\2\2\u0209\u0207\3\2\2\2\u020a\u01dd\3\2\2\2\u020a\u020b")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020d\5u;\2\u020d\u0082")
        buf.write("\3\2\2\2\u020e\u0217\t\7\2\2\u020f\u0213\t\3\2\2\u0210")
        buf.write("\u0212\t\2\2\2\u0211\u0210\3\2\2\2\u0212\u0215\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0217\3")
        buf.write("\2\2\2\u0215\u0213\3\2\2\2\u0216\u020e\3\2\2\2\u0216\u020f")
        buf.write("\3\2\2\2\u0217\u0084\3\2\2\2\u0218\u0219\t\b\2\2\u0219")
        buf.write("\u021d\t\t\2\2\u021a\u021c\t\n\2\2\u021b\u021a\3\2\2\2")
        buf.write("\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3")
        buf.write("\2\2\2\u021e\u0086\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0221")
        buf.write("\t\13\2\2\u0221\u0225\t\f\2\2\u0222\u0224\t\r\2\2\u0223")
        buf.write("\u0222\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0223\3\2\2\2")
        buf.write("\u0225\u0226\3\2\2\2\u0226\u0088\3\2\2\2\u0227\u0225\3")
        buf.write("\2\2\2\u0228\u022f\5\u0083B\2\u0229\u022c\7\62\2\2\u022a")
        buf.write("\u022d\5\u0085C\2\u022b\u022d\5\u0087D\2\u022c\u022a\3")
        buf.write("\2\2\2\u022c\u022b\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u0228")
        buf.write("\3\2\2\2\u022e\u0229\3\2\2\2\u022f\u008a\3\2\2\2\u0230")
        buf.write("\u0231\5\u0083B\2\u0231\u008c\3\2\2\2\u0232\u0234\7\60")
        buf.write("\2\2\u0233\u0232\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0238")
        buf.write("\3\2\2\2\u0235\u0237\t\2\2\2\u0236\u0235\3\2\2\2\u0237")
        buf.write("\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239\3\2\2\2")
        buf.write("\u0239\u008e\3\2\2\2\u023a\u0238\3\2\2\2\u023b\u023d\t")
        buf.write("\16\2\2\u023c\u023e\t\6\2\2\u023d\u023c\3\2\2\2\u023d")
        buf.write("\u023e\3\2\2\2\u023e\u0240\3\2\2\2\u023f\u0241\t\2\2\2")
        buf.write("\u0240\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240\3")
        buf.write("\2\2\2\u0242\u0243\3\2\2\2\u0243\u0090\3\2\2\2\u0244\u0246")
        buf.write("\5\u008bF\2\u0245\u0247\5\u008dG\2\u0246\u0245\3\2\2\2")
        buf.write("\u0246\u0247\3\2\2\2\u0247\u0249\3\2\2\2\u0248\u024a\5")
        buf.write("\u008fH\2\u0249\u0248\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write("\u0092\3\2\2\2\u024b\u024e\5\63\32\2\u024c\u024e\5\65")
        buf.write("\33\2\u024d\u024b\3\2\2\2\u024d\u024c\3\2\2\2\u024e\u0094")
        buf.write("\3\2\2\2\u024f\u0250\t\17\2\2\u0250\u0096\3\2\2\2\u0251")
        buf.write("\u0256\n\20\2\2\u0252\u0256\5\u0095K\2\u0253\u0254\7)")
        buf.write("\2\2\u0254\u0256\7$\2\2\u0255\u0251\3\2\2\2\u0255\u0252")
        buf.write("\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0098\3\2\2\2\u0257")
        buf.write("\u025b\7$\2\2\u0258\u025a\5\u0097L\2\u0259\u0258\3\2\2")
        buf.write("\2\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c")
        buf.write("\3\2\2\2\u025c\u025e\3\2\2\2\u025d\u025b\3\2\2\2\u025e")
        buf.write("\u025f\7$\2\2\u025f\u0260\bM\3\2\u0260\u009a\3\2\2\2\u0261")
        buf.write("\u0263\t\21\2\2\u0262\u0261\3\2\2\2\u0263\u0264\3\2\2")
        buf.write("\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0266")
        buf.write("\3\2\2\2\u0266\u0267\bN\2\2\u0267\u009c\3\2\2\2\u0268")
        buf.write("\u0269\13\2\2\2\u0269\u026a\bO\4\2\u026a\u009e\3\2\2\2")
        buf.write("\u026b\u026f\7$\2\2\u026c\u026e\5\u0097L\2\u026d\u026c")
        buf.write("\3\2\2\2\u026e\u0271\3\2\2\2\u026f\u026d\3\2\2\2\u026f")
        buf.write("\u0270\3\2\2\2\u0270\u0272\3\2\2\2\u0271\u026f\3\2\2\2")
        buf.write("\u0272\u0273\bP\5\2\u0273\u00a0\3\2\2\2\u0274\u0278\5")
        buf.write("\u009fP\2\u0275\u0276\7^\2\2\u0276\u0279\n\22\2\2\u0277")
        buf.write("\u0279\7)\2\2\u0278\u0275\3\2\2\2\u0278\u0277\3\2\2\2")
        buf.write("\u0279\u027a\3\2\2\2\u027a\u027b\bQ\6\2\u027b\u00a2\3")
        buf.write("\2\2\2\u027c\u027d\7,\2\2\u027d\u027e\7,\2\2\u027e\u0283")
        buf.write("\3\2\2\2\u027f\u0280\n\23\2\2\u0280\u0282\n\23\2\2\u0281")
        buf.write("\u027f\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2\2")
        buf.write("\u0283\u0284\3\2\2\2\u0284\u00a4\3\2\2\2\u0285\u0283\3")
        buf.write("\2\2\2+\2\u00b4\u00b6\u0141\u01a3\u01a9\u01b0\u01b6\u01bd")
        buf.write("\u01c4\u01c9\u01ce\u01d4\u01dd\u01e4\u01e9\u01ef\u01f6")
        buf.write("\u01fd\u0202\u0207\u020a\u0213\u0216\u021d\u0225\u022c")
        buf.write("\u022e\u0233\u0238\u023d\u0242\u0246\u0249\u024d\u0255")
        buf.write("\u025b\u0264\u026f\u0278\u0283\7\b\2\2\3M\2\3O\3\3P\4")
        buf.write("\3Q\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    BODY = 2
    BREAK = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    ELSE_IF = 7
    END_BODY = 8
    END_IF = 9
    END_FOR = 10
    END_WHILE = 11
    FOR = 12
    FUNCTION = 13
    IF = 14
    PARAMETER = 15
    RETURN = 16
    THEN = 17
    VAR = 18
    WHILE = 19
    TRUE = 20
    FALSE = 21
    END_DO = 22
    COMMENT = 23
    ADD_INT = 24
    ADD_FLOAT = 25
    SUB_INT = 26
    SUB_FLOAT = 27
    MUL_INT = 28
    MUL_FLOAT = 29
    DIV_INT = 30
    DIV_FLOAT = 31
    MODULO = 32
    NOT = 33
    AND = 34
    OR = 35
    EQUAL_INT = 36
    UNEQUAL = 37
    LARGE_INT = 38
    SMALL_INT = 39
    LARGE_EQUAL_INT = 40
    SMALL_EQUAL_INT = 41
    LARGE_FLOAT = 42
    SMALL_FLOAT = 43
    LARGE_EQUAL_FLOAT = 44
    SMALL_EQUAL_FLOAT = 45
    ASSIGN = 46
    EQUAL_FLOAT = 47
    LP = 48
    RP = 49
    LQ = 50
    RQ = 51
    LB = 52
    RB = 53
    SEMI = 54
    COLON = 55
    COMMA = 56
    DOT = 57
    MULTI_ARRAYLIT = 58
    ARRAYLIT = 59
    INTLIT = 60
    FLOATLIT = 61
    BOOLEANLIT = 62
    STRINGLIT = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    UNTERMINATED_COMMENT = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'>.'", "'<.'", 
            "'>=.'", "'<=.'", "'='", "'=\\='", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "';'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSE_IF", 
            "END_BODY", "END_IF", "END_FOR", "END_WHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "END_DO", "COMMENT", "ADD_INT", "ADD_FLOAT", "SUB_INT", 
            "SUB_FLOAT", "MUL_INT", "MUL_FLOAT", "DIV_INT", "DIV_FLOAT", 
            "MODULO", "NOT", "AND", "OR", "EQUAL_INT", "UNEQUAL", "LARGE_INT", 
            "SMALL_INT", "LARGE_EQUAL_INT", "SMALL_EQUAL_INT", "LARGE_FLOAT", 
            "SMALL_FLOAT", "LARGE_EQUAL_FLOAT", "SMALL_EQUAL_FLOAT", "ASSIGN", 
            "EQUAL_FLOAT", "LP", "RP", "LQ", "RQ", "LB", "RB", "SEMI", "COLON", 
            "COMMA", "DOT", "MULTI_ARRAYLIT", "ARRAYLIT", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DIGIT", "NON_ZERO_DIGIT", "LOWER_CHAR", "UPPER_CHAR", 
                  "SIGN", "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSE_IF", "END_BODY", "END_IF", "END_FOR", "END_WHILE", 
                  "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                  "VAR", "WHILE", "TRUE", "FALSE", "END_DO", "COMMENT", 
                  "ADD_INT", "ADD_FLOAT", "SUB_INT", "SUB_FLOAT", "MUL_INT", 
                  "MUL_FLOAT", "DIV_INT", "DIV_FLOAT", "MODULO", "NOT", 
                  "AND", "OR", "EQUAL_INT", "UNEQUAL", "LARGE_INT", "SMALL_INT", 
                  "LARGE_EQUAL_INT", "SMALL_EQUAL_INT", "LARGE_FLOAT", "SMALL_FLOAT", 
                  "LARGE_EQUAL_FLOAT", "SMALL_EQUAL_FLOAT", "ASSIGN", "EQUAL_FLOAT", 
                  "LP", "RP", "LQ", "RQ", "LB", "RB", "SEMI", "COLON", "COMMA", 
                  "DOT", "MULTI_ARRAYLIT", "ARRAYLIT", "DEC", "HEX", "OCT", 
                  "INTLIT", "INT_PART", "DEC_PART", "EXP_PART", "FLOATLIT", 
                  "BOOLEANLIT", "SPEC_SEQUENCE", "STR_CHAR", "STRINGLIT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[75] = self.STRINGLIT_action 
            actions[77] = self.ERROR_CHAR_action 
            actions[78] = self.UNCLOSE_STRING_action 
            actions[79] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


