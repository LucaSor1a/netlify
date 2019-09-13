from sorting import Sort
import unittest


class SortingAlgorithmsTestCase(unittest.TestCase):

    def setUp(self):
        self.desor1 = [66, 71, 16, 21, 79, 9, 40, 60, 5]
        self.or1 = [5, 9, 16, 21, 40, 60, 66, 71, 79]
        self.desor2 = [66, 71, 16, -21, 79, 9, 40, 60, -5]
        self.or2 = [-21, -5, 9, 16, 40, 60, 66, 71, 79]
        self.desor3 = [5, 9, 16, 21, 40, 60, 66, 71, 79]
        self.or3 = [5, 9, 16, 21, 40, 60, 66, 71, 79]
        self.Sort = Sort()

    def testBuble(self):
        self.assertEqual(self.Sort.BubleSort(self.desor1), self.or1)

    def testInsertion(self):
        self.assertEqual(self.Sort.InsertionSort(self.desor1), self.or1)

    def testMerge(self):
        self.assertEqual(self.Sort.MergeSort(self.desor1), self.or1)

    def testBubleNegativo(self):
        self.assertEqual(self.Sort.BubleSort(self.desor1), self.or1)

    def testInsertionNegativo(self):
        self.assertEqual(self.Sort.InsertionSort(self.desor1), self.or1)

    def testMergeNegativo(self):
        self.assertEqual(self.Sort.MergeSort(self.desor1), self.or1)

    def testBubleOrdenado(self):
        self.assertEqual(self.Sort.BubleSort(self.desor1), self.or1)

    def testInsertionOrdenado(self):
        self.assertEqual(self.Sort.InsertionSort(self.desor1), self.or1)

    def testMergeOrdenado(self):
        self.assertEqual(self.Sort.MergeSort(self.desor1), self.or1)


if __name__ == "__main__":
    unittest.main()
