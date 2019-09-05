foo = input()
cnt = 0
temp = ''
for i in range(len(foo) - 1):
    if ord(foo[i]) > 64:
        if ord(foo[i + 1]) < 64:
            temp += foo[i + 1]
            if i + 2 == len(foo):
                cnt += int(temp)
        else:
            cnt += 1
            if i + 2 == len(foo):
                cnt += 1
    else:
        if ord(foo[i + 1]) > 64:
            cnt += int(temp)
            temp = ''
            if i + 2 == len(foo):
                cnt += 1
        else:
            temp += foo[i + 1]
            if i + 2 == len(foo):
                cnt += int(temp)

print(cnt)
