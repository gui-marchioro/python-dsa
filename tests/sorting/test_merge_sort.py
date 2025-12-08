from sorting.merge_sort import (
    ListNode,
    find_middle,
    merge_sort,
    merge_two_lists,
    build_linked_list,
)


def linked_list_to_list(head: ListNode | None) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def test_find_middle():
    # Test with an odd number of elements
    head = build_linked_list([1, 2, 3, 4, 5])
    middle = find_middle(head)
    assert middle.val == 3

    # Test with an even number of elements
    head = build_linked_list([1, 2, 3, 4])
    middle = find_middle(head)
    assert middle.val == 2

    # Test with two elements
    head = build_linked_list([1, 2])
    middle = find_middle(head)
    assert middle.val == 1

    # Test with one element
    head = build_linked_list([1])
    middle = find_middle(head)
    assert middle.val == 1


def test_merge_two_lists():
    # Test merging two non-empty lists
    l1 = build_linked_list([1, 3, 5])
    l2 = build_linked_list([2, 4, 6])
    merged = merge_two_lists(l1, l2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]

    # Test merging with one empty list
    l1 = build_linked_list([1, 3, 5])
    l2 = None
    merged = merge_two_lists(l1, l2)
    assert linked_list_to_list(merged) == [1, 3, 5]

    # Test merging with the other empty list
    l1 = None
    l2 = build_linked_list([2, 4, 6])
    merged = merge_two_lists(l1, l2)
    assert linked_list_to_list(merged) == [2, 4, 6]

    # Test merging two empty lists
    merged = merge_two_lists(None, None)
    assert linked_list_to_list(merged) == []


def test_merge_sort():
    # Test with an unsorted list
    head = build_linked_list([4, 2, 1, 3])
    sorted_head = merge_sort(head)
    assert linked_list_to_list(sorted_head) == [1, 2, 3, 4]

    # Test with another unsorted list
    head = build_linked_list([5, 2, 8, 1, 9, 4])
    sorted_head = merge_sort(head)
    assert linked_list_to_list(sorted_head) == [1, 2, 4, 5, 8, 9]

    # Test with a list that is already sorted
    head = build_linked_list([1, 2, 3, 4, 5])
    sorted_head = merge_sort(head)
    assert linked_list_to_list(sorted_head) == [1, 2, 3, 4, 5]

    # Test with a list that is sorted in reverse order
    head = build_linked_list([5, 4, 3, 2, 1])
    sorted_head = merge_sort(head)
    assert linked_list_to_list(sorted_head) == [1, 2, 3, 4, 5]

    # Test with a list containing duplicate elements
    head = build_linked_list([4, 2, 1, 3, 2, 1, 4])
    sorted_head = merge_sort(head)
    assert linked_list_to_list(sorted_head) == [1, 1, 2, 2, 3, 4, 4]

    # Test with an empty list
    head = build_linked_list([])
    sorted_head = merge_sort(head)
    assert linked_list_to_list(sorted_head) == []

    # Test with a list containing a single element
    head = build_linked_list([1])
    sorted_head = merge_sort(head)
    assert linked_list_to_list(sorted_head) == [1]
