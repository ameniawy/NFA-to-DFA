// Generated from /home/ameniawy/Documents/SEM_10/Compiler Lab/Task_2/task_2_1.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class task_2_1Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		REG=1, COMMAND=2, IMMEDIATE=3, MEMORY=4, COMMA=5, SPACE=6, NEWLINE=7;
	public static final int
		RULE_command = 0, RULE_newline = 1;
	public static final String[] ruleNames = {
		"command", "newline"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, "','", "' '", "'\n'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "REG", "COMMAND", "IMMEDIATE", "MEMORY", "COMMA", "SPACE", "NEWLINE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "task_2_1.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public task_2_1Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class CommandContext extends ParserRuleContext {
		public TerminalNode COMMAND() { return getToken(task_2_1Parser.COMMAND, 0); }
		public List<TerminalNode> REG() { return getTokens(task_2_1Parser.REG); }
		public TerminalNode REG(int i) {
			return getToken(task_2_1Parser.REG, i);
		}
		public TerminalNode COMMA() { return getToken(task_2_1Parser.COMMA, 0); }
		public List<TerminalNode> SPACE() { return getTokens(task_2_1Parser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(task_2_1Parser.SPACE, i);
		}
		public TerminalNode IMMEDIATE() { return getToken(task_2_1Parser.IMMEDIATE, 0); }
		public TerminalNode MEMORY() { return getToken(task_2_1Parser.MEMORY, 0); }
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_command);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(4);
			match(COMMAND);
			setState(6);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(5);
				match(REG);
				}
				break;
			}
			setState(9);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(8);
				match(COMMA);
				}
			}

			setState(14);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SPACE) {
				{
				{
				setState(11);
				match(SPACE);
				}
				}
				setState(16);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(18);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << REG) | (1L << IMMEDIATE) | (1L << MEMORY))) != 0)) {
				{
				setState(17);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << REG) | (1L << IMMEDIATE) | (1L << MEMORY))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NewlineContext extends ParserRuleContext {
		public TerminalNode NEWLINE() { return getToken(task_2_1Parser.NEWLINE, 0); }
		public NewlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_newline; }
	}

	public final NewlineContext newline() throws RecognitionException {
		NewlineContext _localctx = new NewlineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_newline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t\31\4\2\t\2\4\3"+
		"\t\3\3\2\3\2\5\2\t\n\2\3\2\5\2\f\n\2\3\2\7\2\17\n\2\f\2\16\2\22\13\2\3"+
		"\2\5\2\25\n\2\3\3\3\3\3\3\2\2\4\2\4\2\3\4\2\3\3\5\6\2\32\2\6\3\2\2\2\4"+
		"\26\3\2\2\2\6\b\7\4\2\2\7\t\7\3\2\2\b\7\3\2\2\2\b\t\3\2\2\2\t\13\3\2\2"+
		"\2\n\f\7\7\2\2\13\n\3\2\2\2\13\f\3\2\2\2\f\20\3\2\2\2\r\17\7\b\2\2\16"+
		"\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21\24\3\2\2\2\22"+
		"\20\3\2\2\2\23\25\t\2\2\2\24\23\3\2\2\2\24\25\3\2\2\2\25\3\3\2\2\2\26"+
		"\27\7\t\2\2\27\5\3\2\2\2\6\b\13\20\24";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}