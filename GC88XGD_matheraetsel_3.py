# Solution for GC88XGD - Matherätsel # 3

def digit_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


for a in range(19, 200):
    for b in range(1, 10):
        for c in range(1, 180):
            for d in range(1, 18):
                if (a+b != d*d):
                    continue
                for e in range(1, 20):
                    if (a+c != e*e) or (d >= e):
                        continue
                    for f in range(1, 19):
                        if (e>f>d) and (b+c == f*f) and ((a+b+c+d+e+f) < 200)  and (digit_sum(a+b+c+d+e+f) == 11):
                            print("a =", a)
                            print("b =", b)
                            print("c =", c)
                            print("d =", d)
                            print("e =", e)
                            print("f =", f)
