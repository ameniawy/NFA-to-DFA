# Generated from task_2_1.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\t")
        buf.write("/\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\3\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\3\5\3")
        buf.write("\31\n\3\3\3\7\3\34\n\3\f\3\16\3\37\13\3\3\3\5\3\"\n\3")
        buf.write("\3\3\7\3%\n\3\f\3\16\3(\13\3\3\3\5\3+\n\3\3\4\3\4\3\4")
        buf.write("\2\2\5\2\4\6\2\4\4\2\3\3\6\6\4\2\3\3\5\6\62\2\r\3\2\2")
        buf.write("\2\4\20\3\2\2\2\6,\3\2\2\2\b\t\5\4\3\2\t\n\5\6\4\2\n\f")
        buf.write("\3\2\2\2\13\b\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3")
        buf.write("\2\2\2\16\3\3\2\2\2\17\r\3\2\2\2\20\24\7\4\2\2\21\23\7")
        buf.write("\b\2\2\22\21\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25")
        buf.write("\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2\2\27\31\t\2\2\2\30")
        buf.write("\27\3\2\2\2\30\31\3\2\2\2\31\35\3\2\2\2\32\34\7\b\2\2")
        buf.write("\33\32\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36!\3\2\2\2\37\35\3\2\2\2 \"\7\7\2\2! \3\2\2\2!\"\3")
        buf.write("\2\2\2\"&\3\2\2\2#%\7\b\2\2$#\3\2\2\2%(\3\2\2\2&$\3\2")
        buf.write("\2\2&\'\3\2\2\2\'*\3\2\2\2(&\3\2\2\2)+\t\3\2\2*)\3\2\2")
        buf.write("\2*+\3\2\2\2+\5\3\2\2\2,-\7\t\2\2-\7\3\2\2\2\t\r\24\30")
        buf.write("\35!&*")
        return buf.getvalue()


class task_2_1Parser ( Parser ):

    grammarFileName = "task_2_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "' '" ]

    symbolicNames = [ "<INVALID>", "REG", "COMMAND", "IMMEDIATE", "MEMORY", 
                      "COMMA", "SPACE", "NEWLINE" ]

    RULE_start = 0
    RULE_command = 1
    RULE_newline = 2

    ruleNames =  [ "start", "command", "newline" ]

    EOF = Token.EOF
    REG=1
    COMMAND=2
    IMMEDIATE=3
    MEMORY=4
    COMMA=5
    SPACE=6
    NEWLINE=7

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(task_2_1Parser.CommandContext)
            else:
                return self.getTypedRuleContext(task_2_1Parser.CommandContext,i)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(task_2_1Parser.NewlineContext)
            else:
                return self.getTypedRuleContext(task_2_1Parser.NewlineContext,i)


        def getRuleIndex(self):
            return task_2_1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = task_2_1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==task_2_1Parser.COMMAND:
                self.state = 6
                self.command()
                self.state = 7
                self.newline()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(task_2_1Parser.COMMAND, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.SPACE)
            else:
                return self.getToken(task_2_1Parser.SPACE, i)

        def COMMA(self):
            return self.getToken(task_2_1Parser.COMMA, 0)

        def REG(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.REG)
            else:
                return self.getToken(task_2_1Parser.REG, i)

        def MEMORY(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.MEMORY)
            else:
                return self.getToken(task_2_1Parser.MEMORY, i)

        def IMMEDIATE(self):
            return self.getToken(task_2_1Parser.IMMEDIATE, 0)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = task_2_1Parser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(task_2_1Parser.COMMAND)
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 15
                    self.match(task_2_1Parser.SPACE) 
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 22
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 21
                _la = self._input.LA(1)
                if not(_la==task_2_1Parser.REG or _la==task_2_1Parser.MEMORY):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()


            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 24
                    self.match(task_2_1Parser.SPACE) 
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 31
            _la = self._input.LA(1)
            if _la==task_2_1Parser.COMMA:
                self.state = 30
                self.match(task_2_1Parser.COMMA)


            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==task_2_1Parser.SPACE:
                self.state = 33
                self.match(task_2_1Parser.SPACE)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << task_2_1Parser.REG) | (1 << task_2_1Parser.IMMEDIATE) | (1 << task_2_1Parser.MEMORY))) != 0):
                self.state = 39
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << task_2_1Parser.REG) | (1 << task_2_1Parser.IMMEDIATE) | (1 << task_2_1Parser.MEMORY))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NewlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(task_2_1Parser.NEWLINE, 0)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline" ):
                listener.enterNewline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline" ):
                listener.exitNewline(self)




    def newline(self):

        localctx = task_2_1Parser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(task_2_1Parser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





