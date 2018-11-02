#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import IntEnum
from netaddr import EUI
from construct import Subconstruct, Adapter, BytesInteger, Path


class EUIOctets(IntEnum):

    EUI_48 = 6
    EUI_64 = 8


class EUIAdapter(Adapter):
    """
    Adapter for 48-bit or 64-bit :class:`EUI` from :class:`int`.
    """

    def __init__(self, octets: int=EUIOctets.EUI_48, swapped: bool=False):
        """
        Utilize :class:`BytesInteger` as :class:`Subconstruct`.

        :param octets: number of bytes for integer
        :param swapped: invert byte ordering (endianness)
        :raise ValueError: if neither 48-bit nor 64-bit EUI
        """
        subcon = BytesInteger(EUIOctets(octets), False, swapped)
        super(EUIAdapter, self).__init__(subcon)

    def _encode(self, obj: EUI, context: Subconstruct, path: Path) -> int:
        """
        Encode :class:`EUI` as :class:`int`.

        :param obj: instance
        :param context: wrapper
        :return: buffer
        """
        return int(obj)

    def _decode(self, obj: int, context: Subconstruct, path: Path) -> EUI:
        """
        Decode :class:`EUI` from :class:`int`.

        :param obj: buffer
        :param context: wrapper
        :return: instance
        """
        return EUI(obj)
