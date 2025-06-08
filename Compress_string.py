from itertools import groupby
s = input().strip()
compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]
print(" ".join(map(str, compressed)))
length = len(compressed)
if length == 1:
    print("Single unique character sequence")
elif 2 <= length <= 4:
    print("Moderate compression")
else:
    print("Highly compressed sequence")
