import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        ar = list(
            map(int, "1000000001 1000000002 1000000003 1000000004 1000000005".split()))
        actual = Solution.aVeryBigSum(ar)
        excepted = 5000000015
        self.assertEqual(actual, excepted)
