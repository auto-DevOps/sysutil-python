#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   decorator.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''


def eval_now(func):
    '''
        Call function and pass back return value immediately.

        Arguments:
            func - Function to call
    '''

    return func()
