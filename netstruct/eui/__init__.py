#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This package provides an :class:`Adapter<construct.Adapter>` for
:class:`EUI<netaddr.EUI>` instances, supporting both 48-bit and 64-bit
addresses, and consists of two components: an enum :class:`EUIOctets` and
the :class:`EUIAdapter`, wherein the former is the primary argument for the
latter.
"""

__all__ = ['EUIAdapter', 'EUIOctets']
__version__ = '0.2.4'
__author__ = 'Sean McVeigh'

from .enum import EUIOctets
from .adapter import EUIAdapter
