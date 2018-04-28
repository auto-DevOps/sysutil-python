#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   _os.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from collections import (
    OrderedDict,
)

from .base import (
    BaseHardwareModel,
)


class OS(BaseHardwareModel):

    NAME = 'os'

    FIELD_TYPE = 'type'
    FIELD_DISTRO = 'distro'
    FIELD_VERSION = 'version'
    FIELD_KERNEL_VERSION = 'kernel_version'

    def _fetch_info(self):
        return OrderedDict([
           (self.FIELD_TYPE, self.system.os_type),
           (self.FIELD_KERNEL_VERSION, self.system.kernel_version),
        ])
