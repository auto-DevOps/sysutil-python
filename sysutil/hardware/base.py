#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   base.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import json

from collections import (
    defaultdict,
)

from dmi import (
    fetch_dmi,
)

from ..system import (
    System,
)
from ..util.decorator import (
    eval_now,
)


class BaseHardwareModel(object):

    system = System()

    DMI_TABLE = fetch_dmi()

    @eval_now
    def DMI_MAPPING(table=DMI_TABLE):
        mapping = defaultdict(list)
        for item in table:
            mapping[item['type']].append(item)
        return mapping

    @classmethod
    def lookup_dmi(cls, _type, field):
        for item in cls.DMI_MAPPING[_type]:
            value = item.get(field)
            if value:
                return value

    def __init__(self):
        self.fetch_info()

    def saveto(self, dct):
        dct[self.NAME] = self.info

    def _fetch_info(self):
        if self.system.is_linux:
            return self._fetch_info_linux()

    def fetch_info(self):
        self.info = info = self._fetch_info()
        return info

    def print_info_json(self):
        print(json.dumps(
            self.info,
            ensure_ascii=False,
            indent=4,
        ))
