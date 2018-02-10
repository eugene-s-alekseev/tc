import unittest

class TwoDiagonals:
    def __init__(self):
        pass

    def maxPoints(self, x, y):
        def count_cities(i, j):
            cities_on_roads = 0
            for k in range(len(x)):
                if x[k] - x[i] == y[k] - y[i] or x[k] - x[j] == y[j] - y[k]:
                    cities_on_roads += 1
            return cities_on_roads

        max_cities = max([
            count_cities(i, j)
            for i in range(len(x))
            for j in range(len(x))
        ])

        return max_cities


class TwoDiagonalsTest(unittest.TestCase):
    def setUp(self):
        self.td = TwoDiagonals()

    def test_max_points(self):
        self.assertEqual(
            4,
            self.td.maxPoints([1, 4, 4, 5], [3, 0, 2, 3]),
            "failed test one"
        )
        self.assertEqual(
            2,
            self.td.maxPoints([0, 1, 2, 3, 4, 5], [2, 2, 2, 2, 2, 2]),
            "failed test two"
        )
        self.assertEqual(
            4,
            self.td.maxPoints([2, 2, 3, 3], [2, 3, 2, 3]),
            "failed test three"
        )
        self.assertEqual(
            4,
            self.td.maxPoints([10, 0, 15, 9], [10, 0, 15, 11]),
            "failed test four"
        )
        self.assertEqual(
            2,
            self.td.maxPoints([273, 100, 999, 789, 105], [838, 200, 999, 0, 560]),
            "failed test five"
        )
        self.assertEqual(
            5,
            self.td.maxPoints([0, 2, 0, 2, 1], [0, 0, 2, 2, 1]),
            "failed test six"
        )
        self.assertEqual(
            3,
            self.td.maxPoints([500, 503, 501], [200, 197, 199]),
            "failed test seven"
        )
        self.assertEqual(
            2,
            self.td.maxPoints([0, 2, 4], [0, 3, 6]),
            "failed test eight"
        )

if __name__ == "__main__":
    unittest.main()
