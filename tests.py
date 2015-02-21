# The MIT License (MIT)

# Copyright (c) 2015 Cameron Lai

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

