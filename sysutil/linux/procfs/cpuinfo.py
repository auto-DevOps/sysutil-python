#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   cpuinfo.py
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
    return field.strip().replace(' ', '_'), value.strip()


def parse_cpuinfo(content):
    cpuinfo = OrderedDict(
        parse_pair(pair=pair)
        for pair in content.split('\n')
    )
    return cpuinfo


def parse_cpuinfos(content):
    content = content.strip()
    cpuinfos = [
        parse_cpuinfo(content=cpu)
        for cpu in content.split('\n\n')
    ]
    return cpuinfos


def get_cpuinfos():
    cpuinfo_path = '/proc/cpuinfo'
    if not os.path.exists(cpuinfo_path):
        return None

    content = open(cpuinfo_path).read()
    return parse_cpuinfos(content=content)

if __name__ == '__main__':
    for cpu in get_cpuinfos():
        print(cpu)
