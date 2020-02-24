# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound


import json
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys(), rename=True)(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
