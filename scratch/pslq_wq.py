import sympy as sp
from decimal import Decimal as D, getcontext
import mpmath as mp

mp.dps = 45

q = mp.mpf("1.1099785827513808075916690956107688798744991")
c3 = mp.mpf("-2.06934257711516784") # Wait, is c3 known to more precision?

y = q*q + 1/(q*q)
h = q - 1/q

C_Hopf = y**3 - 6*y**2 + 10*y - 6
C_unknot = 2*y**2 - 7*y + 4

w2 = (c3 - C_unknot) / C_Hopf

print(f"w2 = {w2}")
print(f"h2 = {h**2}")

# Let's try to find an integer relation for w2 in terms of y
# We are looking for sum a_i * x_i = 0
# For example, w2, y, h^2, 1
basis = [w2, h**2, y, mp.mpf(1), w2*y, h**4]
try:
    rel = mp.pslq(basis)
    print(f"Integer relation found: {rel}")
except:
    print("No integer relation found with standard basis")

# Try an affine relation w2 = (a*y + b) / (c*y + d) * h^2
# Which means w2 * (c*y + d) - h^2 * (a*y + b) = 0
basis2 = [w2 * y, w2, h**2 * y, h**2]
try:
    rel2 = mp.pslq(basis2)
    print(f"Integer relation for affine h^2 modifier: {rel2}")
except:
    pass

# Is w2 a rational function of y?
basis3 = [w2 * y**2, w2 * y, w2, y**2, y, mp.mpf(1)]
try:
    rel3 = mp.pslq(basis3)
    print(f"Integer relation for rational function of y: {rel3}")
except:
    pass
