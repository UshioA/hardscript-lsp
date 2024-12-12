# Generated from ./src/HardScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,65,314,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,4,0,39,8,0,11,0,
        12,0,40,1,1,1,1,1,1,3,1,46,8,1,1,1,3,1,49,8,1,1,1,1,1,5,1,53,8,1,
        10,1,12,1,56,9,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,1,1,1,1,1,1,1,5,1,
        68,8,1,10,1,12,1,71,9,1,1,1,1,1,3,1,75,8,1,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,5,3,86,8,3,10,3,12,3,89,9,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,106,8,4,10,4,12,4,109,
        9,4,1,4,1,4,3,4,113,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,125,8,5,1,6,1,6,1,6,5,6,130,8,6,10,6,12,6,133,9,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,3,7,157,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,4,7,203,8,7,11,7,12,7,204,1,7,1,7,1,7,1,7,1,7,5,7,212,
        8,7,10,7,12,7,215,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,227,8,8,1,9,1,9,1,9,5,9,232,8,9,10,9,12,9,235,9,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,5,9,246,8,9,10,9,12,9,249,9,9,1,9,3,9,252,
        8,9,1,10,1,10,1,10,1,10,3,10,258,8,10,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,13,1,13,3,13,271,8,13,1,14,1,14,1,14,1,14,4,
        14,277,8,14,11,14,12,14,278,3,14,281,8,14,1,15,1,15,1,15,1,15,1,
        15,5,15,288,8,15,10,15,12,15,291,9,15,1,15,1,15,1,15,1,15,1,15,1,
        15,3,15,299,8,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,
        17,1,17,3,17,312,8,17,1,17,0,1,14,18,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,0,7,1,0,20,23,1,0,25,27,1,0,20,21,1,0,28,31,
        1,0,32,35,1,0,36,37,1,0,39,41,355,0,38,1,0,0,0,2,74,1,0,0,0,4,76,
        1,0,0,0,6,81,1,0,0,0,8,112,1,0,0,0,10,124,1,0,0,0,12,126,1,0,0,0,
        14,156,1,0,0,0,16,226,1,0,0,0,18,251,1,0,0,0,20,257,1,0,0,0,22,259,
        1,0,0,0,24,263,1,0,0,0,26,270,1,0,0,0,28,280,1,0,0,0,30,298,1,0,
        0,0,32,300,1,0,0,0,34,311,1,0,0,0,36,39,3,2,1,0,37,39,3,24,12,0,
        38,36,1,0,0,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,
        0,0,0,41,1,1,0,0,0,42,43,5,1,0,0,43,45,5,63,0,0,44,46,3,6,3,0,45,
        44,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,49,3,4,2,0,48,47,1,0,0,
        0,48,49,1,0,0,0,49,50,1,0,0,0,50,54,5,2,0,0,51,53,3,8,4,0,52,51,
        1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,
        56,54,1,0,0,0,57,75,5,3,0,0,58,59,5,4,0,0,59,61,5,63,0,0,60,62,3,
        6,3,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,5,0,0,64,
        65,3,14,7,0,65,69,5,2,0,0,66,68,3,8,4,0,67,66,1,0,0,0,68,71,1,0,
        0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,
        5,3,0,0,73,75,1,0,0,0,74,42,1,0,0,0,74,58,1,0,0,0,75,3,1,0,0,0,76,
        77,5,5,0,0,77,78,3,14,7,0,78,79,5,6,0,0,79,80,3,14,7,0,80,5,1,0,
        0,0,81,82,5,7,0,0,82,87,5,63,0,0,83,84,5,8,0,0,84,86,5,63,0,0,85,
        83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,
        0,89,87,1,0,0,0,90,91,5,9,0,0,91,7,1,0,0,0,92,113,3,24,12,0,93,113,
        3,10,5,0,94,95,5,10,0,0,95,113,3,12,6,0,96,97,5,10,0,0,97,113,3,
        14,7,0,98,113,3,14,7,0,99,100,5,11,0,0,100,101,5,7,0,0,101,102,3,
        22,11,0,102,103,5,9,0,0,103,107,5,2,0,0,104,106,3,8,4,0,105,104,
        1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,110,
        1,0,0,0,109,107,1,0,0,0,110,111,5,3,0,0,111,113,1,0,0,0,112,92,1,
        0,0,0,112,93,1,0,0,0,112,94,1,0,0,0,112,96,1,0,0,0,112,98,1,0,0,
        0,112,99,1,0,0,0,113,9,1,0,0,0,114,115,5,12,0,0,115,116,3,12,6,0,
        116,117,5,13,0,0,117,118,3,26,13,0,118,125,1,0,0,0,119,120,5,14,
        0,0,120,121,3,12,6,0,121,122,5,13,0,0,122,123,3,26,13,0,123,125,
        1,0,0,0,124,114,1,0,0,0,124,119,1,0,0,0,125,11,1,0,0,0,126,131,3,
        28,14,0,127,128,5,8,0,0,128,130,3,28,14,0,129,127,1,0,0,0,130,133,
        1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,13,1,0,0,0,133,131,1,
        0,0,0,134,135,6,7,-1,0,135,157,3,26,13,0,136,157,3,34,17,0,137,138,
        5,15,0,0,138,139,3,18,9,0,139,140,5,16,0,0,140,157,1,0,0,0,141,142,
        5,18,0,0,142,157,3,14,7,19,143,144,7,0,0,0,144,157,3,14,7,17,145,
        146,5,48,0,0,146,147,3,14,7,0,147,148,5,49,0,0,148,149,3,14,7,0,
        149,150,5,50,0,0,150,151,3,14,7,2,151,157,1,0,0,0,152,153,5,7,0,
        0,153,154,3,14,7,0,154,155,5,9,0,0,155,157,1,0,0,0,156,134,1,0,0,
        0,156,136,1,0,0,0,156,137,1,0,0,0,156,141,1,0,0,0,156,143,1,0,0,
        0,156,145,1,0,0,0,156,152,1,0,0,0,157,213,1,0,0,0,158,159,10,16,
        0,0,159,160,5,24,0,0,160,212,3,14,7,17,161,162,10,15,0,0,162,163,
        7,1,0,0,163,212,3,14,7,16,164,165,10,14,0,0,165,166,7,2,0,0,166,
        212,3,14,7,15,167,168,10,13,0,0,168,169,7,3,0,0,169,212,3,14,7,14,
        170,171,10,12,0,0,171,172,7,4,0,0,172,212,3,14,7,13,173,174,10,11,
        0,0,174,175,7,5,0,0,175,212,3,14,7,12,176,177,10,10,0,0,177,178,
        5,38,0,0,178,212,3,14,7,11,179,180,10,9,0,0,180,181,7,6,0,0,181,
        212,3,14,7,10,182,183,10,8,0,0,183,184,5,42,0,0,184,212,3,14,7,9,
        185,186,10,7,0,0,186,187,5,43,0,0,187,212,3,14,7,8,188,189,10,6,
        0,0,189,190,5,44,0,0,190,212,3,14,7,7,191,192,10,5,0,0,192,193,5,
        45,0,0,193,212,3,14,7,6,194,195,10,4,0,0,195,196,5,46,0,0,196,212,
        3,14,7,5,197,198,10,3,0,0,198,199,5,47,0,0,199,212,3,14,7,4,200,
        202,10,21,0,0,201,203,3,16,8,0,202,201,1,0,0,0,203,204,1,0,0,0,204,
        202,1,0,0,0,204,205,1,0,0,0,205,212,1,0,0,0,206,207,10,20,0,0,207,
        208,5,17,0,0,208,212,3,28,14,0,209,210,10,18,0,0,210,212,5,19,0,
        0,211,158,1,0,0,0,211,161,1,0,0,0,211,164,1,0,0,0,211,167,1,0,0,
        0,211,170,1,0,0,0,211,173,1,0,0,0,211,176,1,0,0,0,211,179,1,0,0,
        0,211,182,1,0,0,0,211,185,1,0,0,0,211,188,1,0,0,0,211,191,1,0,0,
        0,211,194,1,0,0,0,211,197,1,0,0,0,211,200,1,0,0,0,211,206,1,0,0,
        0,211,209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,
        0,214,15,1,0,0,0,215,213,1,0,0,0,216,217,5,15,0,0,217,218,3,14,7,
        0,218,219,5,16,0,0,219,227,1,0,0,0,220,221,5,15,0,0,221,222,3,14,
        7,0,222,223,5,5,0,0,223,224,3,14,7,0,224,225,5,16,0,0,225,227,1,
        0,0,0,226,216,1,0,0,0,226,220,1,0,0,0,227,17,1,0,0,0,228,233,3,14,
        7,0,229,230,5,8,0,0,230,232,3,14,7,0,231,229,1,0,0,0,232,235,1,0,
        0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,252,1,0,0,0,235,233,1,0,
        0,0,236,237,3,14,7,0,237,238,5,51,0,0,238,239,3,14,7,0,239,252,1,
        0,0,0,240,241,3,14,7,0,241,242,5,42,0,0,242,247,3,20,10,0,243,244,
        5,8,0,0,244,246,3,20,10,0,245,243,1,0,0,0,246,249,1,0,0,0,247,245,
        1,0,0,0,247,248,1,0,0,0,248,252,1,0,0,0,249,247,1,0,0,0,250,252,
        1,0,0,0,251,228,1,0,0,0,251,236,1,0,0,0,251,240,1,0,0,0,251,250,
        1,0,0,0,252,19,1,0,0,0,253,258,3,22,11,0,254,255,5,52,0,0,255,258,
        3,14,7,0,256,258,3,24,12,0,257,253,1,0,0,0,257,254,1,0,0,0,257,256,
        1,0,0,0,258,21,1,0,0,0,259,260,3,28,14,0,260,261,5,53,0,0,261,262,
        3,14,7,0,262,23,1,0,0,0,263,264,5,54,0,0,264,265,3,26,13,0,265,266,
        5,55,0,0,266,267,3,14,7,0,267,25,1,0,0,0,268,271,3,30,15,0,269,271,
        3,28,14,0,270,268,1,0,0,0,270,269,1,0,0,0,271,27,1,0,0,0,272,281,
        5,63,0,0,273,276,5,63,0,0,274,277,3,32,16,0,275,277,5,63,0,0,276,
        274,1,0,0,0,276,275,1,0,0,0,277,278,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,281,1,0,0,0,280,272,1,0,0,0,280,273,1,0,0,0,281,
        29,1,0,0,0,282,283,3,28,14,0,283,284,5,7,0,0,284,289,3,14,7,0,285,
        286,5,8,0,0,286,288,3,14,7,0,287,285,1,0,0,0,288,291,1,0,0,0,289,
        287,1,0,0,0,289,290,1,0,0,0,290,292,1,0,0,0,291,289,1,0,0,0,292,
        293,5,9,0,0,293,299,1,0,0,0,294,295,3,28,14,0,295,296,5,7,0,0,296,
        297,5,9,0,0,297,299,1,0,0,0,298,282,1,0,0,0,298,294,1,0,0,0,299,
        31,1,0,0,0,300,301,5,56,0,0,301,302,5,2,0,0,302,303,3,14,7,0,303,
        304,5,3,0,0,304,33,1,0,0,0,305,312,5,62,0,0,306,312,5,57,0,0,307,
        312,5,58,0,0,308,312,5,59,0,0,309,312,5,60,0,0,310,312,5,61,0,0,
        311,305,1,0,0,0,311,306,1,0,0,0,311,307,1,0,0,0,311,308,1,0,0,0,
        311,309,1,0,0,0,311,310,1,0,0,0,312,35,1,0,0,0,29,38,40,45,48,54,
        61,69,74,87,107,112,124,131,156,204,211,213,226,233,247,251,257,
        270,276,278,280,289,298,311
    ]

