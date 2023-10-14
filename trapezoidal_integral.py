from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

from math import pi
a = 0
b = (1/2) * pi
N = 100
h = (b-a) / N
S = 0
for k in range(1, N+1):
    S += ((h/2) * (sin(a+(k - 1)*h) + sin(a + k*h)))
print(S)