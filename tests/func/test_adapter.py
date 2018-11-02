#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from netaddr import EUI
from euiadapter import EUIAdapter


def test_parse(buffer: bytes, instance: EUI, octets: int, swapped: bool):

    if octets in (6, 8):
        adapter = EUIAdapter(octets, swapped)
        result = adapter.parse(buffer)
        assert instance == result

    else:
        with pytest.raises(ValueError):
            EUIAdapter(octets, swapped)


def test_build(instance: EUI, buffer: bytes, octets: int, swapped: bool):

    if octets in (6, 8):
        adapter = EUIAdapter(octets, swapped)
        result = adapter.build(instance)
        assert buffer == result

    else:
        with pytest.raises(ValueError):
            EUIAdapter(octets, swapped)
