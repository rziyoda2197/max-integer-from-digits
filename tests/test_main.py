import pytest

def maximal_number(nums):
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x*3, reverse=True)
    return int(''.join(nums)) if nums[0] != '0' else 0

@pytest.mark.parametrize("nums, expected", [
    ([3, 30, 34, 5, 9], 9534330),
    ([1, 2, 3], 321),
    ([10, 7, 76, 415], 77641510),
    ([0, 0, 0], 0),
    ([5, 5, 5], 555),
    ([9, 9, 9], 999),
    ([1, 1, 1], 111),
])
def test_maximal_number(nums, expected):
    assert maximal_number(nums) == expected
