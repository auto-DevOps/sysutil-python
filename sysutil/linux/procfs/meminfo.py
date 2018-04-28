#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   meminfo.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import os

from collections import (
    OrderedDict,
)


def parse_pair(pair):
    field, value = pair.split(':')
    field, value = field.strip(), value.strip()

    value_pair = value.split(' ', 1)
    if len(value_pair) == 2:
        value, unit = value_pair
    else:
        value, = value_pair
        unit = None

    return field, (int(value), unit)


def parse_meminfo(content):
    content = content.strip()

    meminfo = OrderedDict([
        parse_pair(pair=line)
        for line in content.split('\n')
    ])
    return meminfo


def get_meminfo():
    meminfo_path = '/proc/meminfo'

    content = open(meminfo_path).read()
    return parse_meminfo(content=content)

if __name__ == '__main__':
    print(get_meminfo())
