import math

Type = input('What Type (A, N, M)? ')


def give(givens):
    a = []
    g = givens.split()
    for i in g:
        a.append(i)
    return a


def needshalf(t, x, xo):
    answer = (math.log2(x/xo))*float(t)
    answer = answer * float(-1)
    return answer


def needst(half, x, xo):
    answer = (math.log2(x/xo))*float(half)
    answer = answer * float(-1)
    return answer


def needsx(half, t, xo):
    answer = float(xo)*(1/2) ** (t/half)
    return answer


def needsxo(half, t, x):
    answer = float(x)/((1/2) ** (t/half))
    return answer


Givens = input(
    'Givens (order: t 1/2, t, X, Xo. If haven\'t got then put in ?) ')
a = give(Givens)
half = a[0]
time = a[1]
X = a[2]
Xo = a[3]
if Type == 'A':
    if half == '?':
        answer = needshalf(float(time), float(X), float(Xo))
        print(f'Half-Life = {answer}')
    elif time == '?':
        answer = needst(float(half), float(X), float(Xo))
        print(f'Time = {answer}')
    elif X == '?':
        answer = needsx(float(half), float(time), float(Xo))
        print(f'Activity = {answer}')
    elif Xo == '?':
        answer = needsxo(float(half), float(time), float(X))
        print(f'Original Activity = {answer}')
elif Type == 'N':
    if half == '?':
        answer = needshalf(float(time), float(X), float(Xo))
        print(f'Half-Life = {answer}')
    elif time == '?':
        answer = needst(float(half), float(X), float(Xo))
        print(f'Time = {answer}')
    elif X == '?':
        answer = needsx(float(half), float(time), float(Xo))
        print(f'Number of Nuclei = {answer}')
    else:
        answer = needsxo(float(half), float(time), float(X))
        print(f'Original Number of Nuclei = {answer}')
elif Type == 'M':
    if half == '?':
        answer = needshalf(float(time), float(X), float(Xo))
        print(f'Half-Life = {answer}')
    elif time == '?':
        answer = needst(float(half), float(X), float(Xo))
        print(f'Time = {answer}')
    elif X == '?':
        answer = needsx(float(half), float(time), float(Xo))
        print(f'Mass = {answer}')
    else:
        answer = needsxo(float(half), float(time), float(X))
        print(f'Original Mass = {answer}')
