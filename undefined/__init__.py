from typing import TYPE_CHECKING

from typing_extensions import TypeAlias

from . import _magic_obj

__version__ = "0.2.0"


__all__ = ("UndefinedError", "Undefined", "undefined")


UndefinedError = _magic_obj.UndefinedError


if TYPE_CHECKING:
    Undefined: TypeAlias = type[_magic_obj.Undefined]
    undefined = _magic_obj.Undefined
else:
    Undefined = _magic_obj.Undefined
    undefined = _magic_obj.Undefined()
