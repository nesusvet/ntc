#!/bin/env python

import counts
import ntc

for color in counts.colorz("turtle2.jpg", 1):
    print color
    print ntc.ntc(color)




