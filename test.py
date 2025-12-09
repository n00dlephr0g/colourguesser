#!/bin/python3

from palette import Palette
from colours import *
p = Palette()

p.add_hex("red", "#ff0000")
p.add_hex("green", "#00ff00")
p.add_hex("blue", "#0000ff")

p.show()
p.set_amount("red", 1)
p.show()
p.set_amount("green", 1)
p.show()
p.set_amount("blue", 1)

p.show()


