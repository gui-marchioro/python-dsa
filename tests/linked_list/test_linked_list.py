from linked_list.linked_list import LinkedList, Node


def test_create_linked_list():
    ll = LinkedList()
    assert ll.head is None
    assert ll.tail is None


def test_append_node():
    ll = LinkedList()
    node1 = Node(1)
    ll.append(node1)
    assert ll.head == node1
    assert ll.tail == node1

    node2 = Node(2)
    ll.append(node2)
    assert ll.head == node1
    assert ll.tail == node2
    assert ll.head.next == node2


def test_remove_node():
    ll = LinkedList()
    node1 = Node(1)
    ll.append(node1)
    ll.remove()
    assert ll.head is None
    assert ll.tail is None

    node2 = Node(2)
    ll.append(node1)
    ll.append(node2)
    ll.remove()
    assert ll.head == node1
    assert ll.tail is node1


def test_node_creation():
    node = Node("some_value")
    assert node.value == "some_value"
    assert node.next is None
    assert node.previous is None


def test_append_sets_previous_pointer():
    ll = LinkedList()
    node1 = Node(1)
    ll.append(node1)
    node2 = Node(2)
    ll.append(node2)
    assert node2.previous == node1


def test_remove_from_list_with_multiple_nodes():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll.append(node1)
    ll.append(node2)
    ll.append(node3)

    ll.remove()  # Removes node3
    assert ll.tail == node2
    assert ll.tail.next is None
    assert ll.head == node1

    ll.remove()  # Removes node2
    assert ll.tail == node1
    assert ll.tail.next is None
    assert ll.head == node1


def test_remove_from_empty_list():
    ll = LinkedList()
    ll.remove()  # Should not raise an error
    assert ll.head is None
    assert ll.tail is None


def test_append_and_remove_sequence():
    ll = LinkedList()
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')

    # Append all
    ll.append(node1)
    ll.append(node2)
    ll.append(node3)
    assert ll.head == node1
    assert ll.tail == node3
    assert ll.tail.previous == node2
    assert node2.previous == node1
    assert node2.next == node3

    # Remove one
    ll.remove()
    assert ll.tail == node2
    assert ll.tail.next is None

    # Remove another
    ll.remove()
    assert ll.tail == node1
    assert ll.head == node1
    assert ll.tail.next is None

    # Remove last one
    ll.remove()
    assert ll.head is None
    assert ll.tail is None

    # Remove from empty
    ll.remove()
    assert ll.head is None
    assert ll.tail is None