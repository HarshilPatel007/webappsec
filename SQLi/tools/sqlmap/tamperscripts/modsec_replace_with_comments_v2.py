#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission

author : Harshil Patel (https://github.com/HarshilPatel007)
"""

import re
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHER


def dependencies():
    pass


def tamper(payload, **kwargs):
    """
    Mod Security Bypass.
    Technique : replace the word(s) with SQL comment.

    >>> tamper('SELECT')
    '/*!12345SELECT*/'
    """

    retVal = payload

    if payload:
        retVal = re.sub(r"(?<=\W)(?P<word>[A-Za-z_]+)", r'/*!12345\1*/', payload)

    return retVal
