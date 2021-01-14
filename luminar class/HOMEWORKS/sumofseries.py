n = input("ENTER THE VALUE : ")
s = 0
if int(n) >= 1 and int(n) <= 9:
    for i in range(1, int(n)+1):
        s = s + int(n * i)
    print("SUM OF SERIES : ", s)
else :
    print("INVALID INPUT")
