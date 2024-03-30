"""a simple package."""

from typing import TYPE_CHECKING, NoReturn

from typing_extensions import TypeAlias, final

__version__ = "0.0.7"


@final
class _Undefined:
    """Simply a global object that act as undefined."""

    def __eq__(self, other: object) -> NoReturn:
        msg = "Cannot compare undefined"
        raise NotImplementedError(msg)

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __bool__(self) -> NoReturn:
        msg = "Undefined is not defined, neither True, nor False."
        raise NotImplementedError(msg)

    def __str__(self) -> NoReturn:
        msg = "Cannot represent undefined !"
        raise NotImplementedError(msg)


Undefined: TypeAlias = type[_Undefined]

if TYPE_CHECKING:
    undefined: Undefined
else:
    undefined = _Undefined()
