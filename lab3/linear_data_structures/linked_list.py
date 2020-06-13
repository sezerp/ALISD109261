from lab3.linear_data_structures.collections import Node, List, T


class LinkedList(List[T]):
    """LinkedList - class simple implementation of linear data structure
    named single linked list
    author:
        Paweł Zabczyński
    """

    def __init__(self):
        super().__init__()
        self.head: Node[T] = None
        self.tail: Node[T] = None
        self.size = 0

    def push_front(self, e: T) -> None:
        node = Node[T](e)
        self.size += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def push_back(self, e: T) -> None:
        node = Node[T](e)
        self.size += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop_front(self) -> T:
        node = None
        if self.is_empty():
            raise IndexError
        elif self.size == 1:
            self.size -= 1
            node = self.head
            self.head = None
            self.tail = None
        else:
            self.size -= 1
            node = self.head
            self.head = self.head.next
        return node.value

    def pop_back(self) -> T:
        node_result = None
        if self.is_empty():
            raise IndexError
        elif self.size == 1:
            self.size -= 1
            node_result = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            node_result = node.next
            self.tail = node
            self.tail.next = None
            self.size -= 1
        return node_result.value

    def pop_element(self, e: T) -> T:
        # on notes method is called pop_1()
        if self.is_empty():
            raise IndexError

        result = None
        node = self.head
        if self.head.value == e:
            result = self.head
            self.head = self.head.next
            self.size -= 1
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
