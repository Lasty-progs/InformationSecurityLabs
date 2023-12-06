a = 17
b = 11
c = 256
MaxVal = 255
t0 = 172


def KSum(P):
    s = 0
    for i in P:
        s += ord(i)
    return s % c

def SummKodBukvOtkr(P):
    Y = []
    for i, item in enumerate(P):
        Y.append(int(binXor(bin(ord(item)), t(i)), 2))

    s = 0
    for i in Y:
        s += i
    return s

def t(i):
    if i == 0:
        return bin(t0)
    return bin((a*int(t(i-1), 2)+b)%c)

def binXor(a, b):
    out = "0b"
    for i, j in zip(a[2:], b[2:]):
        i , j = int(i), int(j)
        out += str((i+j)%2)
    return out

l = ["0123456789", "9876543210", "1000005", "1500000"]
for i in l:
    print(f"P = {i}, KSumm = {KSum(i)}, SummKodBukvOtkr = {SummKodBukvOtkr(i)}" )
