"""
a simple package
"""

from typing import NoReturn


__version__ = '0.0.7'


class Undefined:
    """
    Simply a global object that act as undefined.
    """

    def __eq__(self, other: object) -> NoReturn:
        raise NotImplementedError('Cannot compare undefined')

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __bool__(self)-> NoReturn:
        raise NotImplementedError('Undefined is not defined, neither True, nor False.')

    def __str__(self) -> NoReturn:
        raise NotImplementedError("Cannot represent undefined !")
