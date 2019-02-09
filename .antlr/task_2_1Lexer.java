// Generated from /home/ameniawy/Documents/SEM_10/Compiler Lab/Task_2/task_2_1.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class task_2_1Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		REG=1, COMMAND=2, IMMEDIATE=3, MEMORY=4, COMMA=5, SPACE=6, NEWLINE=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"REG", "COMMAND", "IMMEDIATE", "MEMORY", "COMMA", "SPACE", "NEWLINE"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, "','", "' '"
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


	public task_2_1Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "task_2_1.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t>\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\5\2\32\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3%\n\3\3\4\6"+
		"\4(\n\4\r\4\16\4)\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b"+
		"\6\b9\n\b\r\b\16\b:\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\4"+
		"\5\2\62;C\\c|\4\2\f\f\17\17\2D\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t"+
		"\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\31\3\2\2\2\5$\3\2\2\2"+
		"\7\'\3\2\2\2\t+\3\2\2\2\13/\3\2\2\2\r\63\3\2\2\2\178\3\2\2\2\21\22\7C"+
		"\2\2\22\32\7Z\2\2\23\24\7D\2\2\24\32\7Z\2\2\25\26\7E\2\2\26\32\7Z\2\2"+
		"\27\30\7F\2\2\30\32\7Z\2\2\31\21\3\2\2\2\31\23\3\2\2\2\31\25\3\2\2\2\31"+
		"\27\3\2\2\2\32\4\3\2\2\2\33\34\7C\2\2\34\35\7C\2\2\35%\7C\2\2\36\37\7"+
		"C\2\2\37 \7F\2\2 %\7F\2\2!\"\7K\2\2\"#\7P\2\2#%\7E\2\2$\33\3\2\2\2$\36"+
		"\3\2\2\2$!\3\2\2\2%\6\3\2\2\2&(\t\2\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2"+
		"\2)*\3\2\2\2*\b\3\2\2\2+,\7]\2\2,-\5\3\2\2-.\7_\2\2.\n\3\2\2\2/\60\7."+
		"\2\2\60\61\3\2\2\2\61\62\b\6\2\2\62\f\3\2\2\2\63\64\7\"\2\2\64\65\3\2"+
		"\2\2\65\66\b\7\2\2\66\16\3\2\2\2\679\t\3\2\28\67\3\2\2\29:\3\2\2\2:8\3"+
		"\2\2\2:;\3\2\2\2;<\3\2\2\2<=\b\b\2\2=\20\3\2\2\2\7\2\31$):\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}