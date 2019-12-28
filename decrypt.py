t = int(input())
x=[]
arr = []
prime_list = []
dic = {}
unsorted_list = []
initial_prime = []
alph = []
def gcd(n1, n2):
    while n2!=0:
        if n1>n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    return n1

co = 1
for i in range(t):
    x = input().split(" ")

    arr = input().split(" ")

    k=0
    while arr[k] == arr[k+1]:
        k += 1
    xb = gcd(int(arr[k]),int(arr[k+1]))

    pr = int(arr[k])//int(xb)
    initial_prime.append(pr)
    initial_prime.append(xb)

    for num in range(k+1,len(arr)):
        xa = int(arr[num])//int(xb)
        initial_prime.append(xa)
        xb = xa

    for ele in initial_prime:
        if ele not in unsorted_list:
            unsorted_list.append(ele)

    prime_list = list(unsorted_list)
    prime_list.sort()
    count = 1
    for l in prime_list:
        dic[l]=count
        count += 1

    al = ""
    for z in initial_prime:
        al = al + chr(int(dic[z])+64)
    alph.append(al)
    co += 1
    del initial_prime[0:]
    del unsorted_list[0:]
    del prime_list[0:]
for i in range(t):
    print("Case #{}: {}".format(i+1,alph[i]))    
