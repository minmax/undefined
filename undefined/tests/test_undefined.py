from __future__ import annotations

from typing import Any

import pytest
from typing_extensions import assert_type

from undefined import Undefined, UndefinedError, undefined


def test_undefined() -> None:
    mapping: dict[Any, Any] = {}
    assert mapping.get("", undefined) is undefined


def test_types() -> None:
    mapping: dict[str, None | Undefined] = {"null": None}

    if (val := mapping.get("null", undefined)) is undefined:
        assert_type(val, Undefined)
    else:
        assert_type(val, None)


def test_eq() -> None:
    with pytest.raises(UndefinedError):
        assert undefined == "None"


def test_bool() -> None:
    with pytest.raises(UndefinedError):
        bool(undefined)


def test_str() -> None:
    with pytest.raises(UndefinedError):
        str(undefined)


def test_is_instance_self() -> None:
    # its ok in runtime, but wrong on typing
    assert isinstance(undefined, Undefined)  # pyright: ignore[reportArgumentType]


def test_isinstance() -> None:
    with pytest.raises(UndefinedError, match="Cannot isinstance undefined!"):
        isinstance(object, Undefined)  # pyright: ignore[reportArgumentType]


def test_issubclass() -> None:
    with pytest.raises(UndefinedError, match="Cannot issubclass undefined!"):
        issubclass(object, Undefined)  # pyright: ignore[reportArgumentType]


def test_hash_cls() -> None:
    assert isinstance(hash(Undefined), int)


def test_hash_instance() -> None:
    with pytest.raises(UndefinedError, match="Cannot __hash__ undefined"):
        hash(undefined)
