from django.test import TestCase
from datetime import datetime
from extGenOptimizer import extGenOptimizer

class ExtGenOptimizerTestCase(TestCase):
    def setUp(self):
        self.t = extGenOptimizer()
        self.t.timeSlots = [
            [datetime(2015, 11, 11, 9), datetime(2015, 11, 11, 12)],
            [datetime(2015, 11, 12, 9), datetime(2015, 11, 12, 12)],
        ]
        self.t.studentRecord = [
            ["A", "Chinese", "English"],
            ["B", "Chinese", "English"],
            ["C", "Chinese", "English", "Math"],
        ]         

    def test_valid_resuilt(self):
        self.t.run()
        self.assertEqual(self.t.subjectLookUpLen, 3)
        self.assertEqual(self.t.totalNumHours, 6)
        self.assertEqual(self.t.maxRevisionTime, 3)
        self.assertEqual(len(self.t.best_ind), 3)

