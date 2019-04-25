# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file: basicp/app.py

from __future__ import print_function, with_statement
from basicp.common.snk_logging import get_logger
logger = get_logger(__name__)

from basicp import app

if __name__ == '__main__':
	logger.debug('Antes de invocar app.run()')
	app.run()
	logger.debug('Después de invocar app.run()')