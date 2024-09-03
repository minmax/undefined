from typing import NoReturn

from typing_extensions import final


class UndefinedError(TypeError):
    pass


@final
class UndefinedMeta(type):
    def __subclasscheck__(cls, subclass: type, /) -> NoReturn:
        msg = "Cannot issubclass undefined!"
        raise UndefinedError(msg)

    def __instancecheck__(cls, instance: object, /) -> NoReturn:
        msg = "Cannot isinstance undefined!"
        raise UndefinedError(msg)


@final
class Undefined(metaclass=UndefinedMeta):
    """Simply a global object that act as undefined."""

    __slots__ = ()  # Make object immutable

    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__}>"

    def __str__(self) -> NoReturn:
        msg = "Cannot represent undefined !"
        raise UndefinedError(msg)

    def __eq__(self, other: object, /) -> NoReturn:
        msg = "Cannot compare undefined"
        raise UndefinedError(msg)

    def __hash__(self) -> NoReturn:
        msg = "Cannot __hash__ undefined"
        raise UndefinedError(msg)

    def __bool__(self) -> NoReturn:
        msg = "Undefined is not defined, neither True, nor False."
        raise UndefinedError(msg)
