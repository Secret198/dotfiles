from _typeshed import Incomplete

from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet
from antlr4.atn.ATNState import DecisionState as DecisionState, StarLoopEntryState as StarLoopEntryState
from antlr4.dfa.DFAState import DFAState as DFAState
from antlr4.error.Errors import IllegalStateException as IllegalStateException

class DFA:
    atnStartState: Incomplete
    decision: Incomplete
    s0: Incomplete
    precedenceDfa: bool
    def __init__(self, atnStartState: DecisionState, decision: int = 0) -> None: ...
    def getPrecedenceStartState(self, precedence: int): ...
    def setPrecedenceStartState(self, precedence: int, startState: DFAState): ...
    def setPrecedenceDfa(self, precedenceDfa: bool): ...
    @property
    def states(self): ...
    def sortedStates(self): ...
    def toString(self, literalNames: list[str] | None = None, symbolicNames: list[str] | None = None): ...
    def toLexerString(self): ...
