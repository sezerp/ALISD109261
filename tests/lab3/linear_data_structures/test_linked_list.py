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

    def test_pop_front(self):
        # given
        xs = LinkedList[int]()
        xs.push_front(1)
        # when
        e = xs.pop_front()
        # then
        self.assertEqual(True, xs.is_empty())
        self.assertEqual(1, e)
        self.assertEqual(None, xs.head)
        self.assertEqual(None, xs.tail)

    def test_pop_front_multiple_values(self):
        # given
        xs = LinkedList[int]()
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
        self.assertEqual(2, xs.size)
        self.assertEqual(5, e_1)
        self.assertEqual(4, e_2)
        self.assertEqual(3, e_3)
        self.assertEqual(2, xs.head.value)
        self.assertEqual(1, xs.tail.value)

    def test_pop_back(self):
        # given
        xs = LinkedList[int]()
        xs.push_front(1)
        # when
        e = xs.pop_back()
        # then
        self.assertEqual(True, xs.is_empty())
        self.assertEqual(1, e)
        self.assertEqual(None, xs.head)
        self.assertEqual(None, xs.tail)

    def test_pop_back_multiple_values(self):
        # given
        xs = LinkedList[int]()
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
        self.assertEqual(2, xs.size)
        self.assertEqual(1, e_1)
        self.assertEqual(2, e_2)
        self.assertEqual(3, e_3)
        self.assertEqual(5, xs.head.value)
        self.assertEqual(4, xs.tail.value)

    def test_pop_element_when_is_on_top(self):
        # given
        xs = LinkedList[int]()
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # when
        e = xs.pop_element(5)
        # then
        self.assertEqual(4, xs.size)
        self.assertEqual(5, e)
        self.assertEqual(4, xs.head.value)

    def test_pop_element_when_exist(self):
        # given
        xs = LinkedList[int]()
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # when
        e = xs.pop_element(3)
        # then
        self.assertEqual(4, xs.size)
        self.assertEqual(3, e)

    def test_pop_element_when_is_tail(self):
        # given
        xs = LinkedList[int]()
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # when
        e = xs.pop_element(1)
        # then
        self.assertEqual(4, xs.size)
        self.assertEqual(1, e)
        self.assertEqual(2, xs.tail.value)

    def test_pop_element_when_is_before_tail(self):
        # given
        xs = LinkedList[int]()
        xs.push_front(1)
        xs.push_front(2)
        xs.push_front(3)
        xs.push_front(4)
        xs.push_front(5)
        # when
        e = xs.pop_element(2)
        # then
        self.assertEqual(4, xs.size)
        self.assertEqual(2, e)
        self.assertEqual(1, xs.tail.value)
        self.assertEqual(5, xs.head.value)


if __name__ == '__main__':
    unittest.main()
