""" Kevin Burgon -- 12/07/2016
    This module is a filter object for parsing text and finding individual charges
    in the set of text.
"""

import re

def findCharges(imageText):
    """Find the individual charges in a segment of text."""

    charges = re.findall(r'((?:\S+\s){1,4})(\d+\.\d{2})\b', imageText)
    print(charges)
    return charges
