# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:55:38 2018

@author: calydon
"""

''' Hazards of Plastics program'''

import datetime as dt
import math as mt
current_time=dt.datetime
kms_to_travel=10000
daily_travel=50 # assuming he can cover 50 kms per day after all daily activities
days_required=kms_to_travel/daily_travel
print("required days " + str(days_required))
months=days_required // 30
days_remaining=days_required % 30