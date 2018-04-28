#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   user.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import os


class User(object):

    def __init__(self):
        self.uid = os.getuid()

    @property
    def is_root(self):
        return self.uid == 0
