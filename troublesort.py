with open("trouble.txt", "r") as f:
    a = f.read().split('\n')
    a.remove('')
    test = a[0]
    n = []
    v = []
    [n.append(a[i]) for i in range(len(a)) if (i % 2 != 0 and i>0)]
    [v.append(a[i]) for i in range(len(a)) if (i % 2 == 0 and i>0)]

    fault = []
    flag = -1
    for i in range(len(n)):
        num = n[i]
        e = v[i]
        ele = list(e)
        [ele.remove(' ') for j in range(len(ele)//2)]

        for j in range(len(n)):
            for k in range(len(ele)-2):
                if ele[k] > ele[k+2]:
                    ele[k], ele[k+2] = ele[k+2], ele[k]

        for i in range(len(ele)-1):
            if(ele[i] > ele[i+1]):
                fault.append(i)
                flag = 1
                break

        if(flag != 1):
            fault.append("OK")

    for i in range(len(fault)):
        print("Case #{}: {}".format(i+1, fault[i]))
