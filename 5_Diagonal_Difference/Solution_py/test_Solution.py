import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        source = ["11 2 4", "4 5 6", "10 8 -12"]
        arr = []
        for ar in source:
            arr.append(list(map(int, ar.split())))

        actual = Solution.diagonalDifference(arr)
        excepted = 15

    def testCaseII(self):
        source = ["1 2 3", "4 5 6", "9 8 9"]
        arr = []
        for ar in source:
            arr.append(list(map(int, ar.split())))

        actual = Solution.diagonalDifference(arr)
        excepted = 2

    def testCaseIII(self):
        source = ["-1 1 -7 -8", "-10 -8 -5 -2", "0 9 7 -1", "4 4 -2 1"]
        arr = []
        for ar in source:
            arr.append(list(map(int, ar.split())))

        actual = Solution.diagonalDifference(arr)
        excepted = 1
