# ******************************
nums = []

# for i in range(5):
inputval = list(map(int, input("Enter input: ").split()))
# nums.append(input)
print(inputval)

maxidx = inputval.index(max(inputval))
inputval.pop(maxidx)
# inputval.pop(max(inputval))

minidx = inputval.index(min(inputval))
inputval.pop(minidx)
# inputval.pop(min(inputval))

# sumval = 0
# inputval.remove(max(input))
# inputval.remove(min(input))

# sumval += nums[i]
print(inputval)

# ******************************
