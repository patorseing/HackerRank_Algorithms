import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        a = list(map(int, "5 6 7".strip().split()))
        b = list(map(int, "3 6 10".strip().split()))
        actual = Solution.compareTriplets(a, b)
        excepted = [1, 1]
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        a = list(map(int, "17 28 30".strip().split()))
        b = list(map(int, "99 16 8".strip().split()))
        actual = Solution.compareTriplets(a, b)
        excepted = [2, 1]
        self.assertEqual(actual, excepted)
