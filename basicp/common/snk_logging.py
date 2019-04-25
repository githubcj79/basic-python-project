# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file: basicp/common/snk_logging.py

from __future__ import print_function, with_statement

# This code was taken from: https://www.toptal.com/python/in-depth-python-logging

import logging
import sys
from logging.handlers import TimedRotatingFileHandler

# FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
# FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
FORMATTER = logging.Formatter("[%(asctime)s][%(name)s][%(funcName)s:%(lineno)d][%(levelname)s][%(message)s]")
LOG_FILE = "basicp.log"

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler

def get_file_handler():
   # file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler = logging.FileHandler(LOG_FILE)
   file_handler.setFormatter(FORMATTER)
   return file_handler

def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger