from collections import Counter
n = int(input())
foo = [int(i) for i in input().split()]
foo.sort()
foo.reverse()
num_counts = Counter(foo)
maxx = num_counts.most_common(1)
print(maxx[0][0])