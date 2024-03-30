"""
a simple package
"""


__version__ = '0.0.7'

from typing import NoReturn

class Undefined:
    """
    Simply a global object that act as undefined.
    """

    __version__ = __version__


    @property
    def Undefined(self):
        return self

    def __call__(self, value):
        return value is self

    def __eq__(self, other: object) -> NoReturn:
        raise NotImplementedError('Cannot compare undefined')

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __bool__(self)-> NoReturn:
        raise NotImplementedError('Undefined is not defined, neither True, nor False.')

    def __str__(self) -> NoReturn:
        raise NotImplementedError("Cannot represent undefined !")
