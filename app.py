def main():
    print(two_sum([3, 3], 6))


def two_sum(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        nums_dict[nums[i]] = i

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_dict:
            if nums_dict[diff] != i:
                return [i, nums_dict[diff]]
    return []


if __name__ == '__main__':
    main()
