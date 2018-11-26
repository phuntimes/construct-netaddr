#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import random

from netaddr import EUI


@pytest.fixture(
    params=[
        pytest.param(False, id="big"),
        pytest.param(True, id="little"),
    ]
)
def swapped(request) -> bool:
    return request.param


@pytest.fixture(
    params=[
        pytest.param(
            i, id="{:d}-bit".format(8 * i)
        ) for i in range(5, 9)
    ]
)
def octets(request) -> int:
    return request.param


@pytest.fixture
def value(octets: int) -> int:
    return random.randint(0, 2 ** (8 * octets) - 1)


@pytest.fixture
def instance(value: int) -> EUI:
    return EUI(value)


@pytest.fixture
def byteorder(swapped: bool) -> str:
    return 'little' if swapped else 'big'


@pytest.fixture
def buffer(instance: EUI, swapped: bool) -> bytes:
    buffer = instance.packed
    return buffer[::-1] if swapped else buffer
    # return (value).to_bytes(octets, byteorder, signed=False)
