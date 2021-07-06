import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        ar = list(map(int, "1 2 3 4 10 11".strip().split()))
        actual = Solution.simpleArraySum(ar)
        excepted = 31
        self.assertEqual(actual, excepted)
