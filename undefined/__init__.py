from typing import TYPE_CHECKING, NoReturn

from typing_extensions import TypeAlias, final

__version__ = "0.1.3"


__all__ = ("UndefinedError", "Undefined", "undefined")


class UndefinedError(TypeError):
    pass


@final
class _UndefinedMeta(type):
    def __subclasscheck__(cls, subclass: type, /) -> NoReturn:
        msg = "Cannot issubclass undefined!"
        raise UndefinedError(msg)

    def __instancecheck__(cls, instance: object, /) -> NoReturn:
        msg = "Cannot isinstance undefined!"
        raise UndefinedError(msg)


@final
class _Undefined(metaclass=_UndefinedMeta):
    """Simply a global object that act as undefined."""

    __slots__ = ()  # Make object immutable

    def __eq__(self, other: object, /) -> NoReturn:
        msg = "Cannot compare undefined"
        raise UndefinedError(msg)

    def __repr__(self) -> str:
        return "<Undefined>"

    def __bool__(self) -> NoReturn:
        msg = "Undefined is not defined, neither True, nor False."
        raise UndefinedError(msg)

    def __str__(self) -> NoReturn:
        msg = "Cannot represent undefined !"
        raise UndefinedError(msg)


_Undefined.__qualname__ = "Undefined"

if TYPE_CHECKING:
    Undefined: TypeAlias = type[_Undefined]
    undefined = _Undefined
else:
    Undefined = _Undefined
    undefined = _Undefined()
