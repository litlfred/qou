"""Bridge B, h3: the intertwiner P of NucleonWeightSpaceTraces is the total lowering operator.

Exact sympy, no numerical value of q. Checks:
  1. Delta(F) = F(x)1 + K^-1(x)F commutes with the Jimbo R-check (so it is the coproduct to use).
  2. The block of F3 = F(x)1(x)1 + K^-1(x)F(x)1 + K^-1(x)K^-1(x)F from the (2,1) weight space
     (basis e1e1e2, e1e2e1, e2e1e1) to the (1,2) weight space (e1e2e2, e2e1e2, e2e2e1)
     equals q * P, with P the intertwiner in NucleonWeightSpaceTraces.lean.
  3. F3 commutes with sigma_1 = R(x)1 and sigma_2 = 1(x)R on (C^2)^{(x)3}.
Lean counterpart: NucleonIsospinExclusions.lowerBlock_eq / commutant_trace_eq.
"""
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
K = sp.diag(q, 1 / q)
F = sp.Matrix([[0, 0], [1, 0]])
I2 = sp.eye(2)
kp = sp.kronecker_product

ok = True
DF = kp(F, I2) + kp(K.inv(), F)
c1 = sp.simplify(DF * R - R * DF) == sp.zeros(4)
print("1. Delta(F) commutes with R:", c1); ok &= c1

F3 = kp(kp(F, I2), I2) + kp(kp(K.inv(), F), I2) + kp(kp(K.inv(), K.inv()), F)
Wp = [1, 2, 4]   # e1e1e2, e1e2e1, e2e1e1  (index 4a+2b+c, e1=0)
Wm = [3, 5, 6]   # e1e2e2, e2e1e2, e2e2e1
F0 = sp.Matrix(3, 3, lambda i, j: F3[Wm[i], Wp[j]])
P = sp.Matrix([[q**-2, 1 / q, 0], [1 / q, 0, 1 / q], [0, 1 / q, 1]])
c2 = sp.simplify(F0 - q * P) == sp.zeros(3)
print("2. lowering block =", F0.tolist(), "; equals q*P:", c2); ok &= c2

s1 = kp(R, I2); s2 = kp(I2, R)
c3 = all(sp.simplify(F3 * s - s * F3) == sp.zeros(8) for s in (s1, s2))
print("3. F3 commutes with sigma_1, sigma_2:", c3); ok &= c3

print("ALL CHECKS PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
