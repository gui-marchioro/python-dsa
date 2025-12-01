import pytest
from sorting.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        ([4, 2, 5, 1], [1, 2, 4, 5]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([5, 4, 3 , 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 4, 2, 5], [1, 2, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
    ]
)
def test_bubble_sort(input_array, expected_output):
    assert bubble_sort(input_array) == expected_output
