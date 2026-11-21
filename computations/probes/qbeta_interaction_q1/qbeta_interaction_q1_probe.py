#!/usr/bin/env python3
"""q = 1 coefficient of every interaction quantity on record (pre-registered, PREREGISTRATION.md).

c(F) = lim_{q→1} F(q)/(q−1) is the q = 1 coefficient of Q_β/m_e under the corpus's linear form
Q_β = E₀^full·F. Exact sympy; the q₀ column is mpmath at 50 dps; CODATA only at the end.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))
import mpmath as mp
import sympy as sp
import qou_substrate.constants as C
mp.mp.dps = 50
q = sp.symbols("q", positive=True)
SRC = _ROOT / "computations/probes/beta_pair_creation_word"
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(str(C.M_E_MEV))
E0full = (1 / (q * (q - 1))) / (1 - (1 - 1 / q) ** 2)
rows = []

def order_at_1(F):
    num, den = sp.fraction(sp.factor(F))
    k = 0
    while sp.simplify(num.subs(q, 1)) == 0 and k < 40:
        num = sp.quo(sp.Poly(num, q), sp.Poly(q - 1, q)).as_expr(); k += 1
    j = 0
    while sp.simplify(den.subs(q, 1)) == 0 and j < 40:
        den = sp.quo(sp.Poly(den, q), sp.Poly(q - 1, q)).as_expr(); j += 1
    return k - j

def collect(x, path, name):
    if isinstance(x, dict):
        for k, v in x.items(): collect(v, path + "/" + str(k), name)
    elif isinstance(x, list):
        for i, v in enumerate(x): collect(v, path + f"[{i}]", name)
    elif isinstance(x, str) and "q" in x and any(t in path for t in ("cross_term", "cc_block", "conn", "chi_W")):
        try:
            F = sp.sympify(x, locals={"q": q})
        except Exception:
            return
        if not F.free_symbols <= {q}:
            return
        rows.append((name + path, F))

for f in sorted(SRC.glob("*.witness.json")):
    collect(json.loads(f.read_text()), "", f.stem)

# 1. the reduction (exact)
G = sp.Function("G")
red = sp.simplify(E0full * (q - 1) - q / (2 * q - 1))
print(f"[{'PASS' if red == 0 else 'FAIL'}] E0full*(q-1) = q/(2q-1) (so c(F) = lim F/(q-1))")

out = []
print(f"\n{len(rows)} exact interaction quantities on record")
print(f"{'quantity':90s} order  c(F)    E0*|F| at q0 (MeV)")
for name, F in rows:
    k = order_at_1(F)
    c = sp.limit(F / (q - 1), q, 1) if k >= 1 else ("diverges" if k <= 0 and sp.limit(F, q, 1) != 0 else 0)
    v = me * abs(sp.lambdify(q, E0full * F, "mpmath")(q0))
    out.append({"quantity": name, "order_at_q1": k, "c_q1": str(c), "E0F_q0_MeV": mp.nstr(v, 12)})
    print(f"{name[-90:]:90s} {k:5d}  {str(c):6s}  {mp.nstr(v, 8)}")

order1 = [o for o in out if o["order_at_q1"] == 1]
print(f"\norder >= 2 (c = 0): {sum(o['order_at_q1'] >= 2 for o in out)}; order 1: {len(order1)}; order <= 0: {sum(o['order_at_q1'] <= 0 for o in out)}")

# 3. electron Markov factor t(Δ) = z(hz+1), z = z_D
z = q**3 / (q**2 + 1); h = q - 1 / q
tD = sp.simplify(z * (h * z + 1))
print(f"electron t(Delta) at q=1: {sp.limit(tD, q, 1)}; at q0: {mp.nstr(sp.lambdify(q, tD, 'mpmath')(q0), 12)}")

print("\nComparison (CODATA, outside any proof): Q_beta/m_e = 1.530988; scored cell c = 3/4")
(_HERE / "qbeta-interaction-q1.witness.json").write_text(json.dumps({"rows": out, "electron_tDelta_q1": str(sp.limit(tD, q, 1))}, indent=1, ensure_ascii=False) + "\n")