class HardScriptParser ( Parser ):

    grammarFileName = "HardScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'component'", "'{'", "'}'", "'interface'", 
                     "':'", "'->'", "'('", "','", "')'", "'auto'", "'for'", 
                     "'wire'", "'of'", "'bundle'", "'['", "']'", "'.'", 
                     "'#-'", "'-#'", "'+'", "'-'", "'~'", "'!'", "'**'", 
                     "'*'", "'/'", "'%'", "'>>'", "'<<'", "'>>>'", "'<<<'", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'&'", 
                     "'^~'", "'~^'", "'^'", "'|'", "'&&'", "'||'", "'::'", 
                     "'<>'", "'<+>'", "'if'", "'then'", "'else'", "'..'", 
                     "'when'", "'in'", "'let'", "'='", "'$'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOLEAN", "BIN_NUMBER", "HEX_NUMBER", 
                      "OCT_NUMBER", "DEC_NUMBER", "UNSIGNED_INTEGER", "ID", 
                      "WHITE_SPACE", "COMMENT" ]

    RULE_design = 0
    RULE_component = 1
    RULE_component_type = 2
    RULE_attributes = 3
    RULE_element = 4
    RULE_explicit_data_element = 5
    RULE_primary_symbol_list = 6
    RULE_expression = 7
    RULE_selector = 8
    RULE_list = 9
    RULE_qualifier = 10
    RULE_iterator = 11
    RULE_binding = 12
    RULE_symbol = 13
    RULE_primary_symbol = 14
    RULE_param_symbol = 15
    RULE_interpolation = 16
    RULE_number = 17

    ruleNames =  [ "design", "component", "component_type", "attributes", 
                   "element", "explicit_data_element", "primary_symbol_list", 
                   "expression", "selector", "list", "qualifier", "iterator", 
                   "binding", "symbol", "primary_symbol", "param_symbol", 
                   "interpolation", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    BOOLEAN=57
    BIN_NUMBER=58
    HEX_NUMBER=59
    OCT_NUMBER=60
    DEC_NUMBER=61
    UNSIGNED_INTEGER=62
    ID=63
    WHITE_SPACE=64
    COMMENT=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DesignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ComponentContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ComponentContext,i)


        def binding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.BindingContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.BindingContext,i)


        def getRuleIndex(self):
            return HardScriptParser.RULE_design

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesign" ):
                listener.enterDesign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesign" ):
                listener.exitDesign(self)




    def design(self):

        localctx = HardScriptParser.DesignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_design)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4]:
                    self.state = 36
                    self.component()
                    pass
                elif token in [54]:
                    self.state = 37
                    self.binding()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509482002) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.kind = None # Token
            self.type_ = None # ExpressionContext

        def ID(self):
            return self.getToken(HardScriptParser.ID, 0)

        def attributes(self):
            return self.getTypedRuleContext(HardScriptParser.AttributesContext,0)


        def component_type(self):
            return self.getTypedRuleContext(HardScriptParser.Component_typeContext,0)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ElementContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ElementContext,i)


        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HardScriptParser.RULE_component

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent" ):
                listener.enterComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent" ):
                listener.exitComponent(self)




    def component(self):

        localctx = HardScriptParser.ComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_component)
        self._la = 0 # Token type
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                localctx.kind = self.match(HardScriptParser.T__0)
                self.state = 43
                self.match(HardScriptParser.ID)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 44
                    self.attributes()


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 47
                    self.component_type()


                self.state = 50
                self.match(HardScriptParser.T__1)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -125819314573616000) != 0):
                    self.state = 51
                    self.element()
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.match(HardScriptParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                localctx.kind = self.match(HardScriptParser.T__3)
                self.state = 59
                self.match(HardScriptParser.ID)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 60
                    self.attributes()


                self.state = 63
                self.match(HardScriptParser.T__4)
                self.state = 64
                localctx.type_ = self.expression(0)
                self.state = 65
                self.match(HardScriptParser.T__1)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -125819314573616000) != 0):
                    self.state = 66
                    self.element()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(HardScriptParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.from_ = None # ExpressionContext
            self.to = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ExpressionContext,i)


        def getRuleIndex(self):
            return HardScriptParser.RULE_component_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent_type" ):
                listener.enterComponent_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent_type" ):
                listener.exitComponent_type(self)




    def component_type(self):

        localctx = HardScriptParser.Component_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_component_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(HardScriptParser.T__4)
            self.state = 77
            localctx.from_ = self.expression(0)
            self.state = 78
            self.match(HardScriptParser.T__5)
            self.state = 79
            localctx.to = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HardScriptParser.ID)
            else:
                return self.getToken(HardScriptParser.ID, i)

        def getRuleIndex(self):
            return HardScriptParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)




    def attributes(self):

        localctx = HardScriptParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(HardScriptParser.T__6)
            self.state = 82
            self.match(HardScriptParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 83
                self.match(HardScriptParser.T__7)
                self.state = 84
                self.match(HardScriptParser.ID)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(HardScriptParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_element

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MixedInstantiationContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMixedInstantiation" ):
                listener.enterMixedInstantiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMixedInstantiation" ):
                listener.exitMixedInstantiation(self)


    class LoopContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def iterator(self):
            return self.getTypedRuleContext(HardScriptParser.IteratorContext,0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ElementContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ElementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)


    class BindingStatementContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def binding(self):
            return self.getTypedRuleContext(HardScriptParser.BindingContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBindingStatement" ):
                listener.enterBindingStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBindingStatement" ):
                listener.exitBindingStatement(self)


    class DataInstantiationContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def explicit_data_element(self):
            return self.getTypedRuleContext(HardScriptParser.Explicit_data_elementContext,0)

        def primary_symbol_list(self):
            return self.getTypedRuleContext(HardScriptParser.Primary_symbol_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataInstantiation" ):
                listener.enterDataInstantiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataInstantiation" ):
                listener.exitDataInstantiation(self)


    class ComponentInstantiationContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponentInstantiation" ):
                listener.enterComponentInstantiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponentInstantiation" ):
                listener.exitComponentInstantiation(self)



    def element(self):

        localctx = HardScriptParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = HardScriptParser.BindingStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.binding()
                pass

            elif la_ == 2:
                localctx = HardScriptParser.DataInstantiationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.explicit_data_element()
                pass

            elif la_ == 3:
                localctx = HardScriptParser.DataInstantiationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(HardScriptParser.T__9)
                self.state = 95
                self.primary_symbol_list()
                pass

            elif la_ == 4:
                localctx = HardScriptParser.MixedInstantiationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(HardScriptParser.T__9)
                self.state = 97
                self.expression(0)
                pass

            elif la_ == 5:
                localctx = HardScriptParser.ComponentInstantiationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.expression(0)
                pass

            elif la_ == 6:
                localctx = HardScriptParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.match(HardScriptParser.T__10)
                self.state = 100
                self.match(HardScriptParser.T__6)
                self.state = 101
                self.iterator()
                self.state = 102
                self.match(HardScriptParser.T__8)
                self.state = 103
                self.match(HardScriptParser.T__1)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -125819314573616000) != 0):
                    self.state = 104
                    self.element()
                    self.state = 109
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 110
                self.match(HardScriptParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_data_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.kind = None # Token
            self.type_ = None # SymbolContext

        def primary_symbol_list(self):
            return self.getTypedRuleContext(HardScriptParser.Primary_symbol_listContext,0)


        def symbol(self):
            return self.getTypedRuleContext(HardScriptParser.SymbolContext,0)


        def getRuleIndex(self):
            return HardScriptParser.RULE_explicit_data_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_data_element" ):
                listener.enterExplicit_data_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_data_element" ):
                listener.exitExplicit_data_element(self)




    def explicit_data_element(self):

        localctx = HardScriptParser.Explicit_data_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_explicit_data_element)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                localctx.kind = self.match(HardScriptParser.T__11)
                self.state = 115
                self.primary_symbol_list()
                self.state = 116
                self.match(HardScriptParser.T__12)
                self.state = 117
                localctx.type_ = self.symbol()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                localctx.kind = self.match(HardScriptParser.T__13)
                self.state = 120
                self.primary_symbol_list()
                self.state = 121
                self.match(HardScriptParser.T__12)
                self.state = 122
                localctx.type_ = self.symbol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_symbol_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_symbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.Primary_symbolContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.Primary_symbolContext,i)


        def getRuleIndex(self):
            return HardScriptParser.RULE_primary_symbol_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_symbol_list" ):
                listener.enterPrimary_symbol_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_symbol_list" ):
                listener.exitPrimary_symbol_list(self)




    def primary_symbol_list(self):

        localctx = HardScriptParser.Primary_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primary_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.primary_symbol()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 127
                self.match(HardScriptParser.T__7)
                self.state = 128
                self.primary_symbol()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AccessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)

        def selector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.SelectorContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.SelectorContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessExpr" ):
                listener.enterAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessExpr" ):
                listener.exitAccessExpr(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(HardScriptParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)


    class BinaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.lhs = None # ExpressionContext
            self.op = None # Token
            self.rhs = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpr" ):
                listener.enterBinaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpr" ):
                listener.exitBinaryExpr(self)


    class SymbolExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def symbol(self):
            return self.getTypedRuleContext(HardScriptParser.SymbolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbolExpr" ):
                listener.enterSymbolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbolExpr" ):
                listener.exitSymbolExpr(self)


    class ListExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(HardScriptParser.ListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)


    class FieldExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)

        def primary_symbol(self):
            return self.getTypedRuleContext(HardScriptParser.Primary_symbolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldExpr" ):
                listener.enterFieldExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldExpr" ):
                listener.exitFieldExpr(self)


    class ConditionalExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.cond = None # ExpressionContext
            self.thenBranch = None # ExpressionContext
            self.elseBranch = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpr" ):
                listener.enterConditionalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpr" ):
                listener.exitConditionalExpr(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HardScriptParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                localctx = HardScriptParser.SymbolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 135
                self.symbol()
                pass
            elif token in [57, 58, 59, 60, 61, 62]:
                localctx = HardScriptParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.number()
                pass
            elif token in [15]:
                localctx = HardScriptParser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(HardScriptParser.T__14)
                self.state = 138
                self.list_()
                self.state = 139
                self.match(HardScriptParser.T__15)
                pass
            elif token in [18]:
                localctx = HardScriptParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                localctx.op = self.match(HardScriptParser.T__17)
                self.state = 142
                self.expression(19)
                pass
            elif token in [20, 21, 22, 23]:
                localctx = HardScriptParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.expression(17)
                pass
            elif token in [48]:
                localctx = HardScriptParser.ConditionalExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(HardScriptParser.T__47)
                self.state = 146
                localctx.cond = self.expression(0)
                self.state = 147
                self.match(HardScriptParser.T__48)
                self.state = 148
                localctx.thenBranch = self.expression(0)
                self.state = 149
                self.match(HardScriptParser.T__49)
                self.state = 150
                localctx.elseBranch = self.expression(2)
                pass
            elif token in [7]:
                localctx = HardScriptParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(HardScriptParser.T__6)
                self.state = 153
                self.expression(0)
                self.state = 154
                self.match(HardScriptParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 211
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 158
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 159
                        localctx.op = self.match(HardScriptParser.T__23)
                        self.state = 160
                        localctx.rhs = self.expression(17)
                        pass

                    elif la_ == 2:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 162
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 163
                        localctx.rhs = self.expression(16)
                        pass

                    elif la_ == 3:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 165
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        localctx.rhs = self.expression(15)
                        pass

                    elif la_ == 4:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 168
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        localctx.rhs = self.expression(14)
                        pass

                    elif la_ == 5:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 171
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 172
                        localctx.rhs = self.expression(13)
                        pass

                    elif la_ == 6:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 174
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==37):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        localctx.rhs = self.expression(12)
                        pass

                    elif la_ == 7:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 176
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 177
                        localctx.op = self.match(HardScriptParser.T__37)
                        self.state = 178
                        localctx.rhs = self.expression(11)
                        pass

                    elif la_ == 8:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 180
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 181
                        localctx.rhs = self.expression(10)
                        pass

                    elif la_ == 9:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 183
                        localctx.op = self.match(HardScriptParser.T__41)
                        self.state = 184
                        localctx.rhs = self.expression(9)
                        pass

                    elif la_ == 10:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 186
                        localctx.op = self.match(HardScriptParser.T__42)
                        self.state = 187
                        localctx.rhs = self.expression(8)
                        pass

                    elif la_ == 11:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 189
                        localctx.op = self.match(HardScriptParser.T__43)
                        self.state = 190
                        localctx.rhs = self.expression(7)
                        pass

                    elif la_ == 12:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 192
                        localctx.op = self.match(HardScriptParser.T__44)
                        self.state = 193
                        localctx.rhs = self.expression(6)
                        pass

                    elif la_ == 13:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 195
                        localctx.op = self.match(HardScriptParser.T__45)
                        self.state = 196
                        localctx.rhs = self.expression(5)
                        pass

                    elif la_ == 14:
                        localctx = HardScriptParser.BinaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 197
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 198
                        localctx.op = self.match(HardScriptParser.T__46)
                        self.state = 199
                        localctx.rhs = self.expression(4)
                        pass

                    elif la_ == 15:
                        localctx = HardScriptParser.AccessExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 200
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 202 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 201
                                self.selector()

                            else:
                                raise NoViableAltException(self)
                            self.state = 204 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                        pass

                    elif la_ == 16:
                        localctx = HardScriptParser.FieldExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 206
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 207
                        self.match(HardScriptParser.T__16)
                        self.state = 208
                        self.primary_symbol()
                        pass

                    elif la_ == 17:
                        localctx = HardScriptParser.UnaryExprContext(self, HardScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 209
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 210
                        localctx.op = self.match(HardScriptParser.T__18)
                        pass

             
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_selector

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PartSelectorContext(SelectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.SelectorContext
            super().__init__(parser)
            self.from_ = None # ExpressionContext
            self.to = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartSelector" ):
                listener.enterPartSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartSelector" ):
                listener.exitPartSelector(self)


    class BitSelectorContext(SelectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.SelectorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitSelector" ):
                listener.enterBitSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitSelector" ):
                listener.exitBitSelector(self)



    def selector(self):

        localctx = HardScriptParser.SelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_selector)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = HardScriptParser.BitSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(HardScriptParser.T__14)
                self.state = 217
                self.expression(0)
                self.state = 218
                self.match(HardScriptParser.T__15)
                pass

            elif la_ == 2:
                localctx = HardScriptParser.PartSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(HardScriptParser.T__14)
                self.state = 221
                localctx.from_ = self.expression(0)
                self.state = 222
                self.match(HardScriptParser.T__4)
                self.state = 223
                localctx.to = self.expression(0)
                self.state = 224
                self.match(HardScriptParser.T__15)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyListContext(ListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ListContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyList" ):
                listener.enterEmptyList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyList" ):
                listener.exitEmptyList(self)


    class CommonListContext(ListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommonList" ):
                listener.enterCommonList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommonList" ):
                listener.exitCommonList(self)


    class RangeListContext(ListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ListContext
            super().__init__(parser)
            self.from_ = None # ExpressionContext
            self.to = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeList" ):
                listener.enterRangeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeList" ):
                listener.exitRangeList(self)


    class ListComprehensionContext(ListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.ListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)

        def qualifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.QualifierContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.QualifierContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListComprehension" ):
                listener.enterListComprehension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListComprehension" ):
                listener.exitListComprehension(self)



    def list_(self):

        localctx = HardScriptParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = HardScriptParser.CommonListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.expression(0)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 229
                    self.match(HardScriptParser.T__7)
                    self.state = 230
                    self.expression(0)
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = HardScriptParser.RangeListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                localctx.from_ = self.expression(0)
                self.state = 237
                self.match(HardScriptParser.T__50)
                self.state = 238
                localctx.to = self.expression(0)
                pass

            elif la_ == 3:
                localctx = HardScriptParser.ListComprehensionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.expression(0)
                self.state = 241
                self.match(HardScriptParser.T__41)
                self.state = 242
                self.qualifier()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 243
                    self.match(HardScriptParser.T__7)
                    self.state = 244
                    self.qualifier()
                    self.state = 249
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                localctx = HardScriptParser.EmptyListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_qualifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FilterContext(QualifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.QualifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter" ):
                listener.enterFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter" ):
                listener.exitFilter(self)


    class LocalBindingContext(QualifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.QualifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def binding(self):
            return self.getTypedRuleContext(HardScriptParser.BindingContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalBinding" ):
                listener.enterLocalBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalBinding" ):
                listener.exitLocalBinding(self)


    class GeneratorContext(QualifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.QualifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def iterator(self):
            return self.getTypedRuleContext(HardScriptParser.IteratorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenerator" ):
                listener.enterGenerator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenerator" ):
                listener.exitGenerator(self)



    def qualifier(self):

        localctx = HardScriptParser.QualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_qualifier)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                localctx = HardScriptParser.GeneratorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.iterator()
                pass
            elif token in [52]:
                localctx = HardScriptParser.FilterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(HardScriptParser.T__51)
                self.state = 255
                self.expression(0)
                pass
            elif token in [54]:
                localctx = HardScriptParser.LocalBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.binding()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IteratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_symbol(self):
            return self.getTypedRuleContext(HardScriptParser.Primary_symbolContext,0)


        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HardScriptParser.RULE_iterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterator" ):
                listener.enterIterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterator" ):
                listener.exitIterator(self)




    def iterator(self):

        localctx = HardScriptParser.IteratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_iterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.primary_symbol()
            self.state = 260
            self.match(HardScriptParser.T__52)
            self.state = 261
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self):
            return self.getTypedRuleContext(HardScriptParser.SymbolContext,0)


        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HardScriptParser.RULE_binding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinding" ):
                listener.enterBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinding" ):
                listener.exitBinding(self)




    def binding(self):

        localctx = HardScriptParser.BindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(HardScriptParser.T__53)
            self.state = 264
            self.symbol()
            self.state = 265
            self.match(HardScriptParser.T__54)
            self.state = 266
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_symbol

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParamSymbolContext(SymbolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.SymbolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def param_symbol(self):
            return self.getTypedRuleContext(HardScriptParser.Param_symbolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamSymbol" ):
                listener.enterParamSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamSymbol" ):
                listener.exitParamSymbol(self)


    class PrimarySymbolContext(SymbolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.SymbolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary_symbol(self):
            return self.getTypedRuleContext(HardScriptParser.Primary_symbolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimarySymbol" ):
                listener.enterPrimarySymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimarySymbol" ):
                listener.exitPrimarySymbol(self)



    def symbol(self):

        localctx = HardScriptParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_symbol)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = HardScriptParser.ParamSymbolContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.param_symbol()
                pass

            elif la_ == 2:
                localctx = HardScriptParser.PrimarySymbolContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.primary_symbol()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_primary_symbol

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentifierContext(Primary_symbolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.Primary_symbolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HardScriptParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)


    class InterpolatedContext(Primary_symbolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.Primary_symbolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HardScriptParser.ID)
            else:
                return self.getToken(HardScriptParser.ID, i)
        def interpolation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.InterpolationContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.InterpolationContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated" ):
                listener.enterInterpolated(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated" ):
                listener.exitInterpolated(self)



    def primary_symbol(self):

        localctx = HardScriptParser.Primary_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primary_symbol)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = HardScriptParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(HardScriptParser.ID)
                pass

            elif la_ == 2:
                localctx = HardScriptParser.InterpolatedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(HardScriptParser.ID)
                self.state = 276 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 276
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [56]:
                            self.state = 274
                            self.interpolation()
                            pass
                        elif token in [63]:
                            self.state = 275
                            self.match(HardScriptParser.ID)
                            pass
                        else:
                            raise NoViableAltException(self)


                    else:
                        raise NoViableAltException(self)
                    self.state = 278 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_symbol(self):
            return self.getTypedRuleContext(HardScriptParser.Primary_symbolContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HardScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HardScriptParser.ExpressionContext,i)


        def getRuleIndex(self):
            return HardScriptParser.RULE_param_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_symbol" ):
                listener.enterParam_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_symbol" ):
                listener.exitParam_symbol(self)




    def param_symbol(self):

        localctx = HardScriptParser.Param_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param_symbol)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.primary_symbol()
                self.state = 283
                self.match(HardScriptParser.T__6)
                self.state = 284
                self.expression(0)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 285
                    self.match(HardScriptParser.T__7)
                    self.state = 286
                    self.expression(0)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 292
                self.match(HardScriptParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.primary_symbol()
                self.state = 295
                self.match(HardScriptParser.T__6)
                self.state = 296
                self.match(HardScriptParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterpolationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(HardScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HardScriptParser.RULE_interpolation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolation" ):
                listener.enterInterpolation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolation" ):
                listener.exitInterpolation(self)




    def interpolation(self):

        localctx = HardScriptParser.InterpolationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_interpolation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(HardScriptParser.T__55)
            self.state = 301
            self.match(HardScriptParser.T__1)
            self.state = 302
            self.expression(0)
            self.state = 303
            self.match(HardScriptParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HardScriptParser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BitVectorNumberContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BIN_NUMBER(self):
            return self.getToken(HardScriptParser.BIN_NUMBER, 0)
        def HEX_NUMBER(self):
            return self.getToken(HardScriptParser.HEX_NUMBER, 0)
        def OCT_NUMBER(self):
            return self.getToken(HardScriptParser.OCT_NUMBER, 0)
        def DEC_NUMBER(self):
            return self.getToken(HardScriptParser.DEC_NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitVectorNumber" ):
                listener.enterBitVectorNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitVectorNumber" ):
                listener.exitBitVectorNumber(self)


    class IntNumberContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNSIGNED_INTEGER(self):
            return self.getToken(HardScriptParser.UNSIGNED_INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntNumber" ):
                listener.enterIntNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntNumber" ):
                listener.exitIntNumber(self)


    class BoolNumberContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HardScriptParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(HardScriptParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolNumber" ):
                listener.enterBoolNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolNumber" ):
                listener.exitBoolNumber(self)



    def number(self):

        localctx = HardScriptParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_number)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                localctx = HardScriptParser.IntNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(HardScriptParser.UNSIGNED_INTEGER)
                pass
            elif token in [57]:
                localctx = HardScriptParser.BoolNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(HardScriptParser.BOOLEAN)
                pass
            elif token in [58]:
                localctx = HardScriptParser.BitVectorNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.match(HardScriptParser.BIN_NUMBER)
                pass
            elif token in [59]:
                localctx = HardScriptParser.BitVectorNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 308
                self.match(HardScriptParser.HEX_NUMBER)
                pass
            elif token in [60]:
                localctx = HardScriptParser.BitVectorNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 309
                self.match(HardScriptParser.OCT_NUMBER)
                pass
            elif token in [61]:
                localctx = HardScriptParser.BitVectorNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 310
                self.match(HardScriptParser.DEC_NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 18)
         




