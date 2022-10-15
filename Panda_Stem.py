
import numpy as np
import pandas as pd
from collections import Counter

# Q-1: Find f, p, mean, ss and show stem-leaf table
num_list = [105, 108, 124, 213, 437, 265, 173, 329, 381, 496, 149, 292, 238, 351, 307]

nums = np.array(num_list)

f = np.array(list(dict(Counter(nums)).values()))
p = f/15

mean = np.mean(nums)

diff = nums - mean
squares = diff**2
ss = np.sum(squares)

df = pd.DataFrame()
df["X"] = nums
df["f"] = f
df["p"] = p

descriptive = {"N" : len(nums),
               "m" : mean,
               "ss": ss}
df2 = pd.DataFrame(descriptive, index = [0])

print(df)
print("\n           Descriptives")
print(df2)

# Stem-Leaf Table
# 1. Convert to String
num_str_list = []
for x in nums:
    num_str_list.append(str(x))

# 2. Append to the dict (first is key, others are values as a list)
sl = {}
for n in num_str_list: # ['105', '124', '213', '315'...]
    if n[0] not in sl.keys():
        sl[n[0]] = []
        sl[n[0]].append(n[1]+n[2])
    else:
        sl[n[0]].append(n[1]+n[2])

# 3. Turn values back to int from String
sl_n = {}
for k, v in sl.items():
    k = int(k)
    sl_n[k] = []
    for n in v:
        n = int(n)
        sl_n[k].append(n)

# 1. Algebraic way
sl_dict = {}
for x in num_list:
    first = int(x/100)
    if first not in sl_dict.keys():
        sl_dict[first] = []
        sl_dict[first].append(x-first*100)
    else:
        sl_dict[first].append(x-first*100)

# 4. Sort dict items based on keys
sl_n = dict(sorted(sl_n.items()))

# 5. Sort values of each key
for k in sl_n.keys():
    sl_n[k].sort()

# 6. Show the table
print("\nStem : Leaf")
for k, v in sl_n.items():
    print(f"  {k}  : {v}")