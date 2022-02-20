import sys

nums_file = sys.argv[1]
nums_list = []

with open(nums_file, 'r') as file:
    for line in file:
        nums_list.append(int(line.rstrip()))

m = sorted(nums_list)[len(nums_list) // 2]
print(sum(abs(v - m) for v in nums_list))
