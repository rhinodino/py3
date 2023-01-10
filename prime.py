max = 100
flag = 0
for i in range(2, max + 1):
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break;
    if flag == 0:
        print(i)
    else:
        flag = 0
