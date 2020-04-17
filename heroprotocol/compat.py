#!/usr/bin/env python
#
# Copyright 2015-2020 Blizzard Entertainment. Subject to the MIT license.
# See the included LICENSE file for more information.
#

import sys
import io


PY3 = sys.version_info.major == 3


def byte_to_int(x):
    if PY3 and isinstance(x, (bytes, int)):
        return x
    else:
        return ord(x)


def get_stream():
    if PY3:
        cls = io.StringIO
    else:
        cls = io.BytesIO
    return cls()
