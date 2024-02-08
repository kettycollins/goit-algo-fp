class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def reverse_linkedlist(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def insertion_sort_linkedlist(self):
        dummy = Node(float("-inf"))
        dummy.next = self.head
        prev_sorted = dummy
        current = self.head

        while current:
            if current.value < prev_sorted.value:
                prev_sorted.next = current.next
                insert_pos = dummy
                while insert_pos.next.value < current.value:
                    insert_pos = insert_pos.next
                current.next = insert_pos.next
                insert_pos.next = current
                current = prev_sorted.next
            else:
                prev_sorted = prev_sorted.next
                current = current.next

        self.head = dummy.next

    def merge_sorted_linkedlists(self, other):
        dummy = Node()
        current = dummy
        current1 = self.head
        current2 = other.head

        while current1 and current2:
            if current1.value < current2.value:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        if current1:
            current.next = current1
        elif current2:
            current.next = current2

        self.head = dummy.next

    def print_linkedlist(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    # Створення першого списку
    llist1 = LinkedList()
    llist1.add_node(15)
    llist1.add_node(5)
    llist1.add_node(10)
    llist1.add_node(20)

    print("Зв'язний список:")
    llist1.print_linkedlist()

    # Реверсування списку
    llist1.reverse_linkedlist()
    print("\nРеверсований список:")
    llist1.print_linkedlist()

    # Сортування вставками
    llist1.insertion_sort_linkedlist()
    print("\nВідсортований список:")
    llist1.print_linkedlist()

    # Створення другого списку
    llist2 = LinkedList()
    llist2.add_node(1)
    llist2.add_node(3)
    llist2.add_node(5)

    print("\nЗв'язний список 2:")
    llist2.print_linkedlist()

    # Об'єднання відсортованих списків
    llist1.merge_sorted_linkedlists(llist2)
    print("\nОб'єднаний список:")
    llist1.print_linkedlist()
