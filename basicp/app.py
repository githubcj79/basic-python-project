# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file: basicp/app.py

from __future__ import print_function, with_statement

from basicp.common.my_logging import logger

logger.name = __name__

def run():
    print('Hello world !!!')
    logger.warning('This is a warning')

def mysum(numbers):
    output = 0
    for one_number in numbers:
        output += one_number
    return output