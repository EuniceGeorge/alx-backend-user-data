#!/usr/bin/env python3
""" filter datum """

import re


def filter_datum(fields, redaction, message, separator):
    """function filter"""

    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, f'\\1={redaction}', message)
