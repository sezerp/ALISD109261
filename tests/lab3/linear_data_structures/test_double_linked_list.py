import unittest

from lab3.linear_data_structures.double_linked_list import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    def test_push_front_single_element(self):
        # given
        xs = DoubleLinkedList[int]()
        # when
        xs.push_front(1)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(1, xs.size)
        self.assertEqual(xs.head.value, 1)
        self.assertEqual(None, xs.head.next)
        self.assertEqual(None, xs.head.previous)
        self.assertEqual(1, xs.tail.value)

    def test_push_front_multiple_elements(self):
        # given
        xs = DoubleLinkedList[int]()
        # when
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(5, xs.size)
        self.assertEqual(xs.head.value, 5)
        self.assertEqual(4, xs.head.next.value)
        self.assertEqual(None, xs.head.previous)
        self.assertEqual(1, xs.tail.value)
        self.assertEqual(2, xs.tail.previous.value)

    def test_push_back_single_element(self):
        # given
        xs = DoubleLinkedList[int]()
        # when
        xs.push_front(1)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(1, xs.size)
        self.assertEqual(xs.head.value, 1)
        self.assertEqual(None, xs.head.next)
        self.assertEqual(None, xs.head.previous)
        self.assertEqual(1, xs.tail.value)

    def test_push_back_multiple_elements(self):
        # given
        xs = DoubleLinkedList[int]()
        # when
        xs.push_back(1)
        xs.push_back(2)
        xs.push_back(3)
        xs.push_back(4)
        xs.push_back(5)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(5, xs.size)
        self.assertEqual(xs.head.value, 1)
        self.assertEqual(2, xs.head.next.value)
        self.assertEqual(None, xs.head.previous)
        self.assertEqual(None, xs.tail.next)
        self.assertEqual(5, xs.tail.value)
        self.assertEqual(4, xs.tail.previous.value)

    def test_pop_front_single_element(self):
        # given
        xs = DoubleLinkedList[int]()
        xs.push_front(1)
        # when
        e = xs.pop_front()
        # then
        self.assertEqual(True, xs.is_empty())
        self.assertEqual(0, xs.size)
        self.assertEqual(1, e)
        self.assertEqual(None, xs.tail)
        self.assertEqual(None, xs.head)

    def test_pop_front_multiple_elements(self):
        # given
        xs = DoubleLinkedList[int]()
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # when
        e_1 = xs.pop_front()
        e_2 = xs.pop_front()
        e_3 = xs.pop_front()
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(2, xs.size)
        self.assertEqual(5, e_1)
        self.assertEqual(4, e_2)
        self.assertEqual(3, e_3)
        self.assertEqual(2, xs.head.value)
        self.assertEqual(1, xs.head.next.value)
        self.assertEqual(None, xs.head.previous)
        self.assertEqual(None, xs.tail.next)
        self.assertEqual(1, xs.tail.value)
        self.assertEqual(2, xs.tail.previous.value)

    def test_pop_back_single_element(self):
        # given
        xs = DoubleLinkedList[int]()
        xs.push_front(1)
        # when
        e = xs.pop_front()
        # then
        self.assertEqual(True, xs.is_empty())
        self.assertEqual(0, xs.size)
        self.assertEqual(1, e)
        self.assertEqual(None, xs.tail)
        self.assertEqual(None, xs.head)

    def test_pop_back_multiple_elements(self):
        # given
        xs = DoubleLinkedList[int]()
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # when
        e_1 = xs.pop_back()
        e_2 = xs.pop_back()
        e_3 = xs.pop_back()
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(2, xs.size)
        self.assertEqual(1, e_1)
        self.assertEqual(2, e_2)
        self.assertEqual(3, e_3)
        self.assertEqual(5, xs.head.value)
        self.assertEqual(4, xs.head.next.value)
        self.assertEqual(None, xs.head.previous)
        self.assertEqual(None, xs.tail.next)
        self.assertEqual(4, xs.tail.value)
        self.assertEqual(5, xs.tail.previous.value)

    def test_pop_element_single_element(self):
        # given
        xs = DoubleLinkedList[int]()
        xs.push_front(1)
        # when
        e = xs.pop_element(1)
        # then
        self.assertEqual(True, xs.is_empty())
        self.assertEqual(0, xs.size)
        self.assertEqual(1, e)
        self.assertEqual(None, xs.tail)
        self.assertEqual(None, xs.head)

    def test_pop_element_multiple_elements(self):
        # given
        xs = DoubleLinkedList[int]()
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # when
        e_1 = xs.pop_element(2)
        e_2 = xs.pop_element(3)
        e_3 = xs.pop_element(4)
        # then
        self.assertEqual(False, xs.is_empty())
        self.assertEqual(2, xs.size)
        self.assertEqual(2, e_1)
        self.assertEqual(3, e_2)
        self.assertEqual(4, e_3)
        self.assertEqual(1, xs.tail.value)
        self.assertEqual(5, xs.head.value)
        self.assertEqual(None, xs.head.previous)
        self.assertEqual(None, xs.tail.next)
        self.assertEqual(5, xs.tail.previous.value)
        self.assertEqual(1, xs.head.next.value)


if __name__ == '__main__':
    unittest.main()
