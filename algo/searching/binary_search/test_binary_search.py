import unittest
import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_aSimpleList(self):
        testList = [1, 2, 3, 4, 5, 6, 7, 8]
        testItem = 7
        found = binary_search.binary_search(testList, testItem)
        self.assertEqual(found, 6)


if __name__ == '__main__':
    unittest.main()