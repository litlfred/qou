"""Exact sympy check of PREREGISTRATION-s46.md (both §46 identities), full 16-dim space.
Bit j of a basis index s is the spin on strand j (0 = zero). No float64."""
import itertools, sympy as sp
q = sp.symbols('q', nonzero=True); h = q - 1/q
f0, f1, f01, g0, g1, g01 = sp.symbols('phi0 phi1 phi01 psi0 psi1 psi01')
bit = lambda s, j: (s >> j) & 1
def gen(i):
    M = sp.zeros(16, 16)
    for s in range(16):
        a, b = bit(s, i), bit(s, i + 1)
        if a == b: M[s, s] = q
        elif a == 0: M[s ^ (3 << i), s] = 1
        else: M[s ^ (3 << i), s] = 1; M[s, s] = h
    return M
I = sp.eye(16); S_ = [gen(i) for i in range(3)]; Si = [m - h * I for m in S_]
def word(ls):
    M = I
    for (i, inv) in ls: M = M * (Si[i] if inv else S_[i])
    return M
zeros = lambda s, js: sum(1 for j in js if bit(s, j) == 0)
def O(W, prot, w):
    return sp.simplify(sum((zeros(s, range(4)) - 2) * W[s, s] for s in range(16) if zeros(s, prot) == w))
KL = word([(2, 1), (1, 1), (0, 1), (0, 1), (1, 1), (2, 1)]); KR = word([(0, 1), (1, 1), (2, 1), (2, 1), (1, 1), (0, 1)])
L, Rp = [0, 1, 2], [1, 2, 3]
checks = []
def chk(name, expr):
    ok = sp.simplify(expr) == 0; checks.append(ok); print("PASS" if ok else "FAIL", name)
# mechanism
for i in (0, 1): chk(f"K_L commutes with sigma_{i}", 0 if (S_[i] * KL - KL * S_[i]).applyfunc(sp.simplify).is_zero_matrix else 1)
for i in (1, 2): chk(f"K_R commutes with sigma_{i}", 0 if (S_[i] * KR - KR * S_[i]).applyfunc(sp.simplify).is_zero_matrix else 1)
SKL = sp.factor(O(KL, L, 2) + O(KL, L, 1)); print("S(K_L) =", SKL)
chk("S(K_L) = -h^2[3]_q/q^2", SKL + h**2 * (q**2 + 1 + q**-2) / q**2)
def ev(x, sh):  # x: list of (coeff, word over letters s0,s1 with inverse flag)
    return sum((c * word([(i + sh, b) for (i, b) in w]) for c, w in x), sp.zeros(16, 16))
def gam(p0, p1, p01): return [(1, []), (p0, [(0, 0)]), (p1, [(1, 0)]), (p01, [(0, 0), (1, 1)])]
def mul(x, y): return [(a * b, u + v) for a, u in x for b, v in y]
chi = lambda x: sp.simplify(sum(c * sp.prod([q if b == 0 else 1 / q for (_, b) in w]) for c, w in x))
arms = {"1": [(1, [])], "V": [(1, [(0, 0), (1, 1)])], "s1": [(1, [(1, 0)])], "s1s0": [(1, [(1, 0), (0, 0)])]}
basis = {"1": [(1, [])], "s0": [(1, [(0, 0)])], "s1": [(1, [(1, 0)])], "s0s1": [(1, [(0, 0), (1, 0)])], "s1s0": [(1, [(1, 0), (0, 0)])],
         "s0s1s0": [(1, [(0, 0), (1, 0), (0, 0)])], "s0^-1s1^-1": [(1, [(0, 1), (1, 1)])]}
fam = {**{"basis " + k: v for k, v in basis.items()},
       **{"arm " + k + " (phi,psi symbolic)": mul(mul(gam(f0, f1, f01), gam(g0, g1, g01)), g) for k, g in arms.items()},
       **{"arm " + k + " (derived weights qh,-h/q)": mul(mul(gam(0, 0, q * h), gam(0, 0, -h / q)), g) for k, g in arms.items()}}
for name, x in fam.items():
    NL, NR = ev(x, 0), ev(x, 1); WL, WR = NL * KL, NR * KR
    chk(f"(i) {name}", O(WL, L, 2) + O(WL, L, 1) - chi(x) * SKL)
    chk(f"(ii a) {name}: O+R = -O-L", O(WR, Rp, 2) + O(WL, L, 1))
    chk(f"(ii b) {name}: O-R = -O+L", O(WR, Rp, 1) + O(WL, L, 2))
    if name.startswith("arm") and "symbolic" in name:
        print("   chi_(3) =", sp.factor(chi(x)))
print(f"{sum(checks)}/{len(checks)} checks pass")
