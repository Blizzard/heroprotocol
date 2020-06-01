#!/usr/bin/env python
#
# Copyright 2015-2020 Blizzard Entertainment. Subject to the MIT license.
# See the included LICENSE file for more information.
#

import json
import six


def json_dumps(obj, encoding):
    if six.PY3:
        return json.dumps(obj, ensure_ascii=True)
    else:
        return json.dumps(obj, encoding=encoding)
