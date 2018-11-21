# construct-netaddr

[![Build Status](https://travis-ci.com/phuntimes/construct-netaddr.svg?branch=master)](https://travis-ci.com/phuntimes/construct-netaddr)
[![Coverage Status](https://coveralls.io/repos/github/phuntimes/construct-netaddr/badge.svg?branch=master)](https://coveralls.io/github/phuntimes/construct-netaddr?branch=master)

An extension library for [construct] defining an `Adapter` for the `EUI` class of [netaddr].
Supports both 48-bit and 64-bit addresses.

## Usage

Intended to be consistent with the `Adapter` API:

```python

from construct import Struct
from netstruct import EUIAdapter, EUIOctets


STRUCT = Struct(
    # ...
    mac=EUIAdapter(EUIOctets.EUI_48, False)
    # ...
)

```

## Testing

A full [py.test] suite exists:

 * **unit** for testing encoding and decoding with `ExprAdapter` via `bytes` and `int`.
 * **func** for testing encoding and decoding with `EUIAdapter`.


[construct]: https://github.com/construct/construct
[netaddr]: https://github.com/drkjam/netaddr
[py.test]: https://docs.pytest.org/
