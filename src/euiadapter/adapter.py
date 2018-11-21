#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module defines an :class:`Adapter` subclass :class:`EUIAdapter` for
representing a :class:`EUI` assuming an unsigned 48-bit or 64-bit integer
representation.

Encoding and decoding is passed to an underlying :class:`BytesInteger`
:class:`Subconstruct` whose parameters are set during :class:`EUIAdapter`'s
construction. Explicitly, these parameters are an :class:`IntEnum` subclass
:class:`EUIOctets` defining the octet length of the integer and a boolean
defining the endianness of the integer.

While explicitly passing an :class:`IntEnum` instance to the constructor of
:class:`EUIAdapter` is not required, value equivalence to a member within
the enum is interpreted as an enforceable condition during construction of
an :class:`EUIAdapter` instance.
"""

__all__ = ['EUIAdapter']
__version__ = '0.2.2'
__author__ = 'Sean McVeigh'

from netaddr import EUI
from typing import Union
from construct import Adapter, Path, Subconstruct, BytesInteger
from .enum import EUIOctets


class EUIAdapter(Adapter):
    """
    An :class:`Adapter` for 48-bit or 64-bit :class:`EUI`.
    """

    def __init__(self, octets: Union[int, EUIOctets], swapped: bool):
        """
        Utilize :class:`BytesInteger` as :class:`Subconstruct`.

        :param octets: number of bytes for integer
        :param swapped: invert byte ordering (endianness)
        :raise ValueError: if neither 48-bit nor 64-bit EUI
        """
        length = EUIOctets(octets)
        subcon = BytesInteger(length, False, swapped)
        super(EUIAdapter, self).__init__(subcon)

    def _encode(self, obj: EUI, context: Subconstruct, path: Path) -> int:
        """
        Encode :class:`EUI` as :class:`int` for passing to subconstruct.

        :param obj: instance
        :param context: wrapper
        :return: buffer
        """
        return int(obj)

    def _decode(self, obj: int, context: Subconstruct, path: Path) -> EUI:
        """
        Decode :class:`EUI` from :class:`int` for passing to subconstruct.

        :param obj: buffer
        :param context: wrapper
        :return: instance
        """
        return EUI(obj)
