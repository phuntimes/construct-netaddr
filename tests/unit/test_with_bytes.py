#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from netaddr import EUI
from typing import Callable
from construct import Construct, Adapter, ExprAdapter, Bytes, ByteSwapped


Encoder = Callable[[EUI, Construct], bytes]


@pytest.fixture
def encoder(octets: int, byteorder: str) -> Encoder:

    def encode(obj: EUI, context: Construct) -> bytes:
        return (obj.value).to_bytes(octets, byteorder, signed=False)

    return encode


Decoder = Callable[[bytes, Construct], EUI]


@pytest.fixture
def decoder(byteorder: str) -> Decoder:

    def decode(obj: bytes, context: Construct) -> EUI:
        value = int.from_bytes(obj, byteorder, signed=False)
        return EUI(value)

    return decode


@pytest.fixture
def subcon(octets: int, swapped: bool) -> Construct:

    if octets not in (6, 8):
        pytest.xfail("neither 48-bit nor 64-bit EUI")

    if swapped:
        pytest.xfail("not swapping; why?")

    return ByteSwapped(Bytes(octets)) if swapped else Bytes(octets)


@pytest.fixture
def adapter(subcon: Construct, decoder: Decoder, encoder: Encoder) -> Adapter:
    return ExprAdapter(subcon, decoder, encoder)


def test_parse(buffer: bytes, instance: EUI, adapter: Adapter):
    result = adapter.parse(buffer)
    assert instance == result


def test_build(instance: EUI, buffer: bytes, adapter: Adapter):
    result = adapter.build(instance)
    assert buffer == result
