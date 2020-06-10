import unittest
from lab3.linear_data_structures.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_push_front_single_element(self):
        # given
        xs = LinkedList[int]()
        # when
        xs.push_front(1)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(1, xs.size)
        self.assertEqual(1, xs.head.value)
        self.assertEqual(None, xs.head.next)
        self.assertEqual(1, xs.tail.value)

    def test_push_front_multiple_elements(self):
        # given
        xs = LinkedList[int]()
        # when
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(xs.size, 3)
        self.assertEqual(xs.head.value, 3)
        self.assertEqual(xs.head.next.value, 2)
        self.assertEqual(xs.tail.value, 1)

    def test_push_back_single_element(self):
        # given
        xs = LinkedList[int]()
        # when
        xs.push_back(1)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(1, xs.size)
        self.assertEqual(1, xs.head.value)
        self.assertEqual(None, xs.head.next)
        self.assertEqual(1, xs.tail.value)

    def test_push_back_multiple_elements(self):
        # given
        xs = LinkedList[int]()
        # when
        xs.push_back(1)
        xs.push_back(2)
        xs.push_back(3)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(3, xs.size)
        self.assertEqual(1, xs.head.value)
        self.assertEqual(2, xs.head.next.value)
        self.assertEqual(3, xs.tail.value)


if __name__ == '__main__':
    unittest.main()
