import sympy as sp
from decimal import Decimal as D, getcontext

getcontext().prec = 50

Q_PROTON = D("1.1099785827513808075916690956107688798744991218736")
Q_MUON = D("1.10997859555733471989976322048322502665620840878015368660798114614493")
C3_PROTON = D("-2.06934257711516784")
C3_MUON = D("-2.02018812814143946")

def y_of(q: D) -> D:
    return q*q + 1/(q*q)

def C_Hopf(y: D) -> D:
    return y**3 - 6*y**2 + 10*y - 6

def C_unknot(y: D) -> D:
    return 2*y**2 - 7*y + 4

yp = y_of(Q_PROTON)
ym = y_of(Q_MUON)

chp = C_Hopf(yp)
cup = C_unknot(yp)

print(f"Proton y: {yp}")
print(f"C_Hopf(yp): {chp}")
print(f"C_unknot(yp): {cup}")
print(f"c_3_proton^2 * C_Hopf(yp) + C_unknot(yp) = {C3_PROTON**2 * chp + cup}")
print(f"c_3_proton * C_Hopf(yp) + C_unknot(yp) = {C3_PROTON * chp + cup}")

