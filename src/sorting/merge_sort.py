from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next_node: ListNode | None = None):
        self.val = val
        self.next = next_node


def find_middle(head: ListNode) -> ListNode:
    slow = head
    fast = head.next
    while slow and slow.next and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_two_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    head = ListNode()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return head.next


def merge_sort(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head

    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(after_middle)

    return merge_two_lists(left, right)


# Auxiliars
def build_linked_list(values: list[int])-> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head: ListNode | None) -> None:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)


if __name__ == "__main__":
    _values = [4, 2, 1, 3]
    print("Unsorted Linked List:", _values)
    _head = build_linked_list(_values)
    sorted_head = merge_sort(_head)
    print("Sorted Linked List:", end=" ")
    print_linked_list(sorted_head)
