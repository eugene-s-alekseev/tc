import unittest

from FlightDataRecorder import FlightDataRecorder

class FlightDataRecorderTest(unittest.TestCase):
    def setUp(self):
       self.fdr = FlightDataRecorder()

    def test_get_distance(self):
        self.assertAlmostEqual(5., self.fdr.getDistance([90, 0], [3, 4]), "first test failed")
        self.assertAlmostEqual(1111., self.fdr.getDistance([37, 37, 37, 37], [1, 10, 100, 1000]), "second test failed")

if __name__ == "__main__":
    unittest.main()
