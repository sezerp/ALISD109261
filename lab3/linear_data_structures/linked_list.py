from lab3.linear_data_structures.collections import Node, List, T


class LinkedList(List[T]):
    """LinkedList - class simple implementatioon of linear data structure
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
        pass

    def pop_back(self) -> T:
        pass

    def get_at_index(self, e: T) -> T:
        pass

    def find(self, node: T) -> T:
        pass

    def get(self, index: int) -> T:
        if index >= self.size:
            raise IndexError()
