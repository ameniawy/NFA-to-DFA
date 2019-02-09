# Generated from task_2_1.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\t")
        buf.write(">\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\32\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3%\n\3\3\4\6\4(\n")
        buf.write("\4\r\4\16\4)\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\6\b9\n\b\r\b\16\b:\3\b\3\b\2\2\t\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\3\2\4\5\2\62;C\\c|\4\2\f\f\17\17")
        buf.write("D\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\31\3\2\2\2\5$\3\2")
        buf.write("\2\2\7\'\3\2\2\2\t+\3\2\2\2\13/\3\2\2\2\r\63\3\2\2\2\17")
        buf.write("8\3\2\2\2\21\22\7C\2\2\22\32\7Z\2\2\23\24\7D\2\2\24\32")
        buf.write("\7Z\2\2\25\26\7E\2\2\26\32\7Z\2\2\27\30\7F\2\2\30\32\7")
        buf.write("Z\2\2\31\21\3\2\2\2\31\23\3\2\2\2\31\25\3\2\2\2\31\27")
        buf.write("\3\2\2\2\32\4\3\2\2\2\33\34\7C\2\2\34\35\7C\2\2\35%\7")
        buf.write("C\2\2\36\37\7C\2\2\37 \7F\2\2 %\7F\2\2!\"\7K\2\2\"#\7")
        buf.write("P\2\2#%\7E\2\2$\33\3\2\2\2$\36\3\2\2\2$!\3\2\2\2%\6\3")
        buf.write("\2\2\2&(\t\2\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2")
        buf.write("\2\2*\b\3\2\2\2+,\7]\2\2,-\5\3\2\2-.\7_\2\2.\n\3\2\2\2")
        buf.write("/\60\7.\2\2\60\61\3\2\2\2\61\62\b\6\2\2\62\f\3\2\2\2\63")
        buf.write("\64\7\"\2\2\64\65\3\2\2\2\65\66\b\7\2\2\66\16\3\2\2\2")
        buf.write("\679\t\3\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2")
        buf.write(";<\3\2\2\2<=\b\b\2\2=\20\3\2\2\2\7\2\31$):\3\b\2\2")
        return buf.getvalue()


class task_2_1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    REG = 1
    COMMAND = 2
    IMMEDIATE = 3
    MEMORY = 4
    COMMA = 5
    SPACE = 6
    NEWLINE = 7

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "' '" ]

    symbolicNames = [ "<INVALID>",
            "REG", "COMMAND", "IMMEDIATE", "MEMORY", "COMMA", "SPACE", "NEWLINE" ]

    ruleNames = [ "REG", "COMMAND", "IMMEDIATE", "MEMORY", "COMMA", "SPACE", 
                  "NEWLINE" ]

    grammarFileName = "task_2_1.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


