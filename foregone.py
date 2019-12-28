t = int(input())
lot=[]
for i in range(t):
    x = input()
    lot.append(x)
mod = []
rem = []
for i in lot:
    num = list(i)
    for j in range(len(num)):
        no = int(num[j])
        if no == 4:
            num[j] = no - 1
    s = ''.join(str(x) for x in num)
    rem.append(int(i) - int(s))
    mod.append(s)
for i in range(len(mod)):
    print("Case {}: {} {}".format(i+1, int(mod[i]), int(rem[i])))
