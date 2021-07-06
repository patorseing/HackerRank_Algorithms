import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        num1 = 2
        num2 = 3
        actual = Solution.solveMeFirst(num1, num2)
        excepted = 5
        self.assertEqual(actual, excepted)
