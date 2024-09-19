nums = list(map(int, input().split()))
small = ''
big = ''
for i in range(len(nums)):
    for k in range(len(nums)):
        if nums.count(nums[k]) > nums.count(nums[i]):
            small += str(nums[i])
            break
for i in range(len(nums)):
    for k in range(len(small)):
        if(small[k] == str(nums[i])):
            break
        elif(k == len(small) - 1):
            print(nums[i])
            exit()
print(small)