import sympy as sp
from decimal import Decimal as D, getcontext

getcontext().prec = 50

# The physical anchors
Q_PROTON = D("1.1099785827513808075916690956107688798744991218736")
Q_MUON = D("1.10997859555733471989976322048322502665620840878015368660798114614493")

def y_of(q: D) -> D:
    return q*q + D('1')/(q*q)

def h_of(q: D) -> D:
    return q - D('1')/q

def C_Hopf(y: D) -> D:
    return y**3 - 6*y**2 + 10*y - 6

def C_unknot(y: D) -> D:
    return 2*y**2 - 7*y + 4

yp = y_of(Q_PROTON)
hp = h_of(Q_PROTON)

# Let's test a few simple w(q)^2 expressions
# Hypothesis 1: w^2 = h^2 = y - 2
w2_h1 = yp - D('2')
c3_h1 = w2_h1 * C_Hopf(yp) + C_unknot(yp)

# Hypothesis 2: w^2 = (q - 1)^2 ?
# Actually, typically w(q) is related to (q - q^-1) / (q + q^-1) or similar.
w_val_needed = (D('-2.06934257711516784') - C_unknot(yp)) / C_Hopf(yp)

print(f"Required w^2 for proton c3 (-2.06934257711516784): {w_val_needed}")
print(f"h^2 (y-2) at proton: {w2_h1}")
print(f"c3 under Hyp 1: {c3_h1}")

# Let's calculate exactly what function f(y) produces w_val_needed
print(f"Ratio of w^2 to h^2: {w_val_needed / w2_h1}")
