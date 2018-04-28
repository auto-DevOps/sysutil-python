#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   machine.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from collections import (
    OrderedDict,
)

from dmi.parser.type import (
    DMIType,
)

from .base import (
    BaseHardwareModel,
)


class Machine(BaseHardwareModel):

    NAME = 'machine'

    FIELD_VENDOR = 'vendor'
    FIELD_MANUFACTURER = 'manufacturer'
    FIELD_PRODUCT = 'product'
    FIELD_SERIAL_NUMBER = 'serial_number'
    FIELD_ARCHITECTURE = 'architecture'

    property_fields = (
        FIELD_VENDOR,
        FIELD_MANUFACTURER,
        FIELD_PRODUCT,
        FIELD_SERIAL_NUMBER,
        FIELD_ARCHITECTURE,
    )

    @property
    def vendor(self):
        return self.lookup_dmi(
            _type=DMIType.TYPE_BIOS,
            field='vendor',
        )

    @property
    def manufacturer(self):
        return self.lookup_dmi(
            _type=DMIType.TYPE_SYSTEM,
            field='manufacturer',
        )

    @property
    def product(self):
        return self.lookup_dmi(
            _type=DMIType.TYPE_SYSTEM,
            field='product_name',
        )

    @property
    def serial_number(self):
        return self.lookup_dmi(
            _type=DMIType.TYPE_SYSTEM,
            field='serial_number',
        )

    @property
    def architecture(self):
        self

    def _fetch_info(self):
        return OrderedDict([
            (field, getattr(self, field))
            for field in self.property_fields
        ])
