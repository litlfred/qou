import sympy as sp
from decimal import Decimal as D, getcontext

getcontext().prec = 50

def y_of(q: D) -> D:
    return q*q + D('1')/(q*q)

def h_of(q: D) -> D:
    return q - D('1')/q

# Physical anchors
Q_PROTON = D("1.1099785827513808075916690956107688798744991218736")
C3_PROTON = D("-2.06934257711516784")

yp = y_of(Q_PROTON)
hp = h_of(Q_PROTON)

def C_Hopf(y: D) -> D:
    return y**3 - 6*y**2 + 10*y - 6

def C_unknot(y: D) -> D:
    return 2*y**2 - 7*y + 4

chp = C_Hopf(yp)
cup = C_unknot(yp)

# We want w_p^2 * C_Hopf(yp) + C_unknot(yp) = c3_proton
w2_p = (C3_PROTON - cup) / chp

print(f"w_p^2 needed: {w2_p}")
print(f"h_p^2: {hp**2}")
print(f"Ratio w_p^2 / h_p^2: {w2_p / (hp**2)}")

# Let's test a theoretical form for w(q):
# What if w(q) = h(q) / sqrt(1 - a*h(q)^2) or something?
# Let's check other integer relations
ratio = w2_p / (hp**2)

# Could it be exactly y - 2 ? (which is h^2) No.
# Could it be related to (q^2 - q^-2)^2?
q2_minus_q_minus_2_sq = (Q_PROTON**2 - D('1')/(Q_PROTON**2))**2
print(f"(q^2 - q^-2)^2: {q2_minus_q_minus_2_sq}")
print(f"Ratio: {w2_p / q2_minus_q_minus_2_sq}")

# Let's check the exact formula for w(q)
# Maybe c3 is NOT exactly equal to w^2 C_Hopf + C_unknot ?
# What if c3 = w^2 C_Hopf + 1 ?
