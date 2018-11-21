#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides an :class:`Adapter` for :class:`EUI` instances, supporting
both 48-bit and 64-bit addresses, and consists of two components: an enum
:class:`EUIOctets` and the :class:`EUIAdapter`, wherein the former is intended
to be the primary argument for the latter.

While explicitly passing an :class:`IntEnum` instance to the constructor of
:class:`EUIAdapter` is not required, value equivalence to a member within
the enum is interpreted as an enforceable condition during construction of
an :class:`EUIAdapter` instance.
"""

__all__ = ['EUIAdapter', 'EUIOctets']
__version__ = '0.1.2'
__author__ = 'Sean McVeigh'

from enum import IntEnum
from netaddr import EUI
from construct import Adapter, Path, Subconstruct, BytesInteger


class EUIOctets(IntEnum):
    """
    An :class:`IntEnum` defining the byte length for an unsigned integer
    representing both a 48-bit and a 64-bit address.

    The purpose of this class is not only to standardize argument convention
    but also to enforce passed values provided to :class:`EUIAdapter`'s
    constructor.
    """

    EUI_48 = 6
    EUI_64 = 8


class EUIAdapter(Adapter):
    """
    An :class:`Adapter` for 48-bit or 64-bit :class:`EUI`.
    """

    def __init__(self, octets: int=EUIOctets.EUI_48, swapped: bool=False):
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
