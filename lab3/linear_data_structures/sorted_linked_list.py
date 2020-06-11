from lab3.linear_data_structures.collections import SortedList, T, ComparableNode


class SortedLinkedList(SortedList[T]):
    def __init__(self):
        self
        self.head: ComparableNode[T] = None
        self.tail: ComparableNode[T] = None
        self.size: int = 0

    def insert(self, e: T) -> None:
        new_node = ComparableNode[T](e)
        self.size += 1
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        elif self.head > new_node:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            while node.next and node.next < new_node:
                node = node.next

            if node.next:
                new_node.next = node.next
                node.next = new_node
            else:
                node.next = new_node
                self.tail = new_node

    def delete(self, e: T) -> None:
        if self.is_empty():
            raise IndexError

        result = None
        node = self.head
        if self.head.value == e:
            result = self.head
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
        else:
            while node.next and node.next.value != e:
                node = node.next

            if node.next.value == e:
                result = node.next
                self.size -= 1
                if node.next.next is not None:
                    node.next = node.next.next
                else:
                    self.tail = node
                    node.next = None
            else:
                result = None

        return result.value if result else None
