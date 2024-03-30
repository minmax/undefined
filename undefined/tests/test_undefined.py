from __future__ import annotations

from typing import Any

import pytest
from typing_extensions import assert_type

from undefined import Undefined, undefined


def test_undefined() -> None:
    mapping: dict[Any, Any] = {}
    assert mapping.get("", undefined) is undefined


def test_types() -> None:
    mapping: dict[str, None | Undefined] = {"null": None}

    if (val := mapping.get("null", undefined)) is undefined:
        assert_type(val, Undefined)
    else:
        assert_type(val, None)


def test_is_instance() -> None:
    with pytest.raises(TypeError):
        assert isinstance(undefined, Undefined)  # pyright: ignore[reportArgumentType]


def test_bool() -> None:
    with pytest.raises(NotImplementedError):
        bool(undefined)


def test_str() -> None:
    with pytest.raises(NotImplementedError):
        str(undefined)
