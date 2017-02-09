# Python program to calculate the most efficient height for the least surface area and a volume of 1 litre.
import math
from time import time
lsa = []
lh = []
lr = []
res = int(input("Desired Resolution (1 = 0dp, 10 = 1dp, 100 = 2dp, etc.): ")) # Lazy way to get the desired res.


def main():
    r = math.sqrt((3000/math.pi) / h) # Defining radius
    l = math.sqrt(h**2 + r**2) # Defining length
    rsq = r**2 # Defining radius^2
    v = (math.pi*rsq*h)/3 # Defining volume
    sa = math.pi*r*l # Surface area calculation
    if 999.99 < v < 1000.01 and 8.9 < r < 9.1: # Filter for only some specific values close to desires value, bounds
        lsa.append(sa)
        lh.append(h)
        lr.append(r)
t = time() # Used to calculate time taken (I personally use this program to test efficiency methods as well as hardware)
for i in range(11*res, (13*res)): # Going through the values
    h = i/res
    main()

tfinal = time()-t # Time taken
lsas = lsa
lsas.sort()
bsa = lsas[0]
bh = lh[lsa.index(bsa)]
br = lr[lsa.index(bsa)]
print("\nBest surface area: " + str(bsa) + "\nBest Height: " + str(bh) + "\nBest Radius: " + str(br) + "\n\nTime: " + str(tfinal) + " seconds, or " + str(tfinal/60) + " minutes, or " + str((tfinal/60)/60) + " hours.")
