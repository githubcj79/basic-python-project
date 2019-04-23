# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file: basicp/tests/test_mysum.py

from basicp.app import mysum

def test_sum_integers():
    assert mysum([0,1,2,3,4]) == 10
