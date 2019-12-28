t = int(input())
n=[]
p=[]
ans=[]

for i in range(t*2):
    if i%2==0:
        a = int(input())
        n.append(a)
    else:
        a = input()
        p.append(a)

for s in p:
    st = list(s)
    for i in range(len(st)):
        if st[i] == 'E':
            st[i] = 'S'
        elif st[i] == 'S':
            st[i] = 'E'
    ans.append(''.join(st))

for i in range(t):
    print("Case #{}: {}".format(i+1, ans[i]))
