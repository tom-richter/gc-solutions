import math
LIMIT = 100


def isDigit(num):
    return num >= 0 and num <= 9 and math.floor(num) == num


for A in range(0, LIMIT):
    for B in range(0, LIMIT):
        for C in range(0, LIMIT):
            try:
                if isDigit(1+C-B-B/A) and isDigit((C-1)/A+B-2) and isDigit((C+2)/A+B) and isDigit(B-C+A) and isDigit(C-A+B/(2*A)) and isDigit((C+2)/(A+B)):
                    print('A =', A, 'B =', B, 'C =', C)
            except:
                pass
