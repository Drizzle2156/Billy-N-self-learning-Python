
# modules are code libraries
# import math has an alternate form
from math import pi
import sys
import random as rdm  # lets you rename modules with aliases of your choice
from enum import Enum
import kansas  # custom module kansas.py

print(pi)

# print(dir(rdm)) rewritten below as a list. It outputs every item in the module
for item in dir(rdm):
    print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)
