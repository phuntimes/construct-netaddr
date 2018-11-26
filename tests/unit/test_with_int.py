#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from netaddr import EUI
from typing import Callable
from construct import Construct, Adapter, ExprAdapter, BytesInteger


Encoder = Callable[[EUI, Construct], int]


@pytest.fixture
def encoder() -> Encoder:

    def encode(obj: EUI, context: Construct) -> int:
        return obj.value

    return encode


Decoder = Callable[[int, Construct], EUI]


@pytest.fixture
def decoder() -> Decoder:

    def decode(obj: int, context: Construct) -> EUI:
        return EUI(obj)

    return decode


@pytest.fixture
def subcon(octets, swapped: bool):
    return BytesInteger(octets, False, swapped)


@pytest.fixture
def adapter(subcon: Construct, decoder: Decoder, encoder: Encoder) -> Adapter:
    return ExprAdapter(subcon, decoder, encoder)


def test_parse(buffer: bytes, adapter: Adapter, instance: EUI):
    actual = adapter.parse(buffer)
    assert actual == instance


def test_build(instance: EUI, adapter: Adapter, buffer: bytes):
    actual = adapter.build(instance)
    assert actual == buffer
