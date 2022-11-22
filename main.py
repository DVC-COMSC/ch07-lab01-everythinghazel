# ******************************
nums = [ ]

for i in range(5):
    inputval = list(map(int, input("Enter input: ").split()))
    # nums.append(input)
print(inputval)

inputval.pop(max(inputval))
inputval.pop(min(inputval))

# sumval = 0
# inputval.remove(max(input))
# inputval.remove(min(input))

# sumval += nums[i]
print(inputval)

# ******************************
