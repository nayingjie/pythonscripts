# -*- coding: utf-8 -*-
from random import shuffle
pieces = ["♚", "♛", "♝", "♝", "♞", "♞", "♜", "♜"]
for i in xrange(10): shuffle(pieces)
for i in pieces: print i + "  ",