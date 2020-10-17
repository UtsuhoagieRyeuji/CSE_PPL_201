# Generated from d:\BK\201\PPL\Assignment\Assignment1\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u027f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\7\b\u00be\n\b\f\b\16\b\u00c1\13")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\7\36\u0149\n\36\f\36\16\36\u014c\13\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*")
        buf.write("\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3@\3@\3A\3A\3A\7A\u01ac\nA\fA\16A\u01af\13A\5A\u01b1")
        buf.write("\nA\3B\3B\3B\7B\u01b6\nB\fB\16B\u01b9\13B\3C\3C\3C\7C")
        buf.write("\u01be\nC\fC\16C\u01c1\13C\3D\3D\3D\3D\5D\u01c7\nD\5D")
        buf.write("\u01c9\nD\3E\3E\3F\5F\u01ce\nF\3F\7F\u01d1\nF\fF\16F\u01d4")
        buf.write("\13F\3G\3G\5G\u01d8\nG\3G\6G\u01db\nG\rG\16G\u01dc\3H")
        buf.write("\3H\5H\u01e1\nH\3H\3H\3I\3I\5I\u01e7\nI\3J\3J\3K\3K\3")
        buf.write("K\3K\5K\u01ef\nK\3L\3L\7L\u01f3\nL\fL\16L\u01f6\13L\3")
        buf.write("L\3L\3L\3M\3M\3M\3M\5M\u01ff\nM\3N\3N\7N\u0203\nN\fN\16")
        buf.write("N\u0206\13N\3N\3N\7N\u020a\nN\fN\16N\u020d\13N\3N\7N\u0210")
        buf.write("\nN\fN\16N\u0213\13N\3N\3N\7N\u0217\nN\fN\16N\u021a\13")
        buf.write("N\3N\3N\7N\u021e\nN\fN\16N\u0221\13N\7N\u0223\nN\fN\16")
        buf.write("N\u0226\13N\5N\u0228\nN\3N\3N\3O\3O\7O\u022e\nO\fO\16")
        buf.write("O\u0231\13O\3O\3O\3O\7O\u0236\nO\fO\16O\u0239\13O\3O\7")
        buf.write("O\u023c\nO\fO\16O\u023f\13O\3O\3O\7O\u0243\nO\fO\16O\u0246")
        buf.write("\13O\3O\3O\3O\7O\u024b\nO\fO\16O\u024e\13O\5O\u0250\n")
        buf.write("O\7O\u0252\nO\fO\16O\u0255\13O\5O\u0257\nO\3O\3O\3P\6")
        buf.write("P\u025c\nP\rP\16P\u025d\3P\3P\3Q\3Q\3Q\3R\3R\7R\u0267")
        buf.write("\nR\fR\16R\u026a\13R\3R\3R\3S\3S\3S\3S\5S\u0272\nS\3S")
        buf.write("\3S\3T\3T\3T\3T\3T\7T\u027b\nT\fT\16T\u027e\13T\3\u014a")
        buf.write("\2U\3\3\5\2\7\2\t\2\13\2\r\2\17\4\21\5\23\6\25\7\27\b")
        buf.write("\31\t\33\n\35\13\37\f!\r#\16%\17\'\20)\21+\22-\23/\24")
        buf.write("\61\25\63\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G")
        buf.write(" I!K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64")
        buf.write("q\65s\66u\67w8y9{:};\177<\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("=\u0089\2\u008b\2\u008d\2\u008f>\u0091?\u0093\2\u0095")
        buf.write("\2\u0097@\u0099A\u009bB\u009dC\u009fD\u00a1E\u00a3F\u00a5")
        buf.write("G\u00a7H\3\2\24\3\2\62;\3\2\63;\3\2c|\3\2C\\\4\2--//\3")
        buf.write("\2\62\62\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3")
        buf.write("\2\629\4\2GGgg\5\2\n\13\16\17^^\4\2\f\f$$\5\2\13\f\16")
        buf.write("\17\"\"\7\2ddhhppttvv\3\2,,\2\u029c\2\3\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0087\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2")
        buf.write("\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\3\u00a9\3\2\2\2\5\u00ae")
        buf.write("\3\2\2\2\7\u00b0\3\2\2\2\t\u00b2\3\2\2\2\13\u00b4\3\2")
        buf.write("\2\2\r\u00b6\3\2\2\2\17\u00b8\3\2\2\2\21\u00c2\3\2\2\2")
        buf.write("\23\u00c7\3\2\2\2\25\u00cd\3\2\2\2\27\u00d6\3\2\2\2\31")
        buf.write("\u00d9\3\2\2\2\33\u00de\3\2\2\2\35\u00e5\3\2\2\2\37\u00ed")
        buf.write("\3\2\2\2!\u00f3\3\2\2\2#\u00fa\3\2\2\2%\u0103\3\2\2\2")
        buf.write("\'\u0107\3\2\2\2)\u0110\3\2\2\2+\u0113\3\2\2\2-\u011d")
        buf.write("\3\2\2\2/\u0124\3\2\2\2\61\u0129\3\2\2\2\63\u012d\3\2")
        buf.write("\2\2\65\u0133\3\2\2\2\67\u0138\3\2\2\29\u013e\3\2\2\2")
        buf.write(";\u0144\3\2\2\2=\u0152\3\2\2\2?\u0154\3\2\2\2A\u0157\3")
        buf.write("\2\2\2C\u0159\3\2\2\2E\u015c\3\2\2\2G\u015e\3\2\2\2I\u0161")
        buf.write("\3\2\2\2K\u0163\3\2\2\2M\u0166\3\2\2\2O\u0168\3\2\2\2")
        buf.write("Q\u016a\3\2\2\2S\u016d\3\2\2\2U\u0170\3\2\2\2W\u0173\3")
        buf.write("\2\2\2Y\u0176\3\2\2\2[\u0178\3\2\2\2]\u017a\3\2\2\2_\u017d")
        buf.write("\3\2\2\2a\u0180\3\2\2\2c\u0183\3\2\2\2e\u0186\3\2\2\2")
        buf.write("g\u018a\3\2\2\2i\u018e\3\2\2\2k\u0190\3\2\2\2m\u0194\3")
        buf.write("\2\2\2o\u0196\3\2\2\2q\u0198\3\2\2\2s\u019a\3\2\2\2u\u019c")
        buf.write("\3\2\2\2w\u019e\3\2\2\2y\u01a0\3\2\2\2{\u01a2\3\2\2\2")
        buf.write("}\u01a4\3\2\2\2\177\u01a6\3\2\2\2\u0081\u01b0\3\2\2\2")
        buf.write("\u0083\u01b2\3\2\2\2\u0085\u01ba\3\2\2\2\u0087\u01c8\3")
        buf.write("\2\2\2\u0089\u01ca\3\2\2\2\u008b\u01cd\3\2\2\2\u008d\u01d5")
        buf.write("\3\2\2\2\u008f\u01de\3\2\2\2\u0091\u01e6\3\2\2\2\u0093")
        buf.write("\u01e8\3\2\2\2\u0095\u01ee\3\2\2\2\u0097\u01f0\3\2\2\2")
        buf.write("\u0099\u01fe\3\2\2\2\u009b\u0200\3\2\2\2\u009d\u022b\3")
        buf.write("\2\2\2\u009f\u025b\3\2\2\2\u00a1\u0261\3\2\2\2\u00a3\u0264")
        buf.write("\3\2\2\2\u00a5\u026d\3\2\2\2\u00a7\u0275\3\2\2\2\u00a9")
        buf.write("\u00aa\7o\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7k\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\4\3\2\2\2\u00ae\u00af\t\2\2\2\u00af")
        buf.write("\6\3\2\2\2\u00b0\u00b1\t\3\2\2\u00b1\b\3\2\2\2\u00b2\u00b3")
        buf.write("\t\4\2\2\u00b3\n\3\2\2\2\u00b4\u00b5\t\5\2\2\u00b5\f\3")
        buf.write("\2\2\2\u00b6\u00b7\t\6\2\2\u00b7\16\3\2\2\2\u00b8\u00bf")
        buf.write("\5\t\5\2\u00b9\u00be\5\t\5\2\u00ba\u00be\5\13\6\2\u00bb")
        buf.write("\u00be\7a\2\2\u00bc\u00be\5\r\7\2\u00bd\u00b9\3\2\2\2")
        buf.write("\u00bd\u00ba\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3")
        buf.write("\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0")
        buf.write("\3\2\2\2\u00c0\20\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3")
        buf.write("\7D\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7f\2\2\u00c5\u00c6")
        buf.write("\7{\2\2\u00c6\22\3\2\2\2\u00c7\u00c8\7D\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc")
        buf.write("\7m\2\2\u00cc\24\3\2\2\2\u00cd\u00ce\7E\2\2\u00ce\u00cf")
        buf.write("\7q\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5")
        buf.write("\7g\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7F\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\30\3\2\2\2\u00d9\u00da\7G\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7g\2\2\u00dd\32")
        buf.write("\3\2\2\2\u00de\u00df\7G\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1")
        buf.write("\7u\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7K\2\2\u00e3\u00e4")
        buf.write("\7h\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7G\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7f\2\2\u00e8\u00e9\7D\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7f\2\2\u00eb\u00ec\7{\2\2\u00ec\36")
        buf.write("\3\2\2\2\u00ed\u00ee\7G\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7f\2\2\u00f0\u00f1\7K\2\2\u00f1\u00f2\7h\2\2\u00f2 \3")
        buf.write("\2\2\2\u00f3\u00f4\7G\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7f\2\2\u00f6\u00f7\7H\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7G\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\u00fd\7f\2\2\u00fd\u00fe\7Y\2\2\u00fe\u00ff")
        buf.write("\7j\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7n\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102$\3\2\2\2\u0103\u0104\7H\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\u0106\7t\2\2\u0106&\3\2\2\2\u0107\u0108")
        buf.write("\7H\2\2\u0108\u0109\7w\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7e\2\2\u010b\u010c\7v\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7p\2\2\u010f(\3\2\2\2\u0110\u0111")
        buf.write("\7K\2\2\u0111\u0112\7h\2\2\u0112*\3\2\2\2\u0113\u0114")
        buf.write("\7R\2\2\u0114\u0115\7c\2\2\u0115\u0116\7t\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7o\2\2\u0118\u0119\7g\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\u011b\7g\2\2\u011b\u011c\7t\2\2\u011c,\3")
        buf.write("\2\2\2\u011d\u011e\7T\2\2\u011e\u011f\7g\2\2\u011f\u0120")
        buf.write("\7v\2\2\u0120\u0121\7w\2\2\u0121\u0122\7t\2\2\u0122\u0123")
        buf.write("\7p\2\2\u0123.\3\2\2\2\u0124\u0125\7V\2\2\u0125\u0126")
        buf.write("\7j\2\2\u0126\u0127\7g\2\2\u0127\u0128\7p\2\2\u0128\60")
        buf.write("\3\2\2\2\u0129\u012a\7X\2\2\u012a\u012b\7c\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\62\3\2\2\2\u012d\u012e\7Y\2\2\u012e\u012f")
        buf.write("\7j\2\2\u012f\u0130\7k\2\2\u0130\u0131\7n\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\64\3\2\2\2\u0133\u0134\7V\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135\u0136\7w\2\2\u0136\u0137\7g\2\2\u0137\66")
        buf.write("\3\2\2\2\u0138\u0139\7H\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7n\2\2\u013b\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d8\3")
        buf.write("\2\2\2\u013e\u013f\7G\2\2\u013f\u0140\7p\2\2\u0140\u0141")
        buf.write("\7f\2\2\u0141\u0142\7F\2\2\u0142\u0143\7q\2\2\u0143:\3")
        buf.write("\2\2\2\u0144\u0145\7,\2\2\u0145\u0146\7,\2\2\u0146\u014a")
        buf.write("\3\2\2\2\u0147\u0149\13\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("\u014c\3\2\2\2\u014a\u014b\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014e\7")
        buf.write(",\2\2\u014e\u014f\7,\2\2\u014f\u0150\3\2\2\2\u0150\u0151")
        buf.write("\b\36\2\2\u0151<\3\2\2\2\u0152\u0153\7-\2\2\u0153>\3\2")
        buf.write("\2\2\u0154\u0155\7-\2\2\u0155\u0156\7\60\2\2\u0156@\3")
        buf.write("\2\2\2\u0157\u0158\7/\2\2\u0158B\3\2\2\2\u0159\u015a\7")
        buf.write("/\2\2\u015a\u015b\7\60\2\2\u015bD\3\2\2\2\u015c\u015d")
        buf.write("\7,\2\2\u015dF\3\2\2\2\u015e\u015f\7,\2\2\u015f\u0160")
        buf.write("\7\60\2\2\u0160H\3\2\2\2\u0161\u0162\7^\2\2\u0162J\3\2")
        buf.write("\2\2\u0163\u0164\7^\2\2\u0164\u0165\7\60\2\2\u0165L\3")
        buf.write("\2\2\2\u0166\u0167\7\'\2\2\u0167N\3\2\2\2\u0168\u0169")
        buf.write("\7#\2\2\u0169P\3\2\2\2\u016a\u016b\7(\2\2\u016b\u016c")
        buf.write("\7(\2\2\u016cR\3\2\2\2\u016d\u016e\7~\2\2\u016e\u016f")
        buf.write("\7~\2\2\u016fT\3\2\2\2\u0170\u0171\7?\2\2\u0171\u0172")
        buf.write("\7?\2\2\u0172V\3\2\2\2\u0173\u0174\7#\2\2\u0174\u0175")
        buf.write("\7?\2\2\u0175X\3\2\2\2\u0176\u0177\7@\2\2\u0177Z\3\2\2")
        buf.write("\2\u0178\u0179\7>\2\2\u0179\\\3\2\2\2\u017a\u017b\7@\2")
        buf.write("\2\u017b\u017c\7?\2\2\u017c^\3\2\2\2\u017d\u017e\7>\2")
        buf.write("\2\u017e\u017f\7?\2\2\u017f`\3\2\2\2\u0180\u0181\7@\2")
        buf.write("\2\u0181\u0182\7\60\2\2\u0182b\3\2\2\2\u0183\u0184\7>")
        buf.write("\2\2\u0184\u0185\7\60\2\2\u0185d\3\2\2\2\u0186\u0187\7")
        buf.write("@\2\2\u0187\u0188\7?\2\2\u0188\u0189\7\60\2\2\u0189f\3")
        buf.write("\2\2\2\u018a\u018b\7>\2\2\u018b\u018c\7?\2\2\u018c\u018d")
        buf.write("\7\60\2\2\u018dh\3\2\2\2\u018e\u018f\7?\2\2\u018fj\3\2")
        buf.write("\2\2\u0190\u0191\7?\2\2\u0191\u0192\7^\2\2\u0192\u0193")
        buf.write("\7?\2\2\u0193l\3\2\2\2\u0194\u0195\7*\2\2\u0195n\3\2\2")
        buf.write("\2\u0196\u0197\7+\2\2\u0197p\3\2\2\2\u0198\u0199\7]\2")
        buf.write("\2\u0199r\3\2\2\2\u019a\u019b\7_\2\2\u019bt\3\2\2\2\u019c")
        buf.write("\u019d\7}\2\2\u019dv\3\2\2\2\u019e\u019f\7\177\2\2\u019f")
        buf.write("x\3\2\2\2\u01a0\u01a1\7=\2\2\u01a1z\3\2\2\2\u01a2\u01a3")
        buf.write("\7<\2\2\u01a3|\3\2\2\2\u01a4\u01a5\7.\2\2\u01a5~\3\2\2")
        buf.write("\2\u01a6\u01a7\7\60\2\2\u01a7\u0080\3\2\2\2\u01a8\u01b1")
        buf.write("\t\7\2\2\u01a9\u01ad\t\3\2\2\u01aa\u01ac\t\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01a8\3\2\2\2\u01b0\u01a9\3\2\2\2\u01b1\u0082")
        buf.write("\3\2\2\2\u01b2\u01b3\t\b\2\2\u01b3\u01b7\t\t\2\2\u01b4")
        buf.write("\u01b6\t\n\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u0084\3")
        buf.write("\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bb\t\13\2\2\u01bb")
        buf.write("\u01bf\t\f\2\2\u01bc\u01be\t\r\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3")
        buf.write("\2\2\2\u01c0\u0086\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c9")
        buf.write("\5\u0081A\2\u01c3\u01c6\7\62\2\2\u01c4\u01c7\5\u0083B")
        buf.write("\2\u01c5\u01c7\5\u0085C\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c2\3\2\2\2\u01c8")
        buf.write("\u01c3\3\2\2\2\u01c9\u0088\3\2\2\2\u01ca\u01cb\5\u0081")
        buf.write("A\2\u01cb\u008a\3\2\2\2\u01cc\u01ce\7\60\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d2\3\2\2\2\u01cf")
        buf.write("\u01d1\t\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2")
        buf.write("\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u008c\3")
        buf.write("\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d7\t\16\2\2\u01d6")
        buf.write("\u01d8\t\6\2\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u01da\3\2\2\2\u01d9\u01db\t\2\2\2\u01da\u01d9\3")
        buf.write("\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd")
        buf.write("\3\2\2\2\u01dd\u008e\3\2\2\2\u01de\u01e0\5\u0089E\2\u01df")
        buf.write("\u01e1\5\u008bF\2\u01e0\u01df\3\2\2\2\u01e0\u01e1\3\2")
        buf.write("\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\5\u008dG\2\u01e3")
        buf.write("\u0090\3\2\2\2\u01e4\u01e7\5\65\33\2\u01e5\u01e7\5\67")
        buf.write("\34\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7\u0092")
        buf.write("\3\2\2\2\u01e8\u01e9\t\17\2\2\u01e9\u0094\3\2\2\2\u01ea")
        buf.write("\u01ef\n\20\2\2\u01eb\u01ef\5\u0093J\2\u01ec\u01ed\7)")
        buf.write("\2\2\u01ed\u01ef\7$\2\2\u01ee\u01ea\3\2\2\2\u01ee\u01eb")
        buf.write("\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u0096\3\2\2\2\u01f0")
        buf.write("\u01f4\7$\2\2\u01f1\u01f3\5\u0095K\2\u01f2\u01f1\3\2\2")
        buf.write("\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write("\u01f8\7$\2\2\u01f8\u01f9\bL\3\2\u01f9\u0098\3\2\2\2\u01fa")
        buf.write("\u01ff\5\u0087D\2\u01fb\u01ff\5\u008fH\2\u01fc\u01ff\5")
        buf.write("\u0091I\2\u01fd\u01ff\5\u0097L\2\u01fe\u01fa\3\2\2\2\u01fe")
        buf.write("\u01fb\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01fd\3\2\2\2")
        buf.write("\u01ff\u009a\3\2\2\2\u0200\u0227\5u;\2\u0201\u0203\7\"")
        buf.write("\2\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0207\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0207\u020b\5\u0099M\2\u0208\u020a\7\"")
        buf.write("\2\2\u0209\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u0224\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020e\u0210\7\"\2\2\u020f\u020e\3\2\2\2")
        buf.write("\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3")
        buf.write("\2\2\2\u0212\u0214\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0218")
        buf.write("\5}?\2\u0215\u0217\7\"\2\2\u0216\u0215\3\2\2\2\u0217\u021a")
        buf.write("\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u021b\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021f\5\u0099")
        buf.write("M\2\u021c\u021e\7\"\2\2\u021d\u021c\3\2\2\2\u021e\u0221")
        buf.write("\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write("\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u0211\3\2\2\2")
        buf.write("\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3")
        buf.write("\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0204")
        buf.write("\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\u022a\5w<\2\u022a\u009c\3\2\2\2\u022b\u0256\5u;\2\u022c")
        buf.write("\u022e\7\"\2\2\u022d\u022c\3\2\2\2\u022e\u0231\3\2\2\2")
        buf.write("\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232\3")
        buf.write("\2\2\2\u0231\u022f\3\2\2\2\u0232\u0257\5\u0099M\2\u0233")
        buf.write("\u0237\5\u009bN\2\u0234\u0236\7\"\2\2\u0235\u0234\3\2")
        buf.write("\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238")
        buf.write("\3\2\2\2\u0238\u0253\3\2\2\2\u0239\u0237\3\2\2\2\u023a")
        buf.write("\u023c\7\"\2\2\u023b\u023a\3\2\2\2\u023c\u023f\3\2\2\2")
        buf.write("\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240\3")
        buf.write("\2\2\2\u023f\u023d\3\2\2\2\u0240\u0244\5}?\2\u0241\u0243")
        buf.write("\7\"\2\2\u0242\u0241\3\2\2\2\u0243\u0246\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u024f\3\2\2\2")
        buf.write("\u0246\u0244\3\2\2\2\u0247\u0250\5\u0099M\2\u0248\u024c")
        buf.write("\5\u009bN\2\u0249\u024b\7\"\2\2\u024a\u0249\3\2\2\2\u024b")
        buf.write("\u024e\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2")
        buf.write("\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2\u024f\u0247\3")
        buf.write("\2\2\2\u024f\u0248\3\2\2\2\u0250\u0252\3\2\2\2\u0251\u023d")
        buf.write("\3\2\2\2\u0252\u0255\3\2\2\2\u0253\u0251\3\2\2\2\u0253")
        buf.write("\u0254\3\2\2\2\u0254\u0257\3\2\2\2\u0255\u0253\3\2\2\2")
        buf.write("\u0256\u022f\3\2\2\2\u0256\u0233\3\2\2\2\u0256\u0257\3")
        buf.write("\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259\5w<\2\u0259\u009e")
        buf.write("\3\2\2\2\u025a\u025c\t\21\2\2\u025b\u025a\3\2\2\2\u025c")
        buf.write("\u025d\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025e\u025f\3\2\2\2\u025f\u0260\bP\2\2\u0260\u00a0\3")
        buf.write("\2\2\2\u0261\u0262\13\2\2\2\u0262\u0263\bQ\4\2\u0263\u00a2")
        buf.write("\3\2\2\2\u0264\u0268\7$\2\2\u0265\u0267\5\u0095K\2\u0266")
        buf.write("\u0265\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2")
        buf.write("\u0268\u0269\3\2\2\2\u0269\u026b\3\2\2\2\u026a\u0268\3")
        buf.write("\2\2\2\u026b\u026c\bR\5\2\u026c\u00a4\3\2\2\2\u026d\u0271")
        buf.write("\5\u00a3R\2\u026e\u026f\7^\2\2\u026f\u0272\n\22\2\2\u0270")
        buf.write("\u0272\7)\2\2\u0271\u026e\3\2\2\2\u0271\u0270\3\2\2\2")
        buf.write("\u0272\u0273\3\2\2\2\u0273\u0274\bS\6\2\u0274\u00a6\3")
        buf.write("\2\2\2\u0275\u0276\7,\2\2\u0276\u0277\7,\2\2\u0277\u027c")
        buf.write("\3\2\2\2\u0278\u0279\n\23\2\2\u0279\u027b\n\23\2\2\u027a")
        buf.write("\u0278\3\2\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2")
        buf.write("\u027c\u027d\3\2\2\2\u027d\u00a8\3\2\2\2\u027e\u027c\3")
        buf.write("\2\2\2(\2\u00bd\u00bf\u014a\u01ad\u01b0\u01b7\u01bf\u01c6")
        buf.write("\u01c8\u01cd\u01d2\u01d7\u01dc\u01e0\u01e6\u01ee\u01f4")
        buf.write("\u01fe\u0204\u020b\u0211\u0218\u021f\u0224\u0227\u022f")
        buf.write("\u0237\u023d\u0244\u024c\u024f\u0253\u0256\u025d\u0268")
        buf.write("\u0271\u027c\7\b\2\2\3L\2\3Q\3\3R\4\3S\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    BODY = 3
    BREAK = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    ELSE_IF = 8
    END_BODY = 9
    END_IF = 10
    END_FOR = 11
    END_WHILE = 12
    FOR = 13
    FUNCTION = 14
    IF = 15
    PARAMETER = 16
    RETURN = 17
    THEN = 18
    VAR = 19
    WHILE = 20
    TRUE = 21
    FALSE = 22
    END_DO = 23
    COMMENT = 24
    ADD_INT = 25
    ADD_FLOAT = 26
    SUB_INT = 27
    SUB_FLOAT = 28
    MUL_INT = 29
    MUL_FLOAT = 30
    DIV_INT = 31
    DIV_FLOAT = 32
    MODULO = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL_INT = 37
    UNEQUAL = 38
    LARGE_INT = 39
    SMALL_INT = 40
    LARGE_EQUAL_INT = 41
    SMALL_EQUAL_INT = 42
    LARGE_FLOAT = 43
    SMALL_FLOAT = 44
    LARGE_EQUAL_FLOAT = 45
    SMALL_EQUAL_FLOAT = 46
    ASSIGN = 47
    EQUAL_FLOAT = 48
    LP = 49
    RP = 50
    LQ = 51
    RQ = 52
    LB = 53
    RB = 54
    SEMI = 55
    COLON = 56
    COMMA = 57
    DOT = 58
    INTLIT = 59
    FLOATLIT = 60
    BOOLEANLIT = 61
    STRINGLIT = 62
    LITERALS = 63
    ARRAYLIT = 64
    MULTI_ARRAY_LIT = 65
    WS = 66
    ERROR_CHAR = 67
    UNCLOSE_STRING = 68
    ILLEGAL_ESCAPE = 69
    UNTERMINATED_COMMENT = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'True'", "'False'", "'EndDo'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
            "'>.'", "'<.'", "'>=.'", "'<=.'", "'='", "'=\\='", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "';'", "':'", "','", "'.'" ]

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
            "COMMA", "DOT", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
            "LITERALS", "ARRAYLIT", "MULTI_ARRAY_LIT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "DIGIT", "NON_ZERO_DIGIT", "LOWER_CHAR", "UPPER_CHAR", 
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
                  "DOT", "DEC", "HEX", "OCT", "INTLIT", "INT_PART", "DEC_PART", 
                  "EXP_PART", "FLOATLIT", "BOOLEANLIT", "SPEC_SEQUENCE", 
                  "STR_CHAR", "STRINGLIT", "LITERALS", "ARRAYLIT", "MULTI_ARRAY_LIT", 
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
            actions[74] = self.STRINGLIT_action 
            actions[79] = self.ERROR_CHAR_action 
            actions[80] = self.UNCLOSE_STRING_action 
            actions[81] = self.ILLEGAL_ESCAPE_action 
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

     


