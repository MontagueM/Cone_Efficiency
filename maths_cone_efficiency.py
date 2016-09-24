import math
from time import time
lsa = []
lh = []
lr = []
res = int(input("Desired Resolution (1 = 0dp, 10 = 1dp, 100 = 2dp, etc.): "))


def main():
    r = math.sqrt((3000/math.pi) / h)
    l = math.sqrt(h**2 + r**2)
    rsq = r**2
    v = (1/3)*math.pi*rsq*h
    sa = math.pi*r*l
    if 999.99 < v < 1000.01 and 8.9 < r < 9.1:
        lsa.append(sa)
        lh.append(h)
        lr.append(r)
t = time()
for i in range(11,(13*res)):
    h = i/res
    if i % 10000000 == 0:
        print(str((i/((13*res)-1))*100) + "% | " + str(time()-t) + " seconds")
    main()
tfinal = time()-t
lsas = lsa
lsas.sort()
bsa = lsas[0]
bh = lh[lsa.index(bsa)]
br = lr[lsa.index(bsa)]
print("\nBest surface area: " + str(bsa) + "\nBest Height: " + str(bh) + "\nBest Radius: " + str(br) + "\n\nTime: " + str(tfinal) + " seconds, or " + str(tfinal/60) + " minutes, or " + str((tfinal/60)/60) + " hours.")