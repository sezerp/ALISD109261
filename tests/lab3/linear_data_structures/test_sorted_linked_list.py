import unittest

from lab3.linear_data_structures.sorted_linked_list import SortedLinkedList


class TestSortedLinkedList(unittest.TestCase):
    def test_insert_single_element(self):
        # given
        xs = SortedLinkedList[int]()
        # when
        xs.insert(1)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(1, xs.size)
        self.assertEqual(1, xs.head.value)
        self.assertEqual(1, xs.tail.value)

    def test_insert_multiple_elements(self):
        # given
        xs = SortedLinkedList[int]()
        # when
        xs.insert(3)
        xs.insert(2)
        xs.insert(1)
        xs.insert(5)
        xs.insert(4)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(5, xs.size)
        self.assertEqual(1, xs.head.value)
        self.assertEqual(2, xs.head.next.value)
        self.assertEqual(3, xs.head.next.next.value)
        self.assertEqual(4, xs.head.next.next.next.value)
        self.assertEqual(5, xs.head.next.next.next.next.value)
        self.assertEqual(5, xs.tail.value)
        self.assertEqual(None, xs.tail.next)

    def test_delete_single_element(self):
        # given
        xs = SortedLinkedList[int]()
        xs.insert(1)
        # when
        e = xs.delete(1)
        # then
        self.assertEqual(True, xs.is_empty())
        self.assertEqual(0, xs.size)
        self.assertEqual(1, e)
        self.assertEqual(None, xs.head)
        self.assertEqual(None, xs.tail)

    def test_delete_multiple_elements(self):
        # given
        xs = SortedLinkedList[int]()
        xs.insert(1)
        xs.insert(2)
        xs.insert(3)
        xs.insert(4)
        xs.insert(5)
        # when
        e_1 = xs.delete(5)
        e_2 = xs.delete(2)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(3, xs.size)
        self.assertEqual(5, e_1)
        self.assertEqual(2, e_2)
        self.assertEqual(1, xs.head.value)
        self.assertEqual(3, xs.head.next.value)
        self.assertEqual(4, xs.tail.value)
        self.assertEqual(None, xs.tail.next)


if __name__ == '__main__':
    unittest.main()
