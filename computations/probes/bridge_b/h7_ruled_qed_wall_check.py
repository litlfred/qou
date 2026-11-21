"""H7 part B, ruled reading: the carried all-pairs insertion sum_{a<b} Q_a Q_b (PR #8743 reading of
the owner's charge ruling) is diagonal and constant on each weight space, so it factors out of any
restricted trace, including one with the type-B wall. Exact sympy."""
import sympy as sp
from sympy import kronecker_product as kp
q, s, p, Y = sp.symbols('q s p Y')
I2 = sp.eye(2); H = sp.diag(1, -1)
def on(M, k):
    m = [I2, I2, I2]; m[k] = M; return kp(kp(m[0], m[1]), m[2])
Q = [on(H, k)/2 + Y/2*sp.eye(8) for k in range(3)]
C = sp.expand(Q[0]*Q[1] + Q[0]*Q[2] + Q[1]*Q[2])
Htot = on(H,0) + on(H,1) + on(H,2)
print("C diagonal:", all(C[i, j] == 0 for i in range(8) for j in range(8) if i != j))
for w in (1, -1):
    vals = {sp.factor(C[i, i]) for i in range(8) if Htot[i, i] == w}
    print(f"weight {w:+d}: C values on the weight space = {vals}")
cp = [C[i, i] for i in range(8) if Htot[i, i] == 1][0]
cn = [C[i, i] for i in range(8) if Htot[i, i] == -1][0]
print("C(n) - C(p) =", sp.factor(cn - cp), "; at Y=1/3 [conditional]: p =", cp.subs(Y, sp.Rational(1,3)), ", n =", cn.subs(Y, sp.Rational(1,3)))
