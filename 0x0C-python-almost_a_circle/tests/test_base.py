#!/usr/bin/python3
'''unittest for Base()
'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

        obj3 = Base(89)
        self.assertEqual(obj3.id, 89)
