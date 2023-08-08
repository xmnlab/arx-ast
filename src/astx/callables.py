from typing import List

from astx.base import (
    ASTKind,
    DataType,
    Expr,
    ExprType,
    SourceLocation,
    StatementType,
)
from astx.blocks import Block
from astx.modifiers import ScopeKind, VisibilityKind
from astx.variables import Variable


class Call(Expr):
    """AST class for function call."""

    def __init__(
        self,
        callee: str,
        args: List[Variable],
        loc: SourceLocation = SourceLocation(0, 0),
    ) -> None:
        """Initialize the Call instance."""
        super().__init__(loc)
        self.callee = callee
        self.args = args
        self.kind = ASTKind.CallKind


class FunctionPrototype(StatementType):
    """AST class for function prototype declaration."""

    name: str
    args: List[Variable]
    return_type: ExprType
    scope: ScopeKind
    visibility: VisibilityKind

    def __init__(
        self,
        name: str,
        args: List[Variable],
        return_type: ExprType,
        scope: ScopeKind = ScopeKind.global_,
        visibility: VisibilityKind = VisibilityKind.public,
        loc: SourceLocation = SourceLocation(0, 0),
    ) -> None:
        """Initialize the FunctionPrototype instance."""
        self.name = name
        self.args = args
        self.return_type = return_type
        self.line = loc.line
        self.kind = ASTKind.PrototypeKind
        self.scope = scope
        self.visibility = visibility


class Return(StatementType):
    """AST class for function `return` statement."""

    value: DataType

    def __init__(
        self, value: DataType, loc: SourceLocation = SourceLocation(0, 0)
    ) -> None:
        """Initialize the Return instance."""
        self.loc = loc
        self.value = value
        self.kind = ASTKind.ReturnKind


class Function(StatementType):
    """AST class for function definition."""

    prototype: FunctionPrototype
    body: Block

    def __init__(
        self,
        prototype: FunctionPrototype,
        body: Block,
        loc: SourceLocation = SourceLocation(0, 0),
    ) -> None:
        """Initialize the Function instance."""
        self.loc = loc
        self.prototype = prototype
        self.body = body
        self.kind = ASTKind.FunctionKind

    @property
    def name(self) -> str:
        return self.prototype.name
