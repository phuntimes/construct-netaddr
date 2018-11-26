#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from netaddr import EUI
from netstruct import EUIAdapter


def test_parse(buffer: bytes, instance: EUI, octets: int, swapped: bool):

    if octets in (6, 8):
        adapter = EUIAdapter(octets, swapped)
        actual = adapter.parse(buffer)
        assert actual == instance

    else:
        with pytest.raises(ValueError):
            EUIAdapter(octets, swapped)


def test_build(instance: EUI, buffer: bytes, octets: int, swapped: bool):

    if octets in (6, 8):
        adapter = EUIAdapter(octets, swapped)
        actual = adapter.build(instance)
        assert actual == buffer

    else:
        with pytest.raises(ValueError):
            EUIAdapter(octets, swapped)
