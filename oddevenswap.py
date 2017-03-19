list = [0,'a',1,'b',2,'c',3,'e',4,'f',5,'g',6,'h',7,'i',8,'j',9,'k']
#list = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
print(list)


def swap(lst,e):
    i = 0
    swap = lst
    for l in list:
        if i != len(list) - 1:
            if i % 2 == e:
                temp = l
                swap[i] = list[i + 1]
                swap[i + 1] = temp
        else:
            if e == 1:
                temp = l
                swap[i] = list[0]
                swap[0] = temp
        i += 1
    return swap

cnt = 0
odd = 0
while (cnt < 20):
    list = swap(list,odd)
    print(list)
    odd = (odd + 1) % 2
    cnt += 1
