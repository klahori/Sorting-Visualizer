import unittest
from random import randrange

from bubblesort import bubble_sort
from selectionsort import selection_sort


class Validity(unittest.TestCase):

    def generate_testcases(self):
        cases = []
        arrays = 10
        size = 30
        lower = -15
        upper = 15
        for i in range(arrays):
            current_array = []
            for j in range(size):
                current_array.append(randrange(lower, upper + 1))
            cases.append(current_array)

        return cases
    def bubblesort_test(self):
        cases = self.generate_testcases()
        for case in cases:
            self.assertListEqual(sorted(case), bubble_sort(case))

    def selectionsort_test(self):
        cases = self.generate_testcases()
        for case in cases:
            self.assertListEqual(sorted(case), selection_sort(case))
        

tester = Validity()
tester.bubblesort_test()
tester.selectionsort_test()
