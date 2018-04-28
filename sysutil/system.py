#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   system.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import os
import platform

from .util.decorator import (
    eval_now,
)


class System(object):

    OS_TYPE_LINUX = 'linux'

    @eval_now
    def os_type():
        os = platform.system().lower()
        return os

    def __init__(self):
        self._init(os_type=self.os_type)

    @property
    def is_linux(self):
        return self.os_type == self.OS_TYPE_LINUX

    def _init_uname(self):
        uname = os.uname()

        self.kernel_version = uname[2]

    def _init(self, os_type):
        init_handler_name = '_init_{os_type}'.format(os_type=os_type)
        getattr(self, init_handler_name, self._init_fake)()

    def _init_linux(self):
        self._init_uname()

    def _init_fake(self):
        self
