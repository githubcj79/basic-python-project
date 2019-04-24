# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file: basicp/common/my_logging.py

from __future__ import print_function, with_statement

import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
# c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('basicp.log')
# c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
#logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')