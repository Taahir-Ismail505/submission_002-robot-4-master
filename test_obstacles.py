import unittest

from world.obstacles import path_is_blocked, is_position_blocked

class MyTestCase(unittest.TestCase):

    def test_path_is_blocked(self):
        self.assertNotEqual(path_is_blocked,False)

    def test_is_position_blocked(self):
        self.assertNotEqual(is_position_blocked,False)
