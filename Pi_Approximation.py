# John Burghardt
import os
k = None
while True :
    os.system('clear')
    print("π Approximation Calculator")
    print("π ≈ 4(∑_{n=0}^{k} (-1)^n/(2n+1))")
    if k == None :
            k = input("Enter k: ")
            try :
                k = int(k)
                if k <= 0 :
                    k = None
            except :
                k = None
            continue
    else :
        print("k = " + str(k))
    break
print("π ≈ 4(", end="")
sum = 1
print("1", end="")
for k in range(k + 1) :
    if k % 2 == 0 and k > 0:
        print(f"+1/{2 * k + 1}", end="")
        sum += 1 / (2 * k + 1)
    elif k % 2 == 1 :
        print(f"-1/{2 * k + 1}", end="")
        sum -= 1 / (2 * k + 1)
sum *= 4
print(f") ≈ {sum}")