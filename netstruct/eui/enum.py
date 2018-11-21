#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides an :class:`IntEnum` to define the octet length for the
unsigned :class:`BytesInteger` utilized internally by the :class:`Adapter` for
:class:`EUI`.

The purpose of of the enum :class:`EUIOctets` is to not only standardize
argument convention for the adapter's constructor but also to enforce passed
values provided to the constructor during instantiation.
"""

__all__ = ['EUIOctets']
__version__ = '0.2.3'
__author__ = 'Sean McVeigh'

from enum import IntEnum
from netaddr import EUI
from construct import BytesInteger, Subconstruct


class EUIOctets(IntEnum):
    """
    An :class:`IntEnum` defining the byte length for an unsigned integer
    representing both a 48-bit and a 64-bit address.
    """

    EUI_48 = 6
    EUI_64 = 8
