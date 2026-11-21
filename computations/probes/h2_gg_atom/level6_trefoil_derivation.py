"""Closed-form derivation of the level-6 (3,3) failure of bare H2 with the trefoil electron.

Bean qou-a1hh, PR #7741. Exact arithmetic in sympy over Q(q); the one numerical step
evaluates at the proton pin with mpmath and compares with h2-gg-atom.witness.json.
No witness is written: this script checks an identity, it computes no new observable.

chi_(3,3)(p (x) e) = chi_(3)(p) chi_(3)(e) + chi_(2,1)(p) chi_(2,1)(e)   (H3 (x) H3 branching)
"""
import json, pathlib, sys
import sympy as sp
from mpmath import mp, mpf

q = sp.symbols("q", positive=True)
br = q + 1 / q
x, y = -q**-2 / br, q**2 / br          # seminormal diagonal of sigma_1 on (2,1)
off = sp.sqrt(1 + x * y)               # off-diagonal: det(sigma_1) = -1
s0 = sp.diag(q, -1 / q)
s1 = sp.Matrix([[x, off], [off, y]])
ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)

# Cayley-Hamilton: trace q - 1/q and det -1 give sigma_1^2 = (q - 1/q) sigma_1 + 1
check("Hecke relation (trace, det)", sp.simplify(s1.trace() - (q - 1/q)) == 0 and sp.simplify(s1.det() + 1) == 0)
check("braid relation", sp.simplify(s0*s1*s0 - s1*s0*s1) == sp.zeros(2))
c21 = lambda M: sp.simplify(M.trace())
V = s0 * s1.inv()
c21_tref, c21_tw0, c21_V3 = c21(s0**3 * s1), c21(s0 * s1 * s0), sp.factor(c21(V**3))
check("chi_(2,1)(s0^3 s1) = -1", sp.simplify(c21_tref + 1) == 0)
check("chi_(2,1)(s0 s1 s0) = 0", sp.simplify(c21_tw0) == 0)
target = -(q**4 - q**2 + 1) * (q**8 - 2*q**6 - 2*q**2 + 1) / q**6
check("chi_(2,1)(V^3) closed form", sp.simplify(c21_V3 - target) == 0)

# trefoil: chi_3(e)=q^4, chi_3(V^3)=1 (writhe 0)
ratio = sp.simplify((q**4 * 1 + c21_V3 * c21_tref) / (q**4 * 1))
mp.dps = 40
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "tools/qou-substrate/python"))
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = mpf(Q_50_DIGIT_STR)
pred = mpf(str(sp.N(ratio.subs(q, sp.Rational(Q_50_DIGIT_STR)), 45)))
w = json.load(open(pathlib.Path(__file__).with_name("h2-gg-atom.witness.json")))
ch = w["results"]["V^3"]["electron=trefoil_s0s0s0s1,atom2=pe"]["rows"][0]["chars"]
meas = mpf(ch["6:(3, 3)"]) / mpf(ch["6:(6,)"])
print("predicted (3,3)/(6) =", mp.nstr(pred, 20), " witness =", mp.nstr(meas, 20))
check("matches witness to 1e-18", abs(pred - meas) < mpf("1e-18"))
print("chi_(2,1)(V^3) at q0 =", mp.nstr(mpf(str(sp.N(target.subs(q, sp.Rational(Q_50_DIGIT_STR)), 45))), 20))
sys.exit(0 if ok else 1)
