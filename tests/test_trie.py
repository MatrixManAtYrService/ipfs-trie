import unittest

import ipdb
import IPython
def undebug():
    def f() : pass
    ipdb.set_trace = f
    IPython.embed = f

class TrieStore(unittest.TestCase):

    def setUp(self):
        pass

    def test_dummy1(self):
        self.assertEqual(1,1, "Equality is reflexive")

class TrieRequest(unittest.TestCase):

    def setUp(self):
        pass

    def test_dummy(self):
        self.assertEqual(1,1, "Equality is reflexive")
