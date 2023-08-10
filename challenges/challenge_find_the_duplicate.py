def find_duplicate(nums):
    if not isinstance(nums, list):
        return False

    nums_set = set()
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in nums_set:
            return num
        nums_set.add(num)

    return False
