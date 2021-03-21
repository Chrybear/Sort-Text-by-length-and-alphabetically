# Author: Charles Ryan Barrett
# Date: 3/21/2021
# Description: File to test if sortLenAlph is sorting correctly

import sortLenAlph
import os.path
import unittest


class sortedTesting(unittest.TestCase):

    # Test if text was sorted in ascending order correctly
    def testAscending(self):
        # Need to first make sure the files with which we test with exist
        if os.path.isfile('ascendingTest.txt') and os.path.isfile("../Sort Me.txt"):
            # Get the sorted text file as an array to compare with
            sortedAscending = sortLenAlph.getWords('ascendingTest.txt')

            # Use to sort function
            ascendingTest = sortLenAlph.sortText("../Sort Me.txt", True)

            self.assertEqual(ascendingTest, sortedAscending, "Sorting in Ascending order: FAIL")
        else:
            self.fail('Error: testing files not found. To run tests, the files (ascendingTest.txt) and '
                      '(descendingTest.txt) must be in the same "Test" folder as sortLenAlphTest.py and (Sort Me.txt) '
                      'must be in the main folder')

    # Test if text was sorted in descending order correctly
    def testDescending(self):
        # Need to first make sure the files with which we test with exist
        if os.path.isfile('descendingTest.txt') and os.path.isfile("../Sort Me.txt"):
            # Get the sorted text file as an array to compare with
            sortedDescending = sortLenAlph.getWords('descendingTest.txt')

            # Use to sort function
            descendingTest = sortLenAlph.sortText("../Sort Me.txt", False)

            self.assertEqual(descendingTest, sortedDescending, "Sorting in Descending order: FAIL")
        else:
            self.fail('Error: testing files not found. To run tests, the files (ascendingTest.txt) and '
                      '(descendingTest.txt) must be in the same "Test" folder as sortLenAlphTest.py and (Sort Me.txt) '
                      'must be in the main folder')




