nums = list(map(int, input().split()))
for i in range(len(nums)):
    for k in range(len(nums)):
        if nums.count(nums[k]) <= nums.count(nums[i]) and k == len(nums) - 1:
            print(nums[i])
            exit()
        elif nums.count(nums[k]) > nums.count(nums[i]): break
