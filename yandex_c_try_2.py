n = int(input())
foo = [int(i) for i in input().split()]
bar = []
fib0 = 0
fib1 = 1
fib2 = 2
fib_sum = 0
for i in foo:
    if i == 0:
        bar.append(0)
    elif i == 1:
        bar.append(1)
    elif i == 2:
        bar.append(2)
    else:
        cnt = 0
        while cnt < i - 2:
            fib_sum = fib0 + fib2
            fib0 = fib1
            fib1 = fib2 
            fib2 = fib_sum
            cnt += 1
        bar.append(fib2)
        fib0 = 0
        fib1 = 1
        fib2 = 2
        cnt = 0
print(" ".join(str(i) for i in bar))

