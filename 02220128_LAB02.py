# Node class
class Node:
    def __init__(self, data):
        self.data = data   # stores the element
        self.next = None   # reference to the next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None   # first node
        self.tail = None   # last node (optional but useful)
        self.size = 0      # number of elements

    def display_info(self):
        print("Created new LinkedList")
        print("Current size:", self.size)
        print("Head:", self.head)


# Example usage
ll = LinkedList()
ll.display_info()

#task2
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # 1. append(element)
    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"Appended {element} to the list")

    # 2. get(index)
    def get(self, index):
        if index < 0 or index >= self._size:
            return "Index out of range"

        current = self.head
        for _ in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")
        return current.data

    # 3. set(index, element)
    def set(self, index, element):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return

        current = self.head
        for _ in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    # 4. size()
    def size(self):
        print(f"Current size: {self._size}")
        return self._size

    # 5. prepend(element)
    def prepend(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1
        print(f"Prepend {element} to the list")

    # Helper to print list
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Print Linked list :[" + " ".join(elements) + "]")


# Example usage
ll = LinkedList()

ll.append(5)
ll.get(0)
ll.set(0, 10)
ll.get(0)
ll.size()
ll.prepend(10)
ll.print_list()
