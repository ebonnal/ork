import unittest

import sys

sys.path.append("..")

from ork import NameGenerator


class Test(unittest.TestCase):
    ng = NameGenerator()

    def test(self):
        ng.generate(faction="ork", lang="en")
        ng.generate(faction="ork", lang="en")

