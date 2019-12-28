def damage_cal(p,tot_dam,c_dam):
    for j in p:
        if j=='S':
            tot_dam = tot_dam + c_dam
        elif j=='C':
            c_dam = c_dam * 2
    return tot_dam





with open("robot.txt","r") as f:
    a = f.read().split('\n')
    a.remove('')
    b=[]
    c=[]
    t = a[0]
    damage = []
    pass_list=[]

    for i in a[1:]:
        b.append(i[0])
        c.append(i[2:])



    for i in c:
        tot_dam = 0
        c_dam = 1
        tot_dam = damage_cal(i,tot_dam,c_dam)
        damage.append(tot_dam)

    for i in range(len(damage)):
        tot_dam = 0
        c_dam = 1
        pas = 0
        count = 0
        p = c[i]
        d = b[i]
        pd = list(p)
        for k in range(len(p)):
            for j in reversed(range(len(pd)-1)):
                tdam = damage_cal(pd,tot_dam,c_dam)
                if(pd[j] == 'C' and pd[j+1] == 'S' and tdam>int(d)):
                    pd[j], pd[j+1] = pd[j+1], pd[j]
                    pas += 1

        if(tdam>int(d)):
            pass_list.append("IMPOSSIBLE")
        else:
            pass_list.append(pas)

    for i in range(len(pass_list)):
        print("Case #{} : {}".format(i+1,pass_list[i]))
