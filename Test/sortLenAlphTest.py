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
                      '(descendingTest.txt) and (Sort Me.txt) must be in the same folder as sortLenAlphTest.py')

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
                      '(descendingTest.txt) and (Sort Me.txt) must be in the same folder as sortLenAlphTest.py')




# # Must first make sure the testing files exist and/or are in the right location
# if os.path.isfile('sort me sorted A.txt') and os.path.isfile('sort me sorted D.txt'):
#     # Get the sorted text files as an array to compare with
#     sortedAscending = sortLenAlph.getWords('sort me sorted A.txt')
#     sortedDescending = sortLenAlph.getWords('sort me sorted D.txt')
#
#     # Test for sorting in ascending order
#     ascendingTest = sortLenAlph.sortText('Sort Me.txt', True)
#
#     # Check if the text was sorted correctly
#     if ascendingTest == sortedAscending:
#         print('Sorting in ascending order: PASS')
#     else:
#         print('Sorting in ascending order: FAIL')
#
#     # Test for for sorting in descending order
#     descendingTest = sortLenAlph.sortText('Sort Me.txt', False)
#
#     if descendingTest == sortedDescending:
#         print('Sorting in descending order: PASS')
#     else:
#         print('Sorting in descending order: FAIL')
# else:
#     print('Error: testing files not found. To run tests, the files (sort me sorted A.txt) and (sort me sorted D.txt)'
#           'must be in the same folder as sortLenAlphTest.py')